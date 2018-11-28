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

const int kMaxN = 2000000;

int a[kMaxN + 1], id[kMaxN + 1];
double l[kMaxN + 1];
int n, w, r, t, m;

int Sgn(double x) {
  if (abs(x) < 1e-9) return 0;
  return x < 0 ? -1 : 1;
}

bool Cmp(int x, int y) {
  return a[x] < a[y];
}

int main() {
  int T, b, e;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    printf("Case #%d: ", tt);
    scanf("%d%d%d%d%d", &n, &w, &r, &t, &m);
    l[m] = n; a[m] = 0; id[m] = m;
    for (int i = 0; i < m; ++i) {
      scanf("%d%d%d", &b, &e, a + i);
      l[i] = e - b;
      id[i] = i;
      l[m] -= l[i];
    }
    ++m;
    sort(id, id + m, Cmp);
    double tot = 0.0;
    for (int i = 0; i < m; ++i) {
      if (Sgn((r + a[id[i]]) * (t - tot) - l[id[i]]) >= 0) {
        tot += l[id[i]] / (double) (r + a[id[i]]);
      } else {
        l[id[i]] -= (t - tot) * (r + a[id[i]]);
        tot = t;
        for (int j = i; j < m; ++j) {
          tot += l[id[j]] / (double) (w + a[id[j]]);
        }
        break;
      }
    }
    printf("%lf\n", tot);
  }
  return 0;
}
