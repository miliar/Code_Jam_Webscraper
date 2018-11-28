#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N, S, p;
int t[110];
int dp[110][110];

void init() {
    cin >> N >> S >> p;
    for (int i = 0; i < N; i++) cin >> t[i];
    memset(dp, 0, sizeof(dp));
}

void checkGoogler(int tot, int& m1, int& m2) {
    m1 = m2 = -1;
    for (int i = 0; i <= 10; i++) {
        for (int j = max(0, i - 2); j <= min(10, i + 2); j++) {
            if (i + j > tot) continue;
            int k = tot - i - j;
            if (abs(i - k) > 2 || abs(j - k) > 2) continue;
            bool sur = abs(i - k) == 2 || abs(i - j) == 2 || abs(j - k) == 2;
            if (!sur) {
                m1 = max(m1, max(i, max(j, k)));
            } else {
                m2 = max(m2, max(i, max(j, k)));
            }
        }
    }
}

void solve() {
    int m1, m2;
    checkGoogler(t[0], m1, m2);
    if (m1 >= p) dp[0][0] = 1;
    if (m2 != -1) {
        dp[0][1] = m2 >= p;
    }
    for (int i = 1; i < N; i++) {
        checkGoogler(t[i], m1, m2);
        if (m1 != -1) {
            for (int j = 0; j <= S; j++) {
                dp[i][j] = dp[i - 1][j] + (m1 >= p);
            }
        }
        if (m2 != -1) {
            for (int j = 1; j <= S; j++) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (m2 >= p));
            }
        }
    }
    cout << dp[N - 1][S] << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        init();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
