#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int T, t, n, s, p, arr[200];

int dp[200][200];

const int IMPOSSIBLE = -1000000;
int solve(int idx, int rem) {
    if(idx == n) {
        return rem == 0 ? 0 : IMPOSSIBLE;
    }
    int& result = dp[idx][rem];
    if(result == -1) {
        result = IMPOSSIBLE;
        // not special
        int min_score = arr[idx] / 3, max_score = (arr[idx] + 2) / 3;
        result = solve(idx + 1, rem) + ((max_score >= p) ? 1 : 0);
        // special
        if(rem > 0 && arr[idx] >= 2) {
           int tresult = solve(idx + 1, rem - 1) + ((max_score + 1 >= p) ? 1 : 0);
           result = max(result, tresult);
        }
    }
    return result;
}

int main() {
    cin >> T;
    for(t = 1; t <= T; t ++) {
        cin >> n >> s >> p;
        for(int i = 0; i < n; i ++) {
            cin >> arr[i];
        }
        memset(dp, -1, sizeof dp);
        cout << "Case #" << t << ": " << solve(0, s) << endl;
    }
    return 0;
}
