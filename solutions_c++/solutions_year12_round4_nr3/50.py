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

int A[2100], n, Res[2100], P[2100], m, C[2100], D[2100];

int main()
{
  int tst, cnt, i, j;
  bool fl;
  freopen("in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &tst);
  srand(time(NULL));
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<"                 "<<cnt<<endl;
    scanf("%d", &n), fl=0;
    for (i=0; i<n-1; i++)
      scanf("%d", &A[i]), A[i]--;
    for (i=0; i<n-1; i++)
      for (j=i+1; j<A[i]; j++)
        if (A[j]>A[i])
          fl=1;
    if (fl)
    {
      printf("Case #%d: Impossible\n", cnt);
      continue;
    }
    memset(C,0,sizeof(C)), memset(D,0,sizeof(D)), m=0, Res[n-1]=0;
    for (i=0; i<n-1; i++)
      P[i]=D[A[i]], D[A[i]]++;
    for (i=n-2; i>=0; m=min(Res[i],m), i--)
      C[i]=C[A[i]]+P[i], Res[i]=Res[A[i]]-(A[i]-i)*C[i];
    printf("Case #%d:", cnt);
    for (i=0; i<n; i++)
      printf(" %d", Res[i]-m), assert(Res[i]>=m && Res[i]<=m+inf);
    printf("\n");
  }
  return 0;
}
