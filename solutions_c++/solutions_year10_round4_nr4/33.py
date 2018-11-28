#include <stdio.h>
#include <stdlib.h>
#include <math.h>

  long double min (long double x1, long double x2) {
    return x1 < x2 ? x1 : x2;
  }

  int main () {
    int t;
    scanf ("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
      int n, m;
      scanf ("%d %d", &n, &m);

      long long x0, y0, x1, y1;
      scanf ("%I64d %I64d %I64d %I64d", &x0, &y0, &x1, &y1);

      printf ("Case #%d:", tt);

      for (int j = 0; j < m; j++) {
        long long xq, yq;
        scanf ("%I64d %I64d", &xq, &yq);

        long long R1 = (xq - x0) * (xq - x0) + (yq - y0) * (yq - y0);
        long long R2 = (xq - x1) * (xq - x1) + (yq - y1) * (yq - y1);

        long double r1 = sqrtl (R1);
        long double r2 = sqrtl (R2);

        long long D = (x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1);

        long double d = sqrtl (D);

        long double tmp;

        if (d >= r1 + r2 || R1 == 0 || R2 == 0) {
          tmp = 0;
        } else
        if (d <= fabsl (r1 - r2)) {
          tmp = min (R1, R2) * M_PI;
        } else {
          tmp = R1 * acosl ((D + R1 - R2) / (2 * d * r1)) +
                R2 * acosl ((D + R2 - R1) / (2 * d * r2)) -
                0.5 * sqrtl ( (r1 + r2 - d) * (d + r1 - r2) * (d + r2 - r1) * (d + r2 + r1));
        }

        printf (" %.10lf", (double)tmp);
      }

      puts ("");
    };
};