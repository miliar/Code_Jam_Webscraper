#include <cstdio>


int main (void) {
  int tn;
  scanf ("%d", &tn);

  for (int tt = 1; tt <= tn; tt++) {
    int n, x = 0, y = 1000000000, v, sum = 0;
    scanf ("%d", &n);
    while (n--) {
      scanf ("%d", &v);
      x ^= v;
      sum += v;
      if (y > v) {
        y = v;
      }
    }
    printf ("Case #%d: ", tt);
    if (x) {
      printf ("NO\n");
    } else {
      printf ("%d\n", sum - y);
    }
  } 

  return 0;
}