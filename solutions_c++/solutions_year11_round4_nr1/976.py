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

double W, R;

struct Walkway {
  int b, e, s;
  bool operator<(const Walkway &wk) const { return 1./(s+W)-1./(s+R)>1./(wk.s+W)-1./(wk.s+R); }
};

Walkway wk[1008];

int main() {
  int i, N, t, T;
  double b, e, d, s, A, D, z, Z;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    A=0;
    scanf("%lf %lf %lf %lf %d", &D, &W, &R, &Z, &N);
    for (i=0; i<N+1; i++) {
      if (i<N)
        scanf("%lf %lf %lf", &b, &e, &s);
      else {
        b=0;
        e=D;
        s=0;
      }
      wk[i].b=b;
      wk[i].e=e;
      wk[i].s=s;
      D-=e-b;
    }
    N++;
    sort(wk, wk+N);
    for (i=0; i<N; i++) {
      b=wk[i].b;
      e=wk[i].e;
      s=wk[i].s;
      d=(s+R)*Z;
      if (d>e-b) {
        z=(e-b)/(s+R);
        Z-=z;
        A+=z;
      }
      else {
        d=(s+R)*Z;
        A+=Z;
        Z-=Z;
        z=(e-b-d)/(s+W);
        A+=z;
      }
    }
    PRINT("Case #%d: %.9lf\n", t, A);
  }
  return 0;
}
