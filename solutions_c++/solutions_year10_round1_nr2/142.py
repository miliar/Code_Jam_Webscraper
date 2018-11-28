#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <numeric>
#include <cctype>
#include <list>
#include <functional>
#include <stack>
#include <fstream>
#include <sstream>
#include <cstring>
#include <cstdlib>

#define size(c) (int)c.size()
using namespace std;

typedef pair<int, int> edge;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef map<string, int> msi;
typedef pair<int, int> pii;
const int inf = 1 << 29;
const int maxn = 270;
int T, D, I, M, N;
int A[maxn];
int dp[maxn][maxn];
int main()
{
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        cin >> D >> I >> M >> N;
        for (int i = 1; i <= N; ++ i) cin >> A[i];
        for (int i = 0; i < maxn; ++ i)
            for (int j = 0; j < maxn; ++ j)
                dp[i][j] = inf;
        for (int i = 0; i < maxn; ++ i) dp[0][i] = 0;
        for (int i = 1; i <= N; ++ i) {
            for (int j = 0; j < maxn; ++ j) {
                dp[i][j] <?= dp[i - 1][j] + D;
                if (M != 0) {
                    for (int k = 0; k < maxn; ++ k) {
                        int toadd = (abs(k - j) - 1) / M;
                        toadd >?= 0;
                       // if (toadd < 0) cout << "wrong" << endl;
                        dp[i][j] <?= dp[i - 1][k] + I * toadd + abs(j - A[i]);
                    }
                } else dp[i][j] <?= dp[i - 1][j] + abs(j - A[i]);
            }
        }
        int ans = inf;
        for (int i = 0; i < maxn; ++ i) ans <?= dp[N][i];
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
