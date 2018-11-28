#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;

/* PREWRITTEN CODE */

#define ALL(x) x.begin(),x.end()
#define PB push_back


#define FOR(i,p,k) for (int i=p; i<k; i++)
#define REP(i,n) for (int i=0; i<n; i++)
#define SIZE(x) (int)x.size()
/* COMPETITION CODE */

typedef long double ld;

typedef struct {
  ld x;
  ld y;
} pt;

pt operator+ (const pt &A, const pt &B) {
  pt R;
  R.x = A.x + B.x;
  R.y = A.y + B.y;
  return R;
}

pt operator- (const pt &A, const pt &B) {
  pt R;
  R.x = A.x - B.x;
  R.y = A.y - B.y;
  return R;
}

pt operator* (ld x, const pt &B) {
  pt R;
  R.x = x * B.x;
  R.y = x * B.y;
  return R;
}

ld is (const pt &A, const pt &B) {
  return A.x * B.x + A.y * B.y;
}

ld dist (const pt &A, const pt &B) {
  return sqrtl(is(A-B,A-B));
}

int main () {
  int number_of_tests;
  scanf("%d", &number_of_tests);
  REP (test_number, number_of_tests) {
    printf("Case #%d: ", test_number+1);
    int N;
    scanf("%d", &N);
    pt pts[3];
    int rds[3];
    REP (i, N) {
      scanf("%Lf %Lf %d", &pts[i].x, &pts[i].y, &rds[i]);
    }
    if (N == 1) printf("%Lf\n", (ld) rds[0]);
    if (N == 2) printf("%Lf\n", (ld) (max(rds[0], rds[1])));
    if (N == 3) {
      ld best = 324234234.2;
      REP (i, 3) {
        ld cur = max ((ld) rds[i], (dist(pts[(i+1)%3], pts[(i+2)%3]) + (ld) (rds[(i+1)%3] + rds[(i+2)%3])) / 2.0);
        if (cur < best) best = cur;
      }
      printf("%Lf\n", best);
    }
  }
  return 0;
}

