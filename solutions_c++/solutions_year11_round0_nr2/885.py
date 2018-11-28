#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back

using namespace std;

char C[300][300];
bool P[300][300];
int N[300];
vector <char> res;
char str[300], c1, c2, c3;

int main()
{
  int t, cnt, i, c, n;
  char j, k;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    scanf("%d", &c);
    res.clear();
    memset(N,0,sizeof(N));
    memset(P,0,sizeof(P));
    memset(C,0,sizeof(C));
    for (i=0; i<c; i++)
    {
      scanf(" %c%c%c", &c1, &c2, &c3);
      C[(int)c1][(int)c2]=c3, C[(int)c2][(int)c1]=c3;
    }
    scanf("%d", &c);
    for (i=0; i<c; i++)
    {
      scanf(" %c%c", &c1, &c2);
      P[(int)c1][(int)c2]=1, P[(int)c2][(int)c1]=1;
    }
    scanf("%d %s", &n, &str);
    for (i=0; i<n; i++)
    {
      if (res.size()==0)
      {
        N[(int)str[i]]++;
        res.pb(str[i]);
        continue;
      }
      if (C[(int)res[res.size()-1]][(int)str[i]]!=0)
      {
        c1=C[(int)res[res.size()-1]][(int)str[i]];
        N[(int)res[res.size()-1]]--;
        res.pop_back();
        res.pb(c1);
        continue;
      }
      res.pb(str[i]);
      N[(int)str[i]]++;
      for (j='A'; j<='Z'; j++)
        for (k=j+1; k<='Z'; k++)
          if (N[(int)j]>0 && N[(int)k]>0 && P[(int)j][(int)k])
            while (res.size()>0)
            {
              N[(int)res[res.size()-1]]--;
              res.pop_back();
            }
    }
    printf("Case #%d: [", cnt);
    for (i=0; i<(int)res.size(); i++)
    {
      if (i>0)
        printf(", ");
      printf("%c", res[i]);
    }
    printf("]\n");
  }
  return 0;
}
