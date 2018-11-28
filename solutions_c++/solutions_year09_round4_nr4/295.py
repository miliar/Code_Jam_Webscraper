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

#define DEBUG(format, args...) do { fprintf(stderr, format, ## args); fflush(stderr); } while (0)
#define PRINT(format, args...) do { fprintf(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

struct Plant {
  int x, y, r;
};

Plant pl[64];

double GetDiameter(const Plant &p1, const Plant &p2);

int main() {
  int i, P, t, T;
  double A;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &P);
    for (i=0; i<P; i++)
      scanf("%d %d %d", &pl[i].x, &pl[i].y, &pl[i].r);
    if (P==1)
      A=pl[0].r;
    else if (P==2)
      A=max(pl[0].r, pl[1].r);
    else if (P==3) {
      A=1e26;
      A=min(A, max<double>(GetDiameter(pl[0], pl[1])/2, pl[2].r));
      A=min(A, max<double>(GetDiameter(pl[0], pl[2])/2, pl[1].r));
      A=min(A, max<double>(GetDiameter(pl[1], pl[2])/2, pl[0].r));
    }
    PRINT("Case #%d: %.8lf\n", t, A);
  }
  return 0;
}

double GetDiameter(const Plant &p1, const Plant &p2) {
  return hypot(p1.x-p2.x, p1.y-p2.y)+p1.r+p2.r;
}
