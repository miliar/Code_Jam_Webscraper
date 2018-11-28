#include <cstdio>
#include <cassert>

const long long maxN = 1000000;
const long long inf = (long long)1e16;

long long n, d;
long long x[maxN], c[maxN];

int main() {
  long long nt;
  assert(scanf("%lld", &nt) == 1);
  for (long long tt = 1; tt <= nt; tt++) {
    printf("Case #%lld: ", tt);

    assert(scanf("%lld%lld", &n, &d) == 2);
    d *= 2;
    for (long long i = 0; i < n; i++) {
      assert(scanf("%lld%lld", &x[i], &c[i]));
      x[i] *= 2;
    }
    long long mi = 0, ma = inf;
    while (mi < ma) {
      long long a = (mi + ma) / 2;
      bool ok = true;
      long long left = -inf;
      for (long long i = 0; i < n; i++) {
        for (long long j = 0; j < c[i]; j++) {
          long long t = left;
          if (x[i] - a > t) {
            t = x[i] - a;
          }
          if (t > x[i] + a) {
            ok = false;
            break;
          }
          left = t + d;
        }
      }
      if (ok) {
        ma = a;
      } else {
        mi = a + 1;
      }
    }
    printf("%.1lf\n", mi * 0.5);
  }
  return 0;
}
