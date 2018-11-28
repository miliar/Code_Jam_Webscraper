#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
#include <complex>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, (n))
#define point complex<double>
int n;

point  p[100];
double radius[100];

double cal(int i, int j) {
  double ret = max(radius[i], radius[j]);
  return max(ret, (abs(p[i] - p[j]) + radius[i] + radius[j]) / 2.);
}

int main() {
  int N;
  double x, y;
  cin >> N;
  for (int C = 1; C <= N; ++C) {
    cin >> n;
    REP(i, n) {
      cin >> x >> y >> radius[i];
      p[i] = point(x, y);
    }

    double ans = 0;
    if (n == 1) {
      ans = radius[0];
    } if (n == 2) {
      ans = max(radius[0], radius[1]);
    } if (n == 3) {
      ans = max(cal(0, 1), radius[2]);
      ans = min(ans, max(cal(1, 2), radius[0]));
      ans = min(ans, max(cal(2, 0), radius[1]));
    }

    printf("Case #%d: %lf\n", C, ans);
  }
}
