#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define debug(x) cerr << __LINE__ << ": " << #x << " = " << (x) << "\n"
#define debugf(x...) fprintf(stderr, x)

const char* const pat = "welcome to code jam";

char s[505];

int dp[505][20];

void solve() {
  fgets(s, 505, stdin);
  int n = strlen(s) + 1, m = strlen(pat) + 1;

  for (int i = 0; i < n; ++i) dp[i][0] = (s[i] == pat[0]);
  for (int i = 1; i < m; ++i) {
    int su = 0;
    for (int j = 0; j < n; ++j) {
      dp[j][i] = (s[j] == pat[i]) ? su : 0;
      su = (su + dp[j][i - 1]) % 10000;
    }
  }

  printf("%04d\n", dp[n - 1][m - 1]);
}

int main() {
  int n;
  scanf("%d\n", &n);
  for (int i = 1; i <= n; ++i) printf("Case #%d: ", i), solve();
  return 0;
}
