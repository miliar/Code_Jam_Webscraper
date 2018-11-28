
#include <cstring>
#include <set>
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

static const int g_nBS = 1000000;
char g_szBuf[g_nBS];
char g_szTmp[256];

int main()
{
  freopen("o.txt", "w", stdout);

  int nTC;
  cin >> nTC;

  set<string> sAtt;

  for (int nC = 1; nC <= nTC; nC++)
    {
      int nL;
      cin >> nL;
      getchar();

      int i = 0;
      for (; nL--; )
	{
	  gets(g_szTmp);
	  strcpy(g_szBuf + i, g_szTmp);

	  i = strlen(g_szBuf);
	}

      //cout << g_szBuf << endl;

      printf("Case #%d:\n", nC);

      cin >> nL;
      for (; nL--; )
	{
	  cin >> g_szTmp;
	  int nA;
	  cin >> nA;

	  sAtt.clear();
	  for (; nA--; )
	    {
	      string sA;
	      cin >> sA;

	      sAtt.insert(sA);
	    }

	  double dRes = 1.0;

	  for (i = 0; ; )
	    {
	      for (; g_szBuf[i] != '('; i++);
	      for(; ; i++)
		{
		  if ((g_szBuf[i] >= '0' && g_szBuf[i] <= '9') || 
		      g_szBuf[i] == '.')
		    break;
		}

	      double dP;
	      sscanf(g_szBuf + i, "%lf", &dP);

	      dRes *= dP;

	      for (; ; i++)
		if (g_szBuf[i] >= 'a' && g_szBuf[i] <= 'z' ||
		    g_szBuf[i] == ')')
		  break;

	      if (g_szBuf[i] == ')')
		break;

	      char szA[16];
	      memset(szA, 0, sizeof(szA));
	      sscanf(g_szBuf + i, "%s", szA);
	      string sA(szA);

	      if (sAtt.find(sA) == sAtt.end())
		{
		  for (; g_szBuf[i] != '('; i++);
		  i++;

		  for (int nSt = 1; nSt > 0; i++)
		    {
		      if (g_szBuf[i] == '(')
			nSt++;
		      else if (g_szBuf[i] == ')')
			nSt--;
		    }
		}

	      /*
	      if (sAtt.find(sA) != sAtt.end())
		{
		  continue;
		}
	      else
		{

		}
	      */
	    }

	  printf("%.7f\n", dRes);
	}
    }

  return 0;
}
