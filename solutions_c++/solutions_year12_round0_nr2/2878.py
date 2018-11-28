#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <sstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define VAR(a) cout << #a << " : " << a << endl;

typedef long long int lli;

using namespace std;

int main(int argc, char *argv[])
{
  const int T = 30 + 1;
  int sup[T];
  int normal[T];

  fill(sup, sup + T, -1);
  fill(normal, normal + T, -1);

  for (int a = 0; a <= 10; ++a) {
    for (int b = 0; b <= 10; ++b) {
      for (int c = 0; c <= 10; ++c) {
        int s = abs(a - b);
        int t = abs(a - c);
        int u = abs(b - c);
        if (2 < max(s, max(t, u))) continue;
        
        int sum = a + b + c;
        int mx = max(a, max(b, c));
        if (s == 2 || t == 2 || u == 2) {
          sup[sum] = max(sup[sum], mx);
        } else {
          normal[sum] = max(normal[sum], mx);
        }
      }
    }
  }

  int tc;
  cin >> tc;
  while (tc--) {
    int n, s, p;
    cin >> n >> s >> p;

    int score[n];
    for (int i = 0; i < (int)n; ++i) {
      cin >> score[i];
    }

    const int N = 100 + 2;
    const int S = 100 + 2;
    int dp[N][S];
    fill(&dp[0][0], &dp[N - 1][S], -1);
    dp[0][0] = 0;

    for (int i = 0; i < (int)n; ++i) {
      for (int j = 0; j < (int)S; ++j) {
        if (dp[i][j] == -1) continue;
        if (j + 1 < S && sup[score[i]] != -1) {
          dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (p <= sup[score[i]]));
        }
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (p <= normal[score[i]]));
      }
    }
    
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << dp[n][s] << endl;    
  }

  return 0;
}
