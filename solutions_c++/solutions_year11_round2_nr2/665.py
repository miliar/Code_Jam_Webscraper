/* Google Code Jam 2011, Round 1B, Problem B: "Revenge of the Hot Dogs". */
/* Sat. May. 21, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Sat. May. 21, 2011.
#include <cstdio>

int n;
long long x[1048576];
long long dest[1048576];

inline long long max (long long a, long long b) {
  return (a > b) ? a : b;
}

// Assume first vendor is stationary, and every other vender moves rightward at speed in [0, 2].
int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    int c;
    long long d;
    n = 0;
    scanf ("%d%lld", &c, &d);
    for (int i = 0; i < c; ++ i) {
      long long p;
      int v;
      scanf ("%lld%d", &p, &v);
      for (int j = 0; j < v; ++ j) x[n ++] = p;
    }
    long long x0 = x[0];
    for (int i = 0; i < n; ++ i) x[i] -= x0;
    dest[0] = 0;
    long long sol = 0;
    for (int i = 1; i < n; ++ i) {
      dest[i] = max (x[i], dest [i - 1] + d);
      int delta = dest[i] - x[i];
      //printf ("%lld => %lld\n", x[i], dest[i]);
      if (sol < delta) sol = delta;
    }
    printf ("Case #%d: %.1f\n", ca, sol * 0.5);
  }
  return 0;
}
