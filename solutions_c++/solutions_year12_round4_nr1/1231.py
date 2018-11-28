#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cmath> 
#include <ctime> 
#include <float.h> 

using namespace std; 

#define REP(i, from, to) for (int i = (from); i < (to); ++i) 
#define FOR(i, n) REP(i, 0, (n)) 
#define ALL(x) x.begin(), x.end() 
#define SIZE(x) (int)x.size() 
#define PB push_back 
#define MP make_pair 

typedef long long i64; 
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef vector<string> VS; 
typedef vector<VS> VVS; 
typedef pair<int, int> PII; 

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  //freopen("output2.txt", "w", stdout);

  int tests;
  cin >> tests;

  FOR (curTest, tests) {
    int n;
    cin >> n;

    ++n;
    VI d(n), l(n);
    REP (i, 1, n) cin >> d[i] >> l[i];

    int D;
    cin >> D;

    VI dp(n, -1);
    VI next(n, 0);
    dp[1] = 0;
    next[1] = d[1] + d[1];

    FOR (vine, n) if (dp[vine] != -1) {
      int const from = dp[vine];
      int const curLength = min(l[vine], d[vine] - d[from]);

      REP (j, vine + 1, n) if (d[vine] + curLength >= d[j]/* && d[j] - d[dp[i]] <= l[j]*/) {
        if (dp[j] == -1)
          dp[j] = vine;
      }
    }

    bool ok = false;
    FOR (vine, n) {
      if (dp[vine] != -1 && d[vine] + min(l[vine], d[vine] - d[dp[vine]]) >= D)
        ok = true;
    }

    printf("Case #%d: ", curTest + 1);
    /// Print result here
    if (ok) printf("YES");
    else printf("NO");
    ///
    printf("\n");
  }
  
  return 0;
}