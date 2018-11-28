#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define LET(name, value) __typeof(value) name = value
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for (int i = (a); i < (int)(b); ++i)
#define FOREQ(i, a, b) for (int i = (a); i <= (int)(b); ++i)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for (LET(i, (c).begin()); i != (c).end(); ++i)

int main() {
  int T; scanf("%d", &T);
  for (int testcase = 1; testcase <= T; ++testcase) {
    int N; scanf("%d", &N);
    vector<long long> x(N);
    vector<long long> len(N);
    REP(i, N) { scanf("%lld%lld", &x[i], &len[i]); }
    long long D; scanf("%lld", &D);

    vector<long long> dp(N, -1);
    dp[0] = 2*x[0];
    FOR(i, 1, N) {
      REP(j, i) {
        if (dp[j] < x[i]) { continue; }
        long long diff = x[i] - x[j];
        if (diff > len[i]) {
          dp[i] = max(dp[i], x[i] + len[i]);
        } else {
          dp[i] = max(dp[i], x[i] + diff);
        }
        assert(dp[i] <= x[i] + len[i]);
      }
    }

    printf("Case #%d: ", testcase);
    bool ans = false;
    REP(i, N) {
      if (dp[i] >= D) {
        ans = true;
        break;
      }
    }
    puts(ans ? "YES" : "NO");
  }
}
