#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>

std::map<std::string, int> cache;

template<typename T>
static std::string itos(T value)
{
  std::string str;
  if(value == 0) {
    str = "0";
    return str;
  }
  unsigned int count = 0;
  while(value) {
    ++count;
    char digit = value%10+'0';
    str.insert(str.begin(), digit);
    value /= 10;
  }
  return str;
}

int countEgSwitch(const std::vector<std::string>& egs,
		  const std::vector<std::string>& words,
		  size_t index,
		  std::string curEg)
{
  std::map<std::string, int>::const_iterator i = cache.find(curEg+itos(index));
  if(i != cache.end()) {
    return (*i).second;
  }
  if(index == words.size()) {
    return 0;
  }
  int change = words.size();
  for(std::vector<std::string>::const_iterator i = egs.begin(); i != egs.end();
      ++i) {
    if((*i) != words[index]) {
      int c = countEgSwitch(egs, words, index+1, *i);
      if((*i) != curEg && !curEg.empty()) {
	++c;
      }
      change = std::min(c, change);
    }
  }
  cache[curEg+itos(index)] = change;
  return change;
}

int main(int argc, char** argv)
{
  std::ifstream in(argv[1]);
  int numCase;
  in >> numCase;
  for(int cases = 0; cases < numCase; ++cases) {
    std::string line;
    int numEgs;
    in >> numEgs;
    in >> std::ws;
    std::vector<std::string> egs;
    for(int i = 0; i < numEgs; ++i) {
      getline(in, line);
      egs.push_back(line);
    }
    int numWords;
    in >> numWords;
    in >> std::ws;
    std::vector<std::string> words;
    for(int i = 0; i < numWords; ++i) {
      getline(in, line);
      words.push_back(line);
    }
    std::cout << "Case #" << cases+1 << ": "
	      << countEgSwitch(egs, words, 0, "") << std::endl;
    cache.clear();
  }
}
