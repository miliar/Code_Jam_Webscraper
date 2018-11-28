#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define INF  ((1 << 31) - 1)
#define eps 1e-9
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define all(v) (v).begin(), (v).end()
typedef long long ll;
ll mod = 100003;
ll check(ll x){
	return (x % mod + mod) % mod;	
}
vector<vector<ll> > c;
ll count_c(int a, int b){
	if (a < b) return 0;
	if (b == 0 || a == b) return 1;
	if (c[a][b] != -1LL) return c[a][b];
	ll &res = c[a][b];
	res = check(count_c(a - 1, b) + count_c(a - 1, b - 1));
	return res;
}
vector<vector<ll> > dp;
ll f(int n, int k){
	if (k == 1) return 1;
	if (dp[n][k] != -1LL) return dp[n][k];
	ll &res = dp[n][k];
	res = 0LL;
	for (int i = 1; i < k; ++i){
		res = check(res + count_c(n - k - 1, k - i - 1) * f(k, i));
	}
	return res;
}
int main(){
	freopen("C-large.in", "r", stdin);
	freopen("largeout.txt", "w", stdout);
	int T;
	cin >> T;
	dp.assign(600, vector<ll>(600, -1LL));
	c.assign(600, vector<ll>(600, -1LL));
	/*for (int i = 1; i < 6; ++i){
		for (int j = i + 1; j < 6; ++j){
			printf("res f(%d,%d) = %lld\n", j, i, f(j, i));
		}
	}*/
	//cout << f(4,2) << endl;
	for (int it = 1; it <= T; ++it){
		int n;
		cin >> n;
		ll res = 0;
		for (int i = 1; i < n; ++i){
			res = check(res + f(n, i));
		}
		printf("Case #%d: %lld\n", it, res);
		cerr << it << endl;
	}
	return 0;
}