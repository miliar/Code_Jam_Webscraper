#include <iostream>
using namespace std;

int D, I, M, N;
int a[128], dp[128][512], tmp[512];

inline int absv(int x) { return (x >= 0 ? x : -x); }

inline int mincost(int x, int y) {
  if(M == 0) return absv(x-y);
  return min(absv(x-y), ((absv(x-y) + M - 1) / M) * I);
}

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    cin >> D >> I >> M >> N;

    for(int i = 0; i < N; i++)
      cin >> a[i];

    for(int i = 0; i < 256; i++)
      dp[0][i] = mincost(a[0], i);
    dp[0][256] = D;

    for(int i = 1; i < N; i++) {
      for(int j = 0; j < 256; j++)
        tmp[j] = min(dp[i-1][j] + D, dp[i-1][256] + absv(a[i]-j));

      for(int j = 0; j < 256; j++)
        for(int k = 0; k < 256; k++)
          if(absv(j-k) <= M)
            tmp[k] = min(tmp[k], dp[i-1][j] + absv(a[i]-k));

      for(int j = 0; j < 256; j++) {
        dp[i][j] = tmp[j];
        for(int k = 0; k < 256; k++)
          if(M > 0)
            dp[i][j] = min(dp[i][j], tmp[k] + ((absv(k-j) + M - 1) / M) * I);
      }

      dp[i][256] = dp[i-1][256] + D;
    }

    int res = 1000000000;
    for(int i = 0; i <= 256; i++)
      res = min(res, dp[N-1][i]);

    printf("Case #%d: %d\n", c, res);
  }
  return 0;
}
