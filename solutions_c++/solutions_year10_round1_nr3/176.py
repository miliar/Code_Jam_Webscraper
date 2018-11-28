/* Google Code Jam 2010, Round 1A, Problem C: "Number Game". */
/* Fri. May. 21, 2010, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 21, 2010.
#include <cstdio>
#include <cmath>

double phi = (sqrt (5) + 1) / 2;


int main (void) {
  int nc, ca, i, j;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    int a1, a2, b1, b2, res = 0;
    scanf ("%d%d%d%d", &a1, &a2, &b1, &b2);
    for (i = a1; i <= a2; i ++) for (j = b1; j <= b2; j ++) {
      if ((i == 0) || (j == 0) || (i >= phi * j) || (j >= phi * i)) res ++;
    }
    printf ("Case #%d: %d\n", ca, res); 
  }
  return 0;
}
