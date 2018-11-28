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
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;

int A[21000000];
int P[210], S[210];

int check (int d, long long m)
{
  int l=0, r=m+1, c;
  while (r-l>1)
  {
    c=(l+r)/2;
    (m>=(A[max(c/d-1,0)]*1ll*(d-(c%d)))+(A[c/d]*1ll*(c%d)))?(l=c):(r=c);
  }
  return l;
}

int main()
{
  int m, tst, cnt, res, i, j, f, n;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<cnt<<endl;
    scanf("%d%d%d", &m, &f, &n);
    for (i=0; i<n; i++)
      scanf("%d%d", &P[i], &S[i]);
    for (i=0; i<m; i++) 
      for (A[i]=inf, j=0; j<n; j++)
        if (S[j]>=i)
          A[i]=min(A[i],P[j]);
    for (i=1; i<m; i++)
      A[i]=min(inf,A[i]+A[i-1]);
    for (res=0, i=1; i*f<m; i++)
      res=max(res,check(i,m-i*f));// cerr<<i<<" "<<res<<endl;
    printf("Case #%d: %d\n", cnt, res); 
  }
  return 0;
}
