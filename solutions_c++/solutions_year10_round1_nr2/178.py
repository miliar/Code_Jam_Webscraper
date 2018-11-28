/* Google Code Jam 2010, Round 1A, Problem B: "Make it Smooth". */
/* Fri. May. 21, 2010, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 21, 2010.
#include <cstdio>
#define INF 0x3FFFFFFF

int dp [2][256];

inline int myabs (int a) {return (a < 0) ? -a : a;}
inline int mymax (int a, int b) {return (a > b) ? a : b;}
inline void minim (int &d, int s) {if (d > s) d = s;}

int solve (int d, int a, int m, int n) {
  int i, j, k;
  for (i = 0; i < 256; i ++) dp [0][i] = 0;
  for (i = 0; i < n; i ++) {
    int rd = i & 1, wr = 1 - rd, pix;
    scanf ("%d", &pix);
    for (j = 0; j < 256; j ++) dp [wr][j] = INF;
    for (j = 0; j < 256; j ++) {  // Send
      // Do nothing (if allowed to).
      if ((j >= pix - m) && (j <= pix + m)) minim (dp [wr][pix], dp [rd][j]);
      // Delete pix.
      minim (dp [wr][j], dp [rd][j] + d);
      // Change pix to k, with necessary inserts.
      if (m > 0) {
        for (k = 0; k < 256; k ++) {
          int dif = myabs (k - j), numAdd = (mymax (0, dif - 1)) / m;
          minim (dp [wr][k], dp [rd][j] + numAdd * a + myabs (pix - k));
        }
      } else {
        minim (dp [wr][j], dp [rd][j] + myabs (pix - j));
      }
    }
    //for (j = 0; j < 256; j ++) printf ("%d ", dp [wr][j]);
    //printf ("\n");
  }
  int ret = INF;
  for (i = 0; i < 256; i ++) minim (ret, dp [n & 1][i]);
  return ret;
}

int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    int d, a, m, n;
    scanf ("%d%d%d%d", &d, &a, &m, &n);
    printf ("Case #%d: %d\n", ca, solve (d, a, m, n));
  }
  return 0;
}

