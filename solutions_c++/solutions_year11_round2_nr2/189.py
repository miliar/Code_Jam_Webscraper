#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

const int kMaxN = 200;

pair<int, int> a[kMaxN];
int n, d;

inline int Sign(double x) {
  if (fabs(x) < 1e-9) return 0;
  return x < 0 ? -1 : 1;
}

bool Check(double md) {
  double left = -1e20;
  for (int i = 0; i < n; ++i) {
    double p = a[i].first;
    for (int j = a[i].second - 1; j >= 0; --j) {
      double pos = max(left, p - md - d) + d;
      if (Sign(pos - p - md) > 0) return false;
      left = pos;
    }
  }
  return true;
}

int main() {
  int T, x, y;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d", &n, &d);
    for (int i = 0; i < n; ++i) {
      scanf("%d%d", &x, &y);
      a[i] = make_pair(x, y);
    }
    sort(a, a + n);
    long long l = 0, r = 100000000000000000LL;
    while (l < r) {
      long long m = (l + r) / 2;
      if (Check(m / 2.0)) r = m;
      else l = m + 1;
    }
    printf("Case #%d: %lf\n", t, l / 2.0);
  }
  return 0;
}
