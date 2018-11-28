#include <iostream>
#include <vector>

using namespace std;

const int INF = 1000000000;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    cerr << "ca = " << ca << endl;
    int D, I, M, N;
    cin >> D >> I >> M >> N;
    int ans = INF;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) {
      cin >> a[i];
    }
    vector<vector<int> > dp(N+1, vector<int>(256, INF));
    for (int i = 0; i < int(dp[0].size()); ++i) {
      dp[0][i] = 0;
    }
    for (int i = 1; i <= N; ++i) {
      for (int j = 0; j < int(dp[i].size()); ++j) {
        if (dp[i-1][j]+D < dp[i][j]) {
          dp[i][j] = dp[i-1][j]+D;
        }
        for (int k = max(0, j-M); k < min(int(dp[i].size()), j+M+1); ++k) {
          if (dp[i-1][k]+abs(a[i-1]-j) < dp[i][j]) {
            dp[i][j] = dp[i-1][k]+abs(a[i-1]-j);
          }
        }
        if (M > 0) for (int k = 0; k < int(dp[i].size()); ++k) {
          if (dp[i-1][k]+abs(a[i-1]-j)+I*(max(0, abs(j-k)-1)/M) < dp[i][j]) {
            dp[i][j] = dp[i-1][k]+abs(a[i-1]-j)+I*(max(0, abs(j-k)-1)/M);
          }
        }
      }
    }
    for (int i = 0; i < int(dp[N].size()); ++i) {
      if (dp[N][i] < ans) {
        ans = dp[N][i];
      }
    }
    cout << "Case #" << ca << ": " << ans << endl;
  }
}
