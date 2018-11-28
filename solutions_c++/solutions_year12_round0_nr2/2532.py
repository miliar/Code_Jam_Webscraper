#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>
#include <bitset>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define debug(x) cerr << #x << ": " << x << endl;

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;
typedef pair<int, int> pii;

const string PROBLEM_NAME = "task";

int main() {
    freopen((PROBLEM_NAME + ".in").c_str(), "r", stdin);
    freopen((PROBLEM_NAME + ".out").c_str(), "w", stdout);
    //freopen((PROBLEM_NAME + ".err").c_str(), "w", stderr);
    vector<vector<vector<int> > > amount(31, vector<vector<int> >(2, vector<int> (11, 0)));
    for (int i = 0; i <= 10; ++i) 
        for (int j = 0; j <= 10; ++j) {
            for (int k = 0; k <= 10; ++k) {
                int mi = min(i, min(j, k));
                int ma = max(i, max(j, k));
                if (ma - mi > 2)
                    continue;
                amount[i + j + k][(ma - mi) == 2][ma] += 1;
            }
        }
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cerr << t << " ";
        cout << "Case #" << t + 1 << ": ";
        int n;
        cin >> n;
        int surpr;
        cin >> surpr;
        int atLeast;
        cin >> atLeast;
        vector<int> sums(n);
        for (int i = 0 ;i < n; ++i) {
            scanf("%d", &sums[i]);
        }
        vector<vector<int> > dp(n + 1, vector<int> (surpr + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int s = 0; s <= surpr; ++s) {
                for (int ma = 0; ma <= 10; ++ma) {
                    if (amount[sums[i]][0][ma])
                        dp[i][s] = max(dp[i][s], (ma >= atLeast) + dp[i + 1][s]);
                    if (amount[sums[i]][1][ma] && s)
                        dp[i][s] = max(dp[i][s], (ma >= atLeast) + dp[i + 1][s - 1]);
                }
            }
        }
        cout << dp[0][surpr] << "\n";
    }
    return 0;
}