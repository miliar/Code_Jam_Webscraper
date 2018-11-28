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

int A[1200], P[1200], L[1200];

bool cmp (int a, int b)
{
  if (L[a]*P[b]!=L[b]*P[a])
    return L[a]*P[b]<L[b]*P[a];
  return a<b;
}

int main()
{
  int tst, cnt, n, i;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    scanf("%d", &n);
    for (i=0; i<n; i++)
      A[i]=i, scanf("%d", &L[i]);
    for (i=0; i<n; i++)
      scanf("%d", &P[i]);
    sort(A,A+n,cmp);
    printf("Case #%d:", cnt);
    for (i=0; i<n; i++)
      printf(" %d", A[i]);
    printf("\n");  
  }
  return 0;
}
