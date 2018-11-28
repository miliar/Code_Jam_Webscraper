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

int E;
i64 ec[1000008];

int main() {
  int i, B, S, C, t, T;
  int dt[1008];
  i64 d, z, Z;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %lld %d %d", &B, &Z, &S, &C);
    for (i=0; i<C; i++)
      scanf("%d", &dt[i]);
    E=0;
    z=0;
    for (i=0; i<S; i++) {
      d=dt[i%C];
      if (z<Z) {
        if (z+2*d>Z) {
          d=(Z-z)/2;
          d=dt[i%C]-d;
          ec[E++]=d;
        }
      }
      else
        ec[E++]=d;
      d=dt[i%C];
      z+=2*d;
    }
    sort(ec, ec+E);
    for (i=E-1; i>=0 && B>0; i--, B--)
      z-=ec[i];
    PRINT("Case #%d: %lld\n", t, z);
  }
  return 0;
}
