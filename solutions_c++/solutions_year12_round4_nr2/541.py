#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iomanip>
#include <sstream>

using namespace std;

int dp[10005];

void solve() {
    int n;
    cin >> n;
    int now = 0;
    vector<int> d(n), l(n);
    int D;
    for (int i=0; i<n; i++) {
        cin >> d[i] >> l[i];
    }
    cin >> D;
    for (int i=0; i<10005; i++) {
        dp[i] = 0;
    }
    dp[0] = d[0];
    for (int i = 0; i < n; i++) {
        //cout << dp[i] << endl;
        if (d[i] + dp[i] >= D) {
            cout << "YES" << endl;
            return;
        }
        int j;
        for (j = i+1; j<n; j++) {
            if (d[i] + dp[i] < d[j])break;
            dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
            //cout << "\t" << dp[j] << endl;
        }
    }
    cout << "NO" << endl;
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
