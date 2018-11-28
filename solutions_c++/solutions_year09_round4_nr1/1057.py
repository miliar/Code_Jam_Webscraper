
#include <iostream>
#include <cstdio>

using namespace std;

static const int g_nN = 64;

char szMatrix[g_nN][g_nN];
int nVal[g_nN];
int nIdx[g_nN];

int Solve(int nN)
{
  for (int i = 0; i < nN; i++)
    {
      nVal[i] = 0;
      for (int j = nN - 1; j >= 0; j--)
	{
	  if (szMatrix[i][j] != '0')
	    {
	      nVal[i] = j;
	      break;
	    }
	}
      nIdx[i] = i;
    }

  int nRes = 0;
  for (int i = 0; i < nN; i++)
    {
      if (nVal[i] <= i)
	continue;

      int j;
      for (j = 1; ; j++)
	{
	  if (nVal[i + j] <= i)
	    break;
	}

      nRes += j;

      for (int k = j; k > 0; k--)
	nVal[i + k] = nVal[i + k - 1];
    }

  return nRes;
}

int main()
{
  freopen("o.txt", "w", stdout);

  int nTC;
  cin >> nTC;
  for (int nC = 1; nC <= nTC; nC++)
    {
      int nN;
      cin >> nN;

      for (int i = 0; i < nN; i++)
	cin >> szMatrix[i];

      printf("Case #%d: %d\n", nC, Solve(nN));
    }

  return 0;
}
