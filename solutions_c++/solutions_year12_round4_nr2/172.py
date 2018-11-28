#include <math.h>
#include <stdio.h>
#include <stdlib.h>

const int MAXN = 10000;

double r[MAXN];
double x[MAXN], y[MAXN];

int n, w, l;

inline double sqr(double x) { return x * x; }

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d%d%d", &n, &w, &l);
    for (int i = 0; i < n; ++i) scanf("%lf", &r[i]);
    while (true) {
      for (int i = 0; i < n; ++i) {
        x[i] = rand() / (double) RAND_MAX * w;
        y[i] = rand() / (double) RAND_MAX * l;
      }
      bool found = false;
      for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
          if (sqrt(sqr(x[j] - x[i]) + sqr(y[j] - y[i])) < r[i] + r[j] - 1e-9) {
            found = true;
            break;
          }
        }
        if (found) break;
      }
      if (!found) {
        printf("Case #%d:", tt);
        for (int i = 0; i < n; ++i) printf(" %lf %lf", x[i], y[i]);
        puts("");
        break;
      }
    }
  }
  return 0;
}
