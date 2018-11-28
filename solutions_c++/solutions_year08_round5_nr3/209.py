#include <cstdio>

int cb(int x) {
  int t;
  for (t = 0; x; x &= x - 1)
    ++t;
  return t;
}

int T, n, m, db[10], dp[10][1024], c[1024], t;
char s[256];

int main() {
  for (int i = 0; i < 1024; ++i)
    c[i] = cb(i);
  scanf("%d", &T);
  for (int r = 1; r <= T; ++r) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
      scanf("%s", s);
      db[i] = 0;
      for (int j = 0; j < m; ++j)
        if (s[j] == 'x')
          db[i] |= 1 << j;
    }
    for (int i = 0; i < 1 << m; ++i) {
      dp[0][i] = 0;
      if ((i&(i >> 1)) || (i&(db[0])))
        continue;
      dp[0][i] = c[i];
    }
    for (int i = 1; i < n; ++i)
      for (int j = 0; j < 1 << m; ++j) {
        dp[i][j] = 0;
        if ((j&(j >> 1)) || (j&(db[i])))
          continue;
        for (int k = 0; k < 1 << m; ++k) {
          if ((k&(j >> 1)) || (k&(j << 1)))
            continue;
          if (dp[i][j] < dp[i - 1][k] + c[j])
            dp[i][j] = dp[i - 1][k] + c[j];
        }
      }
    t = 0;
    for (int i = 0; i < 1 << m; ++i)
      if (t < dp[n - 1][i])
        t = dp[n - 1][i];
    printf("Case #%d: %d\n", r, t);
  }
  return 0;
}
