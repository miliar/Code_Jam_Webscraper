#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int X_OFFSET=2000000;
const int RT_BASE=(1<<20)*4;

int rmax[(1<<20)*4*2+8];
int rmin[(1<<20)*4*2+8];

void rt_put(int p, int v);
int rt_get(int p);
int rt_leftmost_two();
int rt_rightmost_zero(int p);
int rt_rightmost_zero_recurse(int n, int x1, int x2, int p);

int main() {
  int i, j, C, p, z, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    memset(rmax, 0, sizeof rmax);
    memset(rmin, 0, sizeof rmin);
    scanf("%d", &C);
    while (C--) {
      scanf("%d %d", &i, &j);
      rt_put(X_OFFSET+i, j);
    }
    i64 A=0;
    while (true) {
      p=rt_leftmost_two();
      if (p<0)
        break;
      z=rt_rightmost_zero(p-1);
      A+=p-z;
      rt_put(z, 1);
      rt_put(z+1, rt_get(z+1)-1);
      rt_put(p, rt_get(p)-1);
      rt_put(p+1, rt_get(p+1)+1);
    }
    PRINT("Case #%d: %lld\n", t, A);
  }
  return 0;
}

void rt_put(int p, int v) {
  int n=RT_BASE+p;
  rmax[n]=v;
  rmin[n]=v;
  do {
    n/=2;
    rmax[n]=max(rmax[n*2], rmax[n*2+1]);
    rmin[n]=min(rmin[n*2], rmin[n*2+1]);
  }
  while (n!=1);
}

int rt_get(int p) {
  return rmax[RT_BASE+p];
}

int rt_leftmost_two() {
  if (rmax[1]<2)
    return -1;
  int n=1, l=(1<<20)*4;
  while (l!=1) {
    if (rmax[n*2]>=2)
      n*=2;
    else {
      assert(rmax[n*2+1]>=2);
      n=2*n+1;
    }
    l/=2;
  }
  assert(n>=RT_BASE);
  return n-RT_BASE;
}

int rt_rightmost_zero(int p) {
  int x=rt_rightmost_zero_recurse(1, 0, RT_BASE-1, p);
  assert(x>=0);
  return x;
}

int rt_rightmost_zero_recurse(int n, int x1, int x2, int p) {
  if (x1==x2)
    return rmin[n]==0 ? x1 : -1;
  else {
    int xm=x1+(x2-x1+1)/2, x=(-1);
    if (xm<=p && rmin[n*2+1]==0)
      x=rt_rightmost_zero_recurse(n*2+1, xm, x2, p);
    if (x<0)
      x=rt_rightmost_zero_recurse(n*2, x1, xm-1, p);
    return x;
  }
}
