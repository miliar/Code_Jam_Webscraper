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

int d, n, D[11000], L[11000], M[11000];

int main()
{
  int tst, cnt, i, j;
  bool fl;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<cnt<<endl;
    scanf("%d", &n);
    memset(M,0,sizeof(M)), fl=0;
    for (i=0; i<n; i++)
      scanf("%d%d", &D[i], &L[i]);
    scanf("%d", &d), M[0]=D[0];
    for (i=0; i<n; i++)
    {
      if (D[i]+M[i]>=d)
      {
        fl=1;
        break;
      }
      for (j=i+1; D[j]<=D[i]+M[i] && j<n; j++)
        M[j]=max(M[j],min(L[j],D[j]-D[i]));
    }
    (fl)?(printf("Case #%d: YES\n", cnt)):(printf("Case #%d: NO\n", cnt));
  }
  return 0;
}
