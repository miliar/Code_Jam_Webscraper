#include <stdio.h>
#include <string.h>

#include <algorithm>

const int MAXN = 20000;

std::pair<int, int> p[MAXN];
int dp[MAXN];
int N, x, y, D;

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    printf("Case #%d: ", tt);
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      scanf("%d%d", &x, &y);
      p[i] = std::make_pair(x, y);
    }
    scanf("%d", &D);
    memset(dp, -1, sizeof(dp));
    dp[0] = p[0].first;
    bool reach = false;
    for (int i = 0; i < N; ++i) {
      if (dp[i] == -1) continue;
      if (p[i].first + dp[i] >= D) reach = true;
      for (int j = i + 1; j < N && p[i].first + dp[i] >= p[j].first; ++j) {
        dp[j] = std::max(dp[j], std::min(p[j].first - p[i].first, p[j].second));
      }
    }
    puts(reach ? "YES" : "NO");
  }
  return 0;
}
