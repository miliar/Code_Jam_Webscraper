#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int n, w, l;
pair <int, int> C[2000];
int X[2000], Y[2000];

int go (int ax, int ay, int bx, int by, int p) {
  //printf ("%d %d %d %d %d\n", ax, ay, bx, by, p);
  if (p == 0) return p;
  int r = C[p - 1].first;
  int cx = ax == 0 ? 0 : ax + r;
  int cy = ay == 0 ? 0 : ay + r;
  if (cx > w || cy > l) return p;
  if (bx < w && cx + r > bx) return p;
  if (by < l && cy + r > by) return p;
  X[C[p - 1].second] = cx;
  Y[C[p - 1].second] = cy;
  --p;
  p = go (cx + r, ay, bx, cy + r, p);
  p = go (ax, cy + r, cx + r, by, p);
  p = go (cx + r, cy + r, bx, by, p);
  return p;
}



int main () {
  int tn;
  scanf ("%d", &tn);
  for (int tc = 1; tc <= tn; tc++) {
    scanf ("%d%d%d", &n, &w, &l);
    for (int i = 0; i < n; i++) {
      scanf ("%d", &C[i].first);
      C[i].second = i;
    }
    sort (C, C + n);
    int r = go (0, 0, w, l, n);
    assert (r == 0);
    printf ("Case #%d:", tc);
    for (int i = 0; i < n; i++) printf (" %d.0 %d.0", X[i], Y[i]);
    puts ("");
  }
  return 0;
}
