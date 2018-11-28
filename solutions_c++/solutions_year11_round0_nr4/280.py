#include <cstdio>

typedef long double dbl;

int a[1010], was[1010];

dbl f[1010], c[1010][1010];

int main (void) {
  int tn;
  scanf ("%d", &tn);

  c[1][1] = 1;
  for (int i = 1; i < 1002; i++) {
    for (int k = 1; k <= i; k++) {
      c[i + 1][k] += c[i][k] * (i + 1 - k) / (i + 1); 
      c[i + 1][k + 1] += c[i][k] * k / (i + 1); 
    }
  }

  for (int i = 2; i <= 1002; i++) {
    for (int k = 1; k < i; k++) {
      dbl v = c[i][k];
      v *= f[i - k] + (k != 1) + f[k];
      f[i] += v;
    }
    f[i] += c[i][i];
    f[i] /= (1 - c[i][i]);
  }

  for (int tt = 1; tt <= tn; tt++) {
    int n;
    scanf ("%d", &n);

    for (int i = 1; i <= n; i++) {
      scanf ("%d", &a[i]);
      was[i] = 0;
    }

    double res = 0;

    for (int i = 1; i <= n; i++) {
      if (!was[i]) {
        int v = 0;
        while (!was[i]) {
          was[i] = 1;
          i = a[i];
          v++;
        }

        if (v > 1) {
          res += 1 + f[v];
        }
      }
    }
    printf ("Case #%d: %.6lf\n", tt, res);
  }

  return 0;
}