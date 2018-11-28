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

int A[22000], B[22000], C[22000];

bool solve (int l)
{
  int j;
  memcpy(B,A,sizeof(A));
  memset(C,0,sizeof(C));
  for (int b=0; b<11000; b++)
    if (B[b]!=0)
    {
      if (C[b]!=0)
      {
        C[b]--, C[b+1]++, B[b]--, b--;
        continue;
      }
      for (j=0; j<l; j++)
      {
        if (B[b+j]==0)
          return 0;
        B[b+j]--;
      }
      C[b+l]++, b--;
    }
  return 1;
}

int main()
{
  int t, cnt, n, i, tmp, l, r;
  freopen("in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    cerr<<"test #"<<cnt<<endl;
    scanf("%d", &n);
    if (n==0)
    {
      printf("Case #%d: 0\n", cnt);
      continue;
    }
    memset(A,0,sizeof(A));
    for (i=0; i<n; i++)
      scanf("%d", &tmp), A[tmp]++;
    l=1, r=11000;
    while (r-l>1)
    {
      if (solve((l+r)/2))
        l=(l+r)/2;
      else
        r=(l+r)/2;
    }
    printf("Case #%d: %d\n", cnt, l);
  }
  return 0;
}
