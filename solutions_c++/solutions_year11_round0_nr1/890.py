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
  int t, cnt, l, n, i, f, s, pf, ps;
  char c;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    scanf("%d", &n);
    f=s=0, pf=ps=1;
    for (i=0; i<n; i++)
    {
      scanf(" %c %d", &c, &l);
      if (c=='O')
        f=max(s+1,f+1+abs(pf-l)), pf=l;
      else
        s=max(f+1,s+1+abs(ps-l)), ps=l;
    }
    printf("Case #%d: %d\n", cnt, max(f,s));
  }
  return 0;
}
