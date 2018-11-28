/* Google Code Jam 2011, Qualification Round, Problem C: "Candy Splitting". */
/* Fri. May. 6, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 6, 2011.
#include <cstdio>
#include <cstdlib>

int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    int n, c, minC = 0x3FFFFFFF, xorC = 0, sumC = 0;
    scanf ("%d", &n);
    for (int i = 0; i < n; ++ i) {
      scanf ("%d", &c);
      if (minC > c) minC = c;
      xorC ^= c;
      sumC += c;
    }
    if (xorC != 0) printf ("Case #%d: NO\n", ca);
    else printf ("Case #%d: %d\n", ca, sumC - minC);
  }
  return 0;
}
