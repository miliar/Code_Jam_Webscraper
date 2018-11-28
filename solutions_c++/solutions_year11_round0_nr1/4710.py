//============================================================================
// Name        : BotTrust.cpp
// Author      : Sohail Munir Khan
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
#include "fstream"
using namespace std;
typedef long long i64;

#define EMPTY_LOCATION 'E'
#define EMPTY_LOCATION_NUM -1

struct loc
{
  char C;
  int N;
  loc() :
    C(EMPTY_LOCATION), N(EMPTY_LOCATION_NUM)
  {
  }
};

loc*
findNext(char type, loc* current)
{
  while (current->C != EMPTY_LOCATION)
    {
      if (type == current->C)
        {
          return current;
        }
      ++current;
    }
  return 0;
}

int output;
int currentO = 1;
int currentB = 1;
int nextO;
int nextB;

void
stepB(bool);

void
stepO(bool initiater)
{
  if (nextO == EMPTY_LOCATION_NUM)
    {
    }
  if (currentO < nextO)
    {
      ++currentO;
    }
  else if (currentO > nextO)
    {
      --currentO;
    }
  if (initiater)
    {
      stepB(false);
      ++output;
    }
}

void
pressO(void)
{
  stepB(false);
  ++output;
}

void
stepB(bool initiater)
{
  if (nextB == EMPTY_LOCATION_NUM)
    {
    }
  if (currentB < nextB)
    {
      ++currentB;
    }
  else if (currentB > nextB)
    {
      --currentB;
    }
  if (initiater)
    {
      stepO(false);
      ++output;
    }
}

void
pressB(void)
{
  stepO(false);
  ++output;
}

int
main(void)
{
  //ifstream fin("FirstInput.in");
  istream& whereFrom = cin;

  int T;
  whereFrom >> T;
  for (int Ti = 1; Ti <= T; ++Ti)
    {
      //fprintf(stderr, "Case #%d of %d...\n", Ti, T);
      int n;
      whereFrom >> n;
      loc next[100];
      output = 0;
      for (int i = 0; i < n; ++i)
        {
          whereFrom >> next[i].C;
          whereFrom >> next[i].N;
        }
      int i = 0;
      loc* current = next;
      char currentlyServing = current->C;
      loc* temp = 0;
      currentO = 1;
      currentB = 1;
      nextO = 0 != (temp = findNext('O', current)) ? temp->N
          : EMPTY_LOCATION_NUM;
      nextB = 0 != (temp = findNext('B', current)) ? temp->N
          : EMPTY_LOCATION_NUM;
      while (i < n)
        {
          if ('O' == currentlyServing)
            {
              while (nextO != currentO)
                {
                  stepO(true);
                }
              pressO();
            }
          else if ('B' == currentlyServing)
            {
              while (nextB != currentB)
                {
                  stepB(true);
                }
              pressB();
            }
          ++i;
          ++current;
          currentlyServing = current->C;
          nextO = 0 != (temp = findNext('O', current)) ? temp->N
              : EMPTY_LOCATION_NUM;
          nextB = 0 != (temp = findNext('B', current)) ? temp->N
              : EMPTY_LOCATION_NUM;
        }
      //if ((k + 1) % (1 << n) == 0) printf("Case #%d: %s\n", Ti, "ON");
      //else printf("Case #%d: %s\n", Ti, "OFF");
      printf("Case #%d: %d\n", Ti, output);
    }
  //fin.close();
  return 0;
}
