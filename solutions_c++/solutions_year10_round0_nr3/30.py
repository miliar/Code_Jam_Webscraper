/* Google Code Jam 2010, Qualification Round, Problem C: "Theme Park". */
/* Fri. May. 7, 2010, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 7, 2010.
#include <cstdio>

int size [1024];  // [mass]
int seen [1024];  // [mass]
int part [1024];  // [space]

int main (void) {
  int nc, ca, r, k, n, i, j;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    scanf ("%d%d%d", &r, &k, &n);
    for (i = 0; i < n; i ++) {
      scanf ("%d", &size [i]);
      seen [i] = -1;
      part [i] = -1;
    }
    int head = 0;
    long long sol = 0;
    for (i = 0; (i < r) && (seen [head] < 0); i ++) {
      int cap = k;
      seen [head] = i;
      for (j = 0; j < n; j ++) {
        if (cap < size [(head + j) % n]) break;
        cap -= size [(head + j) % n];
      }
      sol += (part [i] = k - cap);
      head = (head + j) % n;
    }
    //printf ("[%d %d]\n", i, r);
    if (i < r) {
      int lo = seen [head], len = i - lo;
      for (j = 0; j < len; j ++) {
        long long mult = (r - lo - j - 1) / len;
        //printf (" %d => %d/%d %lld %d\n", j, r - lo - j - 1, len, mult, part [lo + j]);
        sol += mult * part [lo + j];
      }
    }
    printf ("Case #%d: %lld\n", ca, sol);
  }
  return 0;
}
