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

const int INF=1000000008;

int ms[1024];
int mz[1024][1024][11];
int ct[11][1024];

int recurse(int lo, int hi, int m, int y, int x);

int main() {
  int i, j, R, P, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &R);
    P=(1<<R);
    for (i=0; i<P; i++)
      scanf("%d", ms+i);
    for (i=1; i<=R; i++)
      for (j=0; j<(1<<(R-i)); j++)
        scanf("%d", &ct[i][j]);
    memset(mz, -1, sizeof mz);
    PRINT("Case #%d: %d\n", t, recurse(0, P-1, R, R, 0));
  }
  return 0;
}

int recurse(int lo, int hi, int m, int y, int x) {
  int &A=mz[lo][hi][m];
  if (A<0)
    if (lo==hi)
      A=(m<=ms[lo] ? 0 : INF);
    else {
      int t=(hi-lo+1)/2;
      A=ct[y][x]+recurse(lo, lo+t-1, m-1, y-1, 2*x)+recurse(lo+t, hi, m-1, y-1, 2*x+1);
      A=min(A, 0+recurse(lo, lo+t-1, m  , y-1, 2*x)+recurse(lo+t, hi, m  , y-1, 2*x+1));
      A=min(A, INF);
    }
  return A;
}
