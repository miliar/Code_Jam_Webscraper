#include <iostream>
#include <vector>

using namespace std;

const int INFTY = 100500;

int getbest(int sum)
{
  return (sum + 2) / 3;
}

int getsurpise(int sum)
{
  if (sum % 3 == 0) {
    if (sum < 30 && sum > 0) return sum / 3 + 1;
    else return -1;

  } else if (sum % 3 == 1) {
    if (sum > 1) return sum / 3 + 1;
    else return -1;

  } else {
    if (sum < 29) return sum / 3 + 2;
    else return -1;
  }
}

int solve()
{
  int n, s, p;
  cin >> n >> s >> p;
  vector<int> t(n);
  for (int i = 0; i < n; ++i)
    cin >> t[i];

  vector< vector<int> > dp;
  dp.assign(n + 2, vector<int>(s + 2, 0));

  dp[0][0] = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j <= s; ++j)
      if (dp[i][j] >= 0) {
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (getbest(t[i]) >= p ? 1 : (getbest(t[i]) < 0 ? -1 : 0)  ));
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (getsurpise(t[i]) >= p ? 1 : (getsurpise(t[i]) < 0 ? -1 : 0) ));
      }
  }
  return dp[n][s];
}

int main()
{
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: %d\n", test, solve());
  }
  return 0;
}
