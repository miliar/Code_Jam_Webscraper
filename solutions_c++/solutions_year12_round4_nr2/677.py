#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define LET(name, value) __typeof(value) name = value
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for (int i = (a); i < (int)(b); ++i)
#define FOREQ(i, a, b) for (int i = (a); i <= (int)(b); ++i)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for (LET(i, (c).begin()); i != (c).end(); ++i)

const double EPS = 1e-8;

int main() {
  int T; scanf("%d", &T);
  for (int testcase = 1; testcase <= T; ++testcase) {
    int N;
    double W, H;
    scanf("%d%lf%lf", &N, &W, &H);
    vector<double> r(N);
    REP(i, N) { scanf("%lf", &r[i]); }
    vector<double> x(N), y(N);
    for (;;) {
      REP(i, N) {
        x[i] = double(rand()) / RAND_MAX * W;
        y[i] = double(rand()) / RAND_MAX * H;
      }
      bool ok = true;
      REP(i, N) {
        FOR(j, i+1, N) {
          double dy = y[i] - y[j];
          double dx = x[i] - x[j];
          double d = dy*dy + dx*dx;
          if (d-(r[i]+r[j])*(r[i]+r[j]) < -EPS) {
            ok = false;
            break;
          }
        }
      }
      if (ok) {
        printf("Case #%d:", testcase);
        REP(k, N) {
          printf(" %f %f", x[k], y[k]);
        }
        puts("");
        break;
      }
    }
  }
}
