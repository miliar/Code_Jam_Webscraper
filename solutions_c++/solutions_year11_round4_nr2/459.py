/* Google Code Jam 2011, Round 2, Problem B: "Spinning Blade". */
/* Sat. Jun. 4, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Sat. Jun. 4, 2011.
#include <cstdio>

typedef long long t_space[512][512];

t_space mass, xMom, yMom;
t_space massInt, xMomInt, yMomInt;

void integrate (t_space &d, t_space &s, int h, int w) {
  int i, j;
  for (j = 0; j <= w; ++ j) d[0][j] = 0;
  for (i = 1; i <= h; ++ i) {  // Fetch.
    d[i][0] = 0;
    for (j = 1; j <= w; ++ j) d[i][j] = s[i - 1][j - 1] + d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1];
  }
}

inline long long rectMass (t_space &a, int r1, int c1, int r2, int c2) {
  return a[r2][c2] - a[r1][c2] - a[r2][c1] + a[r1][c1];
}

// Incl. (r1, c1), excl. (r2, c2).
inline long long clover4 (t_space &a, t_space &aInt, int r1, int c1, int r2, int c2) {
  return rectMass (aInt, r1, c1, r2, c2) - a[r1][c1] - a[r1][c2 - 1] - a[r2 - 1][c1] - a[r2 - 1][c2 - 1];
}


int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    int h, w, d;
    scanf ("%d%d%d", &h, &w, &d);
    char tbuf[512];
    for (int i = 0; i < h; ++ i) {
      scanf ("%511s", tbuf);
      for (int j = 0; j < w; ++ j) mass[i][j] = tbuf[j] - '0';  // Not using d.
    }
    for (int i = 0; i < h; ++ i) {
      for (int j = 0; j < w; ++ j) {
        xMom[i][j] = mass[i][j] * j;
        yMom[i][j] = mass[i][j] * i;
      }
    }
    integrate (massInt, mass, h, w);
    integrate (xMomInt, xMom, h, w);
    integrate (yMomInt, yMom, h, w);
    int sol;
    for (sol = (h < w) ? h : w; sol >= 3; -- sol) {
      //printf ("\n");
      for (int i = 0; i + sol <= h; ++ i) {
        for (int j = 0; j + sol <= w; ++ j) {
          long long m = clover4 (mass, massInt, i, j, i + sol, j + sol);
          long long mXCent = clover4 (xMom, xMomInt, i, j, i + sol, j + sol);
          long long mYCent = clover4 (yMom, yMomInt, i, j, i + sol, j + sol);
          // Goal: mXCent / m == j + (sol - 1) / 2 and mYCent / m == i + (sol - 1) / 2.
          // Shifted by (-0.5, -0.5) since mass is concentrated on top-left corner of each square.
          //printf ("(%d %d)-(%d %d): (%f, %f) vs (%f %f)\n", i, j, i + sol - 1, j + sol - 1,
          //    mYCent / (double) m, mXCent / (double) m, (i * 2 + sol - 1) * 0.5, (j & 2 + sol - 1) * 0.5);
          if ((mXCent * 2 == m * (j * 2 + sol - 1)) && (mYCent * 2 == m * (i * 2 + sol - 1))) {
            goto success;
          }
        }
      }
      continue;
success:;
      break;
    }
    if (sol >= 3) {
      printf ("Case #%d: %d\n", ca, sol);
    } else {
      printf ("Case #%d: IMPOSSIBLE\n", ca);
    }
  }
  return 0;
}
