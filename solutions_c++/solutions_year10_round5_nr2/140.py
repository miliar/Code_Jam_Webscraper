#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef long long ll;
typedef vector<ll> vec;
typedef vector<vec> mat;

const int S = 110;

int bs[110];
int dp[S + 10];
ll dist[100010];

mat mat_mul(const mat& a, const mat& b) {
	int n = a.size();
	mat res(n, vec(n, -1));
	for(int i = 0; i < n; ++i) {
		for(int j = 0; j < n; ++j) {
			for(int k = 0; k < n; ++k) if(a[i][k] != -1 && b[k][j] != -1) {
				if(res[i][j] != -1) res[i][j] = min(a[i][k] + b[k][j], res[i][j]);
				else res[i][j] = a[i][k] + b[k][j];
			}
		}
	}
	return res;
}

void debug(const mat& a) {
	int n = a.size();
	for(int i = 0; i < n; ++i) {
		for(int j = 0; j < n; ++j) {
			cerr << a[i][j] << " ";
		}
		cerr << endl;
	}
	cerr << endl;
}

mat mat_pow(mat a, ll n) {
	int m = a.size();
	mat res(m, vec(m, -1));
	for(int i = 0; i < m; ++i) res[i][i] = 0;
	for(; n; n >>= 1) {
		if(n & 1) res = mat_mul(a, res);
		a = mat_mul(a, a);
	}
	return res;
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		ll len;
		int n;
		cin >> len >> n;
		for(int i = 0; i < n; ++i) cin >> bs[i];
		sort(bs, bs + n);
		for(int i = 0; i < S + 10; ++i) dp[i] = -1;
		dp[0] = 0;
		for(int i = 0; i < n; ++i) {
			for(int j = bs[i]; j < S + 10; ++j) if(dp[j - bs[i]] != -1) {
				if(dp[j] != -1) dp[j] = min(dp[j], dp[j - bs[i]] + 1);
				else dp[j] = dp[j - bs[i]] + 1;
			}
		}
		mat m(S, vec(S, -1));
		for(int i = 0; i < S - 1; ++i) {
			m[i][i + 1] = 0;
		}
		for(int i = 1; i <= S; ++i) m[S - 1][S - i] = dp[i];
		mat res = mat_pow(m, len);
		ll r = -1;
		for(int i = 0; i < S; ++i) if(res[0][i] != -1 && dp[i] != -1) {
			if(r != -1) r = min(r, res[0][i] + dp[i]);
			else r = res[0][i] + dp[i];
		}
		printf("Case #%d: ", t + 1);
		if(r == -1) puts("IMPOSSIBLE");
		else printf("%lld\n", r);
	}
	return 0;
}
