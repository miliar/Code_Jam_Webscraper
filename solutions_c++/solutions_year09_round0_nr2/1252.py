// p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "memory.h"

#include <iostream>

using namespace std;

int ntests;

int fld[128][128];
char ans[128][128];
int h, w;

int Fld(int i, int j)
  {
  if (i >= 0 && i < h && j >= 0 && j < w)
    return fld[i][j];
  else 
    return 1000000000;
  }

char Spread(int i, int j, char& c)
  {
  if (ans[i][j] != 0)
    return ans[i][j];

  int minv = min(min(Fld(i - 1, j), Fld(i + 1, j)), min(Fld(i, j - 1), Fld(i, j + 1)));

  if (minv >= Fld(i, j))
    return ans[i][j] = c++;
  
  if (Fld(i - 1, j) == minv)
    return ans[i][j] = Spread(i - 1, j, c);
  else if (Fld(i, j - 1) == minv)
    return ans[i][j] = Spread(i, j - 1, c);
  else if (Fld(i, j + 1) == minv)
    return ans[i][j] = Spread(i, j + 1, c);
  else if (Fld(i + 1, j) == minv)
    return ans[i][j] = Spread(i + 1, j, c);
  else
    while (true);

  return 0;
  }

int _tmain(int argc, _TCHAR* argv[])
  {
  cin >> ntests;
  for (int ctest = 0; ctest < ntests; ++ctest)
    {
    cin >> h >> w;
    for (int i = 0; i < h; ++i)
      for (int j = 0; j < w; ++j)
        cin >> fld[i][j];

    memset(ans, 0, sizeof(ans));

    char next = 'a';
    for (int i = 0; i < h; ++i)
      for (int j = 0; j < w; ++j)
        if (ans[i][j] == 0)
          Spread(i, j, next);

    printf("Case #%d:\n", ctest + 1);

    for (int i = 0; i < h; ++i)
      for (int j = 0; j < w; ++j)
        cout << char(ans[i][j]) << ((j == w - 1) ? "\n" : " ");
    }
  
	return 0;
  }

