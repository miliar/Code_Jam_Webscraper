/* Google Code Jam 2011, Qualification Round, Problem A: "Bot Trust". */
/* Fri. May. 6, 2010, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 6, 2010.
#include <cstdio>
#include <cstdlib>

int main (void) {
  int nc, ca;
  char r[2];
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    int n, x[2] = {1, 1}, t[2] = {0}, newX, prevT = -1;
    scanf ("%d", &n);
    for (int i = 0; i < n; ++ i) {
      scanf ("%1s%d", r, &newX);
      int idx = (*r == 'O') ? 0 : 1;
      t[idx] += abs (newX - x[idx]);  // Walk there.
      if (t[idx] < prevT) t[idx] = prevT;  // Wait for other robot (nop if self).
      ++ t[idx];  // Press button.
      x[idx] = newX;
      prevT = t[idx];
    }
    printf ("Case #%d: %d\n", ca, t[0] > t[1] ? t[0] : t[1]);
  }
  return 0;
}
