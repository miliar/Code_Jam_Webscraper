
#include <cstring>
#include <iostream>
#include <cstdio>

using namespace std;

static const int g_nSize = 128;

int g_nDP[g_nSize][g_nSize];
int g_nPos[g_nSize];

int Solve(int nI, int nJ)
{
  if (g_nDP[nI][nJ] > 0)
    return g_nDP[nI][nJ];

  if (nI + 1 == nJ)
    return 0;

  int nMin = -1;
  for (int k = nI + 1; k < nJ; k++)
    {
      int nTmp = Solve(nI, k) + Solve(k, nJ);
      if (nMin < 0 || nTmp < nMin)
	{
	  nMin = nTmp;
	}
    }

  return g_nDP[nI][nJ] = g_nPos[nJ] - g_nPos[nI] - 1 - 1 + nMin;
}

int main()
{
  freopen("o.txt", "w", stdout);

  int nTC;
  cin >> nTC;
  for (int nC = 1; nC <= nTC; nC++)
    {
      int nP, nQ;
      cin >> nP >> nQ;

      g_nPos[0] = 0;
      for (int i = 1; i <= nQ; i++)
	{
	  cin >> g_nPos[i];
	}
      g_nPos[nQ + 1] = nP + 1;

      memset(g_nDP, 0, sizeof(g_nDP));
      printf("Case #%d: %d\n", nC, Solve(0, nQ + 1));
    }

  return 0;
}
