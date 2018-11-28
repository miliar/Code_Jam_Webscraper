#include <iostream>
using namespace std;

int n;
bool vis[16][1024][16];
long long dp[16][1024][16], P[16][1024];
int M[1024];

long long go(int d, int r, int m) {
  if(vis[d][r][m]) return dp[d][r][m];

  if(d == n) {
    if(m > M[r]) return 1000000000;
    return 0;
  }

  vis[d][r][m] = true;
  return dp[d][r][m] = min(P[d][r]+go(d+1, 2*r, m)+go(d+1, 2*r+1, m), go(d+1, 2*r, m+1)+go(d+1, 2*r+1, m+1));
}

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    cin >> n;
    for(int i = 0; i < (1<<n); i++) {
      cin >> M[i];
    }
    for(int i = n-1; i >= 0; i--)
      for(int j = 0; j < (1<<i); j++)
        cin >> P[i][j];

    memset(vis, 0, sizeof(vis));
    printf("Case #%d: %lld\n", c, go(0, 0, 0));
  }

  return 0;
}
