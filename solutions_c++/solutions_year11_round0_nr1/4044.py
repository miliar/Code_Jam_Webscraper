env = Environment(CXXFLAGS="-std=c++0x")
env.MergeFlags("-pthread -Wall -Werror")
env.Replace(CXX = "g++-4.5")
env.Program("bot_trust", "main.cpp")
