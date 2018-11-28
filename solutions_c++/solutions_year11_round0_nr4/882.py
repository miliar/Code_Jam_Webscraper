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

int A[1100], n, B[1100], res;
map <int,int> C;

int main()
{
  int t, cnt, i;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    scanf("%d", &n);
    for (i=0; i<n; i++)
      scanf("%d", &A[i]), B[i]=A[i];
    sort(B,B+n);
    C.clear();
    for (i=0; i<n; i++)
      C[B[i]]=i;
    res=n;
    for (i=0; i<n; i++)
      if (i==C[A[i]])
        res--;
    printf("Case #%d: %d\n", cnt, res);
  }
  return 0;
}
