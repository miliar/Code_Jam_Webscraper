#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define ALL(x) (x).begin(), (x).end()
#define MP make_pair

using namespace std;

string a = "welcome to code jam";

int dp[501][501];

int main() {
  int N;
  scanf("%d ", &N);
  REP(n, N) {
    string b;
    getline(cin, b);

    REP(i, a.size() + 1) REP(j, b.size() + 1) {
      if (i == 0 && j == 0) {
        dp[i][j] = 1;
      } else if (i == 0) {
        dp[i][j] = dp[i][j - 1];
      } else if (j == 0) {
        dp[i][j] = 0;
      } else {
        dp[i][j] = dp[i][j - 1];
        if (a[i - 1] == b[j - 1]) {
          dp[i][j] += dp[i - 1][j - 1];
          dp[i][j] %= 10000;
        }
      }
    }
//     REP(i, a.size() + 1) {
//       REP(j, b.size() + 1) cout << dp[i][j] << " ";
//       cout << endl;
//     }
    printf("Case #%d: %04d\n", n + 1, dp[a.size()][b.size()]);
  }
  return 0;
}
