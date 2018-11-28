#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef long long ll;
const int mod = 100003;
const int N = 600;
int dp[N][N];
ll x[600];
ll eGcd ( ll a, ll b , ll &x, ll &y ){
 if ( b == 0 )
    {
     x = 1;
     y = 0;

     return a;
    }

 else
    {
     ll ans = eGcd ( b, a % b, x, y );
     ll t = x;
     x = y;
     y = t - ( a / b ) * y;

     return ans;
    }

}

ll comb(int n, int m) {
	m = min(n-m, m);
	ll res = 1;
	for (int i=1; i<=m; ++i) {
		res = res*(n-m+i)*x[i];
		res %= mod;
	}
	return res;
}

ll solve(int n, int p) {
	if (p==1) return 1;
	if (dp[n][p]) return dp[n][p];
	ll res = 0;
	for (int i=1; i<p; ++i) {
		if (n-p<p-i) continue;
		res += solve(p, i) * comb(n-p-1, p-i-1);
		res %= mod;
	}
	return dp[n][p] = res;
}


int main() {
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	memset(dp, 0, sizeof(dp));

	for (int i=1; i<=300; ++i) {
		ll y;
		eGcd(ll(i), ll(mod), x[i], y);
	}
	for (int cass=1; cass<=cas; ++cass) {
		int n;
		scanf("%d", &n);
		int res = 0;
		for (int i=1; i<n; ++i) {
			res += solve(n, i);
			res %= mod;
		}
		res %= mod;
		if (res<0) res += mod;
		printf("Case #%d: %d\n", cass, res);
	}


	return 0;
}