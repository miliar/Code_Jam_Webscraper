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

int main()
{
  int t, cnt, n, i, m, st, sf, tmp;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    scanf("%d", &n);
    st=sf=0, m=inf;
    for (i=0; i<n; i++)
    {
      scanf("%d", &tmp);
      m=min(m,tmp), st+=tmp, sf^=tmp;
    }
    printf("Case #%d: ", cnt);
    if (sf!=0)
      printf("NO\n");
    else
      printf("%d\n", st-m); 
  }
  return 0;
}
