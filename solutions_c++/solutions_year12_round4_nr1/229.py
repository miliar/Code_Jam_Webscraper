#include <iostream>
#include <cstring>
using namespace std;

long long d[10100], I[10100], D;
long long dp[10100];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    for (int i = 0; i < n; i++) cin >> d[i] >> I[i];
    cin >> D;

    memset(dp, 0, sizeof(dp));
    dp[0] = d[0];
    bool can = false;
    for (int i = 0; i < n; i++) {
      for (int j = i+1; j < n; j++) {
        if (d[i] + dp[i] < d[j]) break;
        dp[j] = max(dp[j], min(I[j], d[j] - d[i]));
      }
      if (d[i] + dp[i] >= D) {
        can = true;
        break;
      }
    }

    cout << "Case #" << c << ": " << (can ? "YES" : "NO") << endl;
  }
  return 0;
}
