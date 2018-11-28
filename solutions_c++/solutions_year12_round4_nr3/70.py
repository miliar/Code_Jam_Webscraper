#include <cstdio>

int D[10000], V[10000];
int n;

//w is coordinate of b + 1
bool solve (int a, int b, int s, int w) {
  if (a > b) return true;
  int h = D[a];
  while (h < b + 1) {
    V[a] = w - (s + 1) * (b - a + 1);
    V[h] = w - (s + 1) * (b - h + 1);
    if (!solve (a + 1, h - 1, s + 2, V[h])) return false;
    a = h;
    h = D[h];
  }
  if (h > b + 1) return false;
  ++s;
  V[a] = w - s * (b - a + 1);
  return solve (a + 1, b, s + 1, w);
}

int main () {
  int tn;
  scanf ("%d", &tn);
  for (int tc = 1; tc <= tn; tc++) {
    scanf ("%d", &n);
    for (int i = 1; i < n; i++) {
      scanf ("%d", &D[i]);
    }
    D[n] = n + 1;
    bool res = solve (1, n, 1, (int)1e9);
    printf ("Case #%d:", tc);
    if (!res) {
      puts (" Impossible");
    } else {
      for (int i = 1; i <= n; i++) printf (" %d", V[i]);
      puts ("");
    }
  }
  return 0;
}
