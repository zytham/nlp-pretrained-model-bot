
import os
import transformers


def initialize_model():

  model = transformers.pipeline("conversational", model="facebook/blenderbot_small-90M")
  os.environ["TOKENIZERS_PARALLELISM"] = "true"

  return model


def get_bot_response(model, user_input):

  chat = model(transformers.Conversation(user_input))
  bot_response = str(chat)
  bot_response = bot_response[bot_response.find("bot >> ")+6:].strip()

  return bot_response