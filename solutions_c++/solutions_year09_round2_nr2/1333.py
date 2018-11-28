
#include <cstring>
#include <cstdio>

static const int g_nBase = 10;
static const int g_nRange = 1000;

int g_nFlag[12][g_nRange];
bool g_bAFlag[g_nRange]; 
int g_nASet[g_nRange];
int g_nASC;

int Next(int nN, int nB)
{
  int nRes = 0;

  for (; nN > 0; nN /= nB)
    {
      int nTmp = nN % nB;
      nRes += nTmp * nTmp;
    }

  return nRes;
}

int MakeBase()
{
  for (int i = 2; i <= g_nBase; i++)
    {
      memset(g_nFlag[i], 0, sizeof(g_nFlag[i]));
      g_nFlag[i][1] = 1;

      for (int j = 2; j < g_nRange; j++)
	{
	  memset(g_bAFlag, 0, sizeof(g_bAFlag));
	  g_nASC = 0;

	  bool bHappy = false;
	  for (int k = j; ; k = Next(k, i))
	    {
	      if (g_bAFlag[k])
		break;
	      g_bAFlag[k] = true;
	      g_nASet[g_nASC++] = k;

	      if (g_nFlag[i][k] > 0)
		bHappy = true;

	      if (g_nFlag[i][k] != 0)
		break;
	    }

	  for (int k = 0; k < g_nASC; k++)
	    g_nFlag[i][g_nASet[k]] = (bHappy) ? 1 : -1;
	}
    }

  return 0;
}

bool IsHappy(int nN, int nB)
{
  for (; nN >= g_nRange; nN = Next(nN, nB));

  return (g_nFlag[nB][nN] > 0) ? true : false;
}

int main()
{
  freopen("o.txt", "w", stdout);

  MakeBase();

  int nTC;
  scanf("%d", &nTC); 
  getchar();

  char szBuf[64];
  char szTmp[8];

  int nBase[g_nBase + 1];
  int nBC;

  for (int nC = 1; nC <= nTC; nC++)
    {
      memset(szBuf, 0, sizeof(szBuf));
      gets(szBuf);

      nBC = 0;
      for (int i = 0; sscanf(szBuf + i, "%s", szTmp) != EOF; i += strlen(szTmp) + 1)
	{
	  sscanf(szTmp, "%d", &nBase[nBC++]);
	}

      int i = 2;
      for (; ; i++)
	{
	  int j = 0;
	  for (; j < nBC; j++)
	    {
	      if (!IsHappy(i, nBase[j]))
		break;
	    }

	  if (j >= nBC)
	    break;
	}

      printf("Case #%d: %d\n", nC, i);
    }

  return 0;
}
