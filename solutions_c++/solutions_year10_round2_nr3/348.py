#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <sstream>
#include <complex>
#include <bitset>
#include <numeric>
#include <valarray>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cstdlib>
using namespace std;
#define rep(i,n) for(int i = 0;i < (int)(n); i++)
#define all(a) (a).begin(),(a).end()
#define foreach(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

const int inf = 987654321;
const int mod = 100003;

int ans[1000];

int dp[1000][1000];
int _binom[1000][1000];

int binom(int n, int r) {
    if (n < r) return 0;
    if (_binom[n][r] != -1) return _binom[n][r];
    else {
        return (r == 0 || r == n) ? 1 : (_binom[n][r] = (binom(n-1, r-1) + binom(n-1,r)) % mod);
    }
}

int _solve(int n, int k) { // n is k th
    if (dp[n][k] != -1) return dp[n][k];
    if (k == 1) return 1;
    int ans = 0;
    for (int i = 1; i <= k-1; ++i) {
        ans += _solve(k,i) * binom(n-k-1, k-1-i);
        //cout << "binom " << n-k-1 << ' ' << k-1-i << "->" << binom(n-k-1, k-1-i) << endl;
        ans %= mod;
    }
    //cout << n << " is " << k << " th -> " << ans << endl;
    return dp[n][k] = ans;
}

int solve(int n) {
    int ans = 0;
    for (int i = 1; i <= n-1; ++i) { // n is rank i
        ans += _solve(n,i);
        ans %= mod;
    }
    return ans;
}

int main() {
    rep(i,1000) ans[i] = -1;
    rep(i,1000) rep(j,1000) dp[i][j] = _binom[i][j] = -1;
    int T;
    cin >> T;
    rep(I,T) {
        int n;
        cin >> n;
        if (ans[n] == -1) ans[n] = solve(n);
        cout << "Case #" << I+1 << ": " << ans[n] << endl;
    }
    return 0;
}
