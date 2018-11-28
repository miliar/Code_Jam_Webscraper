#ifndef MagickaH
#define MagickaH

#include <map>
#include <string>

typedef std::map<std::string,char> CombineMap;  // string two char
typedef std::map<std::string,char> OppositeMap; // string two char


// ----------------------------------------------------------------------------
// Magicka
// ----------------------------------------------------------------------------
class Magicka
{
public:
  CombineMap  combineMap;
  OppositeMap oppositeMap;
  std::string elementList;

public:
  void clear();
  void process(char ch);
};

#endif // MagickaH