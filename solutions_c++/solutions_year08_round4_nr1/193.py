#include <cstdio>

int min(int a, int b) {
  return a < b ? a : b;
}

int T, n, v, g[20000][2], t, dp[20000][2];

int main() {
  scanf("%d", &T);
  for (int r = 1; r <= T; ++r) {
    printf("Case #%d: ", r);
    scanf("%d%d", &n, &v);
    for (int i = 1; i << 1 < n; ++i)
      scanf("%d%d", g[i], g[i] + 1);
    for (int i = n + 1 >> 1; i <= n; ++i) {
      scanf("%d", &t);
      dp[i][t] = 0;
      dp[i][!t] = 1 << 20;
    }
    for (int i = n >> 1; i > 0; --i) {
      dp[i][0] = dp[i][1] = 1 << 20;
      if (g[i][1])
        if (g[i][0]) {
          dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][0]);
          dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][1]);
          dp[i][0] = min(dp[i][0], dp[2*i + 1][1] + dp[2*i][0]);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][1]);
          dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][0] + 1);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][0] + dp[2*i][1] + 1);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][0] + 1);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][1] + 1);
        } else {
          dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][0]);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][0] + dp[2*i][1]);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][0]);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][1]);
          dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][0] + 1);
          dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][1] + 1);
          dp[i][0] = min(dp[i][0], dp[2*i + 1][1] + dp[2*i][0] + 1);
          dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][1] + 1);
        }
      else if (g[i][0]) {
        dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][0]);
        dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][1]);
        dp[i][0] = min(dp[i][0], dp[2*i + 1][1] + dp[2*i][0]);
        dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][1]);
      } else {
        dp[i][0] = min(dp[i][0], dp[2*i + 1][0] + dp[2*i][0]);
        dp[i][1] = min(dp[i][1], dp[2*i + 1][0] + dp[2*i][1]);
        dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][0]);
        dp[i][1] = min(dp[i][1], dp[2*i + 1][1] + dp[2*i][1]);
      }
    }
//    for (int i = 1; i < n; ++i)
//      printf("%d %d\n", dp[i][0], dp[i][1]);
    if (dp[1][v] < 1 << 20)
      printf("%d\n", dp[1][v]);
    else
      puts("IMPOSSIBLE");
  }
  return 0;
}
