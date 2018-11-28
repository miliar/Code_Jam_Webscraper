/* Google Code Jam 2010, Qualification Round, Problem A: "Snapper Chain". */
/* Fri. May. 7, 2010, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 7, 2010.
#include <cstdio>

int main (void) {
  int nc, ca, n, k;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    scanf ("%d%d", &n, &k);
    int mask = (1 << n) - 1;
    printf ("Case #%d: %s\n", ca, (mask & k) == mask ? "ON" : "OFF");
  }
  return 0;
}
