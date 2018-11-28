#include <cstdio>

const int p = 10007;
int f[10007], inv[10007];

int fac(int n) {
  if ((n/p)&1)
    return -f[n%p];
  return f[n%p];
}

int v(int n) {
  int t;
  n /= p;
  for (t = 0; n; n /= p)
    t += n;
  return t;
}

int C(int n, int r) {
  if (v(n) != v(r) + v(n - r))
    return 0;
  return fac(n)*inv[fac(r)]%p*inv[fac(n - r)]%p;
}

int T, h, w, n, x[16], y[16], ans;

int sol(int a, int b) {
  if ((2*a - b)%3 || (2*b - a)%3)
    return 0;
  int x = (2*a - b)/3, y = (2*b - a)/3;
  if (x < 0 || y < 0)
    return 0;
  return C(x + y, x);
}

int z(int b) {
  int cx = 1, cy = 1, k = 1, c = 0;
  for (int i = 0; i < n; ++i)
    if (b&(1 << i)) {
      ++c;
      k = k*sol(x[i] - cx, y[i] - cy)%p;
      cx = x[i];
      cy = y[i];
    }
  k = k*sol(h - cx, w - cy)%p;
  if (c&1)
    return -k;
  return k;
}

int main() {
  f[0] = 1;
  for (int i = 1; i < p; ++i) {
    f[i] = f[i - 1]*i%p;
    inv[i] = 1;
    while (i*inv[i]%p != 1)
      ++inv[i];
  }
  scanf("%d", &T);
  for (int r = 1; r <= T; ++r) {
    ans = 0;
    scanf("%d%d%d", &h, &w, &n);
    for (int i = 0; i < n; ++i)
      scanf("%d%d", x + i, y + i);
    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j)
        if (x[i] > x[j]) {
          x[i] ^= x[j] ^= x[i] ^= x[j];
          y[i] ^= y[j] ^= y[i] ^= y[j];
        }
    for (int i = 0; i < 1 << n; ++i)
      ans = (ans + z(i) + p)%p;
    printf("Case #%d: %d\n", r, ans);
  }
  return 0;
}
