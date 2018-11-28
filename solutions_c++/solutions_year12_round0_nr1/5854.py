#ifndef CONFIG_H_
#define CONFIG_H_

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using std::string;
using std::map;
using std::vector;
using std::ifstream;

class Config {
  public:
    static Config* LoadConfig(string filename);
    ~Config();
    void AddToAlphabet(char english, char googlerese);
    bool CheckAlphabetComplete();
    map<char,char>* GetAlphabet();
  private:
    Config();
    vector<string>* ReadInput(ifstream* file, int number);
    vector<string>* ReadOutput(ifstream* file, int number);
    map<char,char>* alphabet_;
};

#endif
