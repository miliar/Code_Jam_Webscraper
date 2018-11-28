#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) { fprintf(stderr, format, ## args); fflush(stderr); }
#define PRINT(format, args...) { fprintf(stdout, format, ## args); DEBUG(format, ## args); }

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

int main() {
  int t, T;
  int X, Y, dx1, dy1, dx2, dy2, A, f;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    f=0;
    scanf("%d %d %d", &X, &Y, &A);
    if (X*Y<A)
      goto QUIT;
    for (dx1=(-X); dx1<=0; dx1++)
      for (dy1=0; dy1<=Y; dy1++)
        if (dx1-dy1!=0 && A%__gcd(-dx1, dy1)==0)
          for (dy2=0; dy2<=Y; dy2++) {
            if (dy1==0)
              for (dx2=dx1; dx2-dx1<=X; dx2++)
                if (abs(dx1*dy2-dx2*dy1)==A) {
                  f=1;
                  PRINT("Case #%d: %d %d %d %d %d %d\n",
                      t, -dx1, 0, 0, dy1, -dx1+dx2, dy2);
                  goto QUIT;
                }
            if (dy1!=0 && (A-dx1*dy2)%dy1==0) {
              dx2=(A-dx1*dy2)/-dy1;
              if (dx1<=dx2 && dx2-dx1<=X) {
                f=1;
                PRINT("Case #%d: %d %d %d %d %d %d\n",
                    t, -dx1, 0, 0, dy1, -dx1+dx2, dy2);
                goto QUIT;
              }
            }
            if (dy1!=0 && (-A-dx1*dy2)%dy1==0) {
              dx2=(-A-dx1*dy2)/-dy1;
              if (dx1<=dx2 && dx2-dx1<=X) {
                f=1;
                PRINT("Case #%d: %d %d %d %d %d %d\n",
                    t, -dx1, 0, 0, dy1, -dx1+dx2, dy2);
                goto QUIT;
              }
            }
          }
QUIT:
    if (!f)
      PRINT("Case #%d: IMPOSSIBLE\n", t);
  }
  return 0;
}
