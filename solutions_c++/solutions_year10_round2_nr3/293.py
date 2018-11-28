#include <iostream>

using namespace std;

int C[505][505];

const int MOD = 100003;

int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  for (int i = 0; i < 505; i++)
  {
    C[i][0] = 1;
    for (int j = 1; j <= i; j++)
    {
      C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
    }
  }
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int n;
    cin >> n;
    int dp[505][505] = {0};
    dp[1][1] = 1;
    for (int i = 2; i <= n; i++)
    {
      dp[i][1] = 1;
      for (int j = 2; j < i; j++)
      {
        for (int k = 1; k < j; k++)
        {
          dp[i][j] += (dp[j][k] * C[i-j-1][j-k-1]) % MOD;
        }
      }
    }
    int ans = 0;
    for (int i = 1; i < n; i++)
    {
      ans += dp[n][i];
      ans %= MOD;
    }
    cout << ans << endl;
  }
  return 0;
}