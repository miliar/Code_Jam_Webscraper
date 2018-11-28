#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
using namespace std;

const int N = 20000;

int t, n, d[N], len[N], D;
int dp[N];

bool solve() {
    memset(dp, -1, sizeof dp);
    if(d[0] > len[0]) dp[0] = -1; else dp[0] = d[0];
    for(int i = 0; i < n; i ++) {
        //cout << i << endl;
        if(dp[i] == -1) return false;
        dp[i] = min(dp[i], len[i]);
        for(int j = i + 1; j < n && d[j] - d[i] <= dp[i]; j ++) {
          //  cout << " --" << j << endl;
            dp[j] = max(dp[j], d[j] - d[i]);
        }
    }
    for(int i = 0; i < n; i ++) {
        if(d[i] + dp[i] >= D) return true;
    }
    return false;
}

int main() {
    cin >> t;
    for(int I = 1; I <= t; I ++) {
        cin >> n;
        for(int i = 0; i < n; i ++) {
            cin >> d[i] >> len[i];
        }
        cin >> D;
        cout << "Case #" << I << ": " << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}
