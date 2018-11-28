
#include <cstring>
#include <iostream>
#include <cstdio>

using namespace std;

int g_nCount[256];
int Count(char* szNum)
{
  int nRes = 0;

  memset(g_nCount, 0, sizeof(g_nCount));
  for (int i = 0; szNum[i]; i++)
    if((g_nCount[szNum[i]]++) == 0)
      nRes++;

  if (nRes == 1)
    nRes++;

  return nRes;
}

typedef unsigned long long LInt;

int g_nMap[256];
LInt Solve(char* szNum)
{
  int nBase = Count(szNum);
  int nN = strlen(szNum);

  LInt nRes = 0, nPow = 1;
  for (int i = 1; i < nN; i++)
    nPow *= LInt(nBase);

  memset(g_nMap, 0, sizeof(g_nMap));

  g_nCount[szNum[0]] = 1;
  g_nMap[szNum[0]] = 1;

  int j = 0;
  for (int i = 0; i < nN; )
    {
      if (g_nMap[szNum[i]])
	{
	  nRes += nPow * LInt(g_nCount[szNum[i]]);

	  i++;
	  nPow /= LInt(nBase);
	}
      else
	{
	  g_nCount[szNum[i]] = j++;
	  g_nMap[szNum[i]] = 1;

	  if (j == 1)
	    j++;
	}
    }

  return nRes;
}

int main()
{
  freopen("o.txt", "w", stdout);

  char szNum[64];

  int nTC;
  cin >> nTC;
  for (int nC = 1; nC <= nTC; nC++)
    {
      cin >> szNum;

      printf("Case #%d: %lld\n", nC, Solve(szNum));
    }

  return 0;
}
