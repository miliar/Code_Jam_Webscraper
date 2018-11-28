// SAI [ 9 April 2012 ]
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>

typedef struct {
  uint32_t a;
  uint32_t b;
}Pair;

typedef std::vector<Pair*>           PairList;
typedef std::vector<Pair*>::iterator PairListIterator;

void rotate(std::string& txt);
void add(uint32_t a, uint32_t b, PairList& list);
bool has(uint32_t a, uint32_t b, PairList& list);

int main(void)
{
  int cases = 0;
  std::cin >> cases;  
  for (int cse = 0; cse < cases; cse += 1)
  {
    std::string start,end;
    std::cin >> start;
    std::cin >> end;
  
    int digits = start.length()- 1; 

    uint32_t answer = 0;
    uint32_t s = atoi(start.c_str());
    uint32_t e = atoi(end.c_str());
    PairList list;
    for (int r = s; r < e+1; r += 1)
    {
      char tmp[20];
      sprintf(tmp, "%u", r);
      start = tmp;
      std::string orig = start;
      for (int i = 0; i < digits; i += 1)
      {
        rotate(start);
        uint32_t num1 = atoi(orig.c_str());
        uint32_t num2 = atoi(start.c_str());
        if (num1 != num2 && num1 >= s && num1 <= e && num2 <= e && num2 >= s && !has(num1, num2, list))
        {
          //std::cout << orig << " vs. " << start << std::endl;
          answer += 1;
          add(num1, num2, list);
        } 
      }
    } 
    std::cout << "Case #" << (cse+1) << ": " << answer << std::endl;
  }
  return 0;
}

void 
rotate(std::string& txt)
{
  char * buff1 = strdup(txt.c_str());
  char * buff2 = strdup(txt.c_str());
  strncpy(buff2 + 1, buff1, txt.length() - 1);
  buff2[0] = buff1[txt.length() - 1];
  txt = buff2;
}

void 
add(uint32_t a, uint32_t b, PairList& list)
{
  if (a > b)
  {
    int c = b;
    b = a;
    a = c;
  }

  Pair * pair = new Pair();
  pair->a = a;
  pair->b = b;

  list.push_back(pair);
}

bool 
has(uint32_t a, uint32_t b, PairList& list)
{
  if (a > b)
  {
    int c = b;
    b = a;
    a = c;
  }

  int size = list.size();
  for(int i = 0; i < size; i += 1)
  {
    Pair * pair = list.at(i);
    if (pair->a == a && pair->b == b) return true;
  }
  return false;
}

