#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <numeric>
#include <cstring>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <complex>
#include <cassert>
using namespace std;
#define rep(i,s,e) for(int i=(s),___e=(e);i<___e;++i)
#define REP(i,n) rep(i,0,n)
#define ITER(c) __typeof((c).begin())
#define FOR(i,c) for(ITER(c) i=(c).begin(),___e=(c).end();i!=___e;++i)
#define ALL(c) (c).begin(), (c).end()
#define CLEAR(v) memset(v, 0, sizeof(v))
typedef unsigned int ui;
typedef long long ll;
const double PI = atan(1.0) * 4.0;
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) return ~0; } return c; }
int in() {
  int x = 0, c;
  while ((ui)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) return ~0; }
  do { x = 10 * x + (c - '0'); } while ((ui)((c = getchar()) - '0') < 10);
  return x;
}
typedef long double ld;
typedef complex<ld> P;
#define x real()
#define y imag()

const ld EPS = 1e-7;
ld AreaCC(P c1, ld r1, P c2, ld r2) {
  ld d = abs(c1 - c2);
  if(r1 + r2 < d + EPS) return 0;
  if(d < abs(r1 - r2) + EPS) {
    ld r = min(r1, r2);
    return r * r * PI;
  }
  ld xx = (d * d + r1 * r1 - r2 * r2) / (2 * d);
  ld t1 = acos(xx / r1);
  ld t2 = acos((d - xx) / r2);
  return r1 * r1 * t1 + r2 * r2 * t2 - d * r1 * sin(t1);
}
P ps[2], qs[10];
ld ans[10];
int main() {
//  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  REP(turn, T) {
    int N, M;
    cin >> N >> M;
    REP(i, N) cin >> ps[i].x >> ps[i].y;
    REP(i, M) cin >> qs[i].x >> qs[i].y;
    REP(i, M) {
      P q = qs[i];
      P a = ps[0], b= ps[1];
      ld la = abs(a - q), lb = abs(b - q);
      // |x - a| = la, |x - b| = lb
      ans[i] = AreaCC(a, la, b, lb);
    }
    printf("Case #%d:", turn + 1);
    REP(i, M) printf(" %.7Lf", ans[i]);
    puts("");
//    cerr << N << ' ' << M << endl;
  }
  return 0;
}

