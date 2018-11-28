// SAI [ 9 April 2012 ]
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <vector>

//#include "lib/MyBlock.h"
//#include "lib/Block.h"
//#include "lib/RegEx.h"
//#include "lib/Utils.h"

int main(void)
{
  char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

  int cases = 0;

  std::string num;
  std::getline(std::cin, num);
  cases = atoi(num.c_str());
  
  for (int cse = 0; cse < cases; cse += 1)
  {
    std::string txt;
    std::getline(std::cin, txt);

    std::string out;
    for (int i = 0; i < txt.length(); i += 1)
    {
      char ch = txt.at(i);
      if (ch != ' ') 
        ch = map[(int)(ch - 'a')];
      char tmp [2] = {ch , 0};
      out.append(tmp);
    }
    std::cout << "Case #" << (cse + 1) << ": " << out << std::endl;
  }

  return 0;
}

int main2(void)
{
  int cases = 0;

  std::string num;
  std::getline(std::cin, num);
  cases = atoi(num.c_str());

  char map[256] = {0};
  for (int cse = 0; cse < cases; cse += 1)
  {
    std::string from;
    std::string to;
    std::getline(std::cin, from);
    std::getline(std::cin, to);
     
    std::cout << "Read " << from << std::endl;
    std::cout << "Read " << to << std::endl;
    for (int i = 0; i < from.length(); i += 1)
    {
      int index = (int) from.at(i); 
      if (map[index] != 0 && map[index] != to.at(i))
      {
        std::cout << "Conflict " << from.at(i) << " and " << to.at(i) << std::endl;
      }
      else
      {
        map[index] = to.at(i);
      }
    }  
  }

  for (int i = 0; i < 256; i += 1)
  {
    char from = (char) i;
    if (map[i] != 0)
    {
      std::cout << "\'" << map[i] << "\', ";
      //std::cout << map[i] << std::endl; 
    }
  }
  return 0;
}

