#include <cstdio>
#include <algorithm>

using namespace std;

int main (void) {
  int tn;
  scanf ("%d", &tn);
  for (int tt = 1; tt <= tn; tt++) {
    int t[2] = {0}, p[2] = {1, 1};

    int n;
    scanf ("%d", &n);
    int pt = 0;
    for (int i = 1; i <= n; i++) {
      int c;
      while ((c = getc(stdin)) != 'O' && c != 'B') {
      }
      c = c == 'O';
      int x;
      scanf ("%d", &x);
      pt = t[c] = max (t[c] + abs (x - p[c]) + 1, pt + 1);
      p[c] = x;
    }

    printf ("Case #%d: %d\n", tt, pt);
  }
  return 0;
}