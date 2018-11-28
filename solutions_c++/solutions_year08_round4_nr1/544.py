#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

#define MAX 10003

ll dp[MAX][2];
int val[MAX][3];

ll mini(ll a, ll b) {
    if (a < b) return a;
    return b;
}

int main () {
    int N, M, V, cs=0;
    cin >> N;
    int i, j;
    while (N--) {
        cin >> M >> V;
        int mid = (M-1);
        mid >>= 1;
        for (i=1; i<=mid; i++) {
            cin >> val[i][1] >> val[i][2];
        }
        for (i=mid+1; i<=M; i++) {
            cin >> val[i][0];
        }
        for (i=mid; i>=1; i--) {
            int ch = 2*i;
            if (val[i][1]) {
                val[i][0] = val[ch][0] & val[ch+1][0];
            }
            else val[i][0] = val[ch][0] | val[ch+1][0];
        }
        for (i=0; i<MAX; i++) {
            for (j=0; j<2; j++) dp[i][j] = INT_MAX;
        }
        for (i=M; i>=1; i--) {
            for (j=0; j<2; j++) {
                if (val[i][0] == j) {
                    dp[i][j] = 0;
                }
                else {
                    int ch = 2*i;
                    if (ch > M) {
                        dp[i][j] = INT_MAX;
                    }
                    else {
                        int mi = INT_MAX;
                        if (val[i][1] == 1) {
                            if (j == 0) {
                                mi = mini(mi, (ll)dp[ch][1] + dp[ch+1][0]);
                                mi = mini((ll)dp[ch][0] + dp[ch+1][1], mi);
                                mi = mini((ll)dp[ch][0] + dp[ch+1][0], mi);
                                if (val[i][2]) {
                                    mi = mini((ll)1 + dp[ch][0] + dp[ch+1][0], mi);
                                }
                            }
                            else if (j == 1) {
                                mi = mini((ll)dp[ch][1] + dp[ch+1][1], mi);
                                if (val[i][2]) {
                                    mi = mini((ll)1 + dp[ch][1] + dp[ch+1][0], mi);
                                    mi = mini((ll)1 + dp[ch][0] + dp[ch+1][1], mi);
                                    mi = mini((ll)1 + dp[ch][1] + dp[ch+1][1], mi);
                                }
                            }
                        }
                        else {
                            if (j == 0) {
                                mi = mini((ll)dp[ch][0] + dp[ch+1][0], mi);
                                if (val[i][2]) {
                                    mi = mini((ll)1 + dp[ch][1] + dp[ch+1][0], mi);
                                    mi = mini((ll)1 + dp[ch][0] + dp[ch+1][1], mi);
                                    mi = mini((ll)1 + dp[ch][0] + dp[ch+1][0], mi);
                                }
                            }
                            else if (j == 1) {
                                mi = mini((ll)dp[ch][0] + dp[ch+1][1], mi);
                                mi = mini((ll)dp[ch][1] + dp[ch+1][0], mi);
                                mi = mini((ll)dp[ch][1] + dp[ch+1][1], mi);
                                if (val[i][2]) {
                                    mi = mini((ll)1 + dp[ch][1] + dp[ch][1], mi);
                                }
                            }
                        }
                        dp[i][j] = mi;
                    }
                }
            }
        }
        if (dp[1][V] >= INT_MAX) {
            cout << "Case #" << ++cs << ": IMPOSSIBLE" << endl;
        }
        else cout << "Case #" << ++cs << ": " << dp[1][V] << endl;
    }
    return 0;
}
