#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

const int MAXC = 1005;
const int MAXN = 1005;
const int MAXL = 5;

int cc;
int l, t, n, c;
int dist, k, res;
int d[MAXC];
int dp[MAXN][MAXL];

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        scanf("%d%d%d%d", &l, &t, &n, &c);
        for (int i = 0; i < c; i++) scanf("%d", &d[i]);
        memset(dp, 63, sizeof(dp));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            dist = d[(i - 1) % c];
            // Can use booster
            if (dp[i - 1][0] + dist * 2 > t) {
                if (dp[i - 1][0] < t) {
                    k = (t - dp[i - 1][0]) / 2 + ((t - dp[i - 1][0]) % 2);
                    dp[i][1] = dp[i - 1][0] + k * 2 + (dist - k);
                } else {
                    for (int j = 1; j <= l; j++) {
                        dp[i][j] = min(dp[i - 1][j] + dist * 2, dp[i - 1][j - 1] + dist);
                    }
                }
            }
            dp[i][0] = dp[i - 1][0] + dist * 2;
        }
        res = dp[n][0];
        for (int i = 1; i <= l; i++) res = min(res, dp[n][i]);
        cout << "Case #" << cas << ": " << res << endl;
    }
	return 0;
}