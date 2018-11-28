/* Google Code Jam 2010, Round 2, Problem C: "Bacteria". */
/* Sat. Jun. 5, 2010, By: Sparrow. */
// Last update: Sat. Jun. 5, 2010.
#include <cstdio>

int gr [128][128];

//   0
// 1 2
int lut [8] = {0, 0, 0, 1, 0, 1, 1, 1};

void out (int size) {
  for (int i = 0; i <= size; i ++) {
    for (int j = 0; j <= size; j ++) printf ("%d", gr [i][j]);
    printf ("\n");
  }
}

int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    int res = 0, nr, i, j;
    int size = 101;
    scanf ("%d", &nr);
    while (nr --) {
      int x1, y1, x2, y2;
      scanf ("%d%d%d%d", &x1, &y1, &x2, &y2);
      for (i = y1; i <= y2; i ++) {
        for (j = x1; j <= x2; j ++) gr [i][j] = 1;
      }
    }
    int popu = 0;
    for (i = 0; i < size; i ++) for (j = 0; j < size; j ++) popu += gr [i][j];
    for (res = 0; popu > 0; res ++) {
      for (i = size; i > 0; i --) {
        for (j = size; j > 0; j --) {
          int newGr = lut [(gr [i - 1][j]) | (gr [i][j - 1] << 1) | (gr [i][j] << 2)];
          popu += newGr - gr [i][j];
          gr [i][j] = newGr;
        }
      }
    }
    printf ("Case #%d: %d\n", ca, res);
  }
  return 0;
}
