#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>

#include <gmp.h>
#include <gmpxx.h>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())


void solve_case() {

    int n, desired;
    cin >> n >> desired;

    int m = (n-1)/2;

    const int INF = 12345;
    vector< vector<int> > dp(n, vector<int>(2, INF));
    vector<int> gates(m);
    vector<int> changable(m);
    for(int i = 0; i < m; i++) {
        cin >> gates[i] >> changable[i];
    }
    for(int i = m; i < n; i++) {
        int x;
        cin >> x;
        dp[i][x] = 0;
    }

    for(int i = m-1; i >= 0; i--) {
        REP(g, 2) {
            int c = (g != gates[i] ? 1 : 0);
            if (c && !changable[i])
                continue;
            REP(l, 2) REP(r, 2) {
                int x = (g ? (l&r) : (l|r));
                dp[i][x] <?= dp[2*i+1][l] + dp[2*i+2][r] + c;
            }
        }
    }

    int res = dp[0][desired];
    if (res >= INF)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << res << endl;
}


int main() {

    int nCases;
    cin >> nCases;

    REP(iCase, nCases) {
        cout << "Case #" << iCase+1 << ": ";
        solve_case();
    }

    return 0;
}
