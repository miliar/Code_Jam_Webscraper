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

char gd[512][512];
i64 sh[512][512];
i64 sv[512][512];

int main() {
  int Y, X, y, x, yi, xi, k, A, t, T;
  i64 W, dx, dy;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    A=0;
    scanf("%d %d %lld", &Y, &X, &W);
    for (y=1; y<=Y; y++)
      scanf("%s", &gd[y][1]);
    for (y=1; y<=Y; y++)
      for (x=1; x<=X; x++)
        for (k=1; true; k++) {
          dx=0;
          dy=0;
          if (y-k<1 || x-k<1)
            break;
          if (y+k>Y || x+k>X)
            break;
          for (yi=y-k; yi<=y+k; yi++)
            for (xi=x-k; xi<=x+k; xi++) {
              if (yi==y-k && xi==x-k ||
                  yi==y-k && xi==x+k ||
                  yi==y+k && xi==x-k ||
                  yi==y+k && xi==x+k)
                continue;
              dx+=(xi-x)*(W+(gd[yi][xi]-'0'));
              dy+=(yi-y)*(W+(gd[yi][xi]-'0'));
            }
          if (dx==0 && dy==0)
            A=max(A, 2*k+1);
        }
    for (y=1; y<=Y; y++)
      for (x=1; x<=X; x++)
        for (k=1; true; k++) {
          dx=0;
          dy=0;
          if (y-(k-1)<1 || x-(k-1)<1)
            break;
          if (y+k>Y || x+k>X)
            break;
          for (yi=y-(k-1); yi<=y+k; yi++)
            for (xi=x-(k-1); xi<=x+k; xi++) {
              if (yi==y-(k-1) && xi==x-(k-1) ||
                  yi==y-(k-1) && xi==x+k ||
                  yi==y+k && xi==x-(k-1) ||
                  yi==y+k && xi==x+k)
                continue;
              dx+=(2*xi-2*x-1)*(W+(gd[yi][xi]-'0'));
              dy+=(2*yi-2*y-1)*(W+(gd[yi][xi]-'0'));
            }
          if (dx==0 && dy==0)
            A=max(A, 2*k);
        }
    if (A<=2)
      PRINT("Case #%d: IMPOSSIBLE\n", t);
    else
      PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}
