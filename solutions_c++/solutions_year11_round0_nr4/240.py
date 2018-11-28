/* Google Code Jam 2011, Qualification Round, Problem D: "GoroSort". */
/* Fri. May. 6, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 6, 2011.
#include <cstdio>

#if 0
#define NLIM 1024

#include <algorithm>
using namespace std;
int countCycle (int n, int *dst, int *src) {
  int seen[NLIM] = {0}, dstPos = 0;
  for (int i = 0; i < n; ++ i) {
    if (seen [i]) continue;
    int v = 0;
    for (int j = i; !seen[j]; j = src[j], ++ v) seen[j] = 1;
    dst[dstPos ++] = v;
  }
  return dstPos;
}

// Unused: Solutions for n-cycles.
// Emperically: [0, 0, 2, 3, 4, 5, 6, 7, 8, ...] => ASSUME WITHOUT PROOF this works in general!!!
double cycExp[NLIM + 1];
void gen (void) {
  int p[NLIM], cycle[NLIM];
  for (int i = 0; i < NLIM; ++ i) p[i] = i;
  cycExp[1] = 0;
  for (int n = 2; n <= NLIM; ++ n) {
    int fact = 0;
    cycExp[n] = 0;
    do {
      ++ fact;
      int nCy = countCycle (n, cycle, p);
      if (nCy > 1) {
        double e = 0;
        for (int i = 0; i < nCy; ++ i) {
          e += cycExp[cycle[i]];
        }
        cycExp[n] += e;        
      }
    } while (next_permutation (p, p + n));
    // x = 1 + ((n - 1)! / n!) x + (sum non-uni perms) / n!
    //   = 1 + x / n + (sum non-uni perms) / n!
    // x - x / n = 1 + (sum non-uni perms) / n!
    // x = (n / (n - 1)) [1 + (sum non-uni perms) / n!]
    cycExp[n] = n / (n - 1.0) * (1 + cycExp[n] / fact);
  }
  for (int i = 1; i <= NLIM; ++ i) printf ("%d: %.6f\n", i, cycExp[i]);
}
#endif


int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  // Each m-cycle contributes 0 if m = 1, and m otherwise.
  // So contribution of all cycles is n - #(fix points).
  for (ca = 1; ca <= nc; ++ ca) {
    int n, v, sol = 0;
    scanf ("%d", &n);
    for (int i = 0; i < n; ++ i) {
      scanf ("%d", &v);
      if (v - 1 != i) ++ sol;
    }
    printf ("Case #%d: %.6f\n", ca, (double) sol);
  }
  return 0;
}
