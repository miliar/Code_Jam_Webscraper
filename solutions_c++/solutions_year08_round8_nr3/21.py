#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <sstream>
#include <map>
#include <queue>

using namespace std;

const int INF = 1e9;
const double eps = 1e-9;
const int NN = 1 << 20;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const ll MOD = 1000000009;

#define mp make_pair
#define pb push_back

int test = 1;
int n, k;	

vi G[1 << 10];
const int nn = 1 << 10;

ll res = 0;

ll pow(ll x, ll p) {
	if (p == 0) return 1;
	ll y = pow(x, p / 2);
	if (p & 1) {
		return (((y*y)%MOD)*x)%MOD;
	} else {
		return (y*y)%MOD;
	}
}

ll C(int n, int m) {
	ll res = 1;
	if (m > n) return 0;
	for (int i = 1; i <= m; i++) {
		res = (res*(n-i+1)) % MOD;
//		ll z = pow(i, MOD - 2);
//		res = (res*z) % MOD;
	}
	return res;
}

void dfs(int x, int p, int z) {
	int s = G[x].size(); if (p > 0) s--;
	ll D = C(k - z, s);
	res = (res* D) % MOD;
	int Z = G[x].size();
	for (int i = 0; i < G[x].size(); i++) if (G[x][i] != p) {
		dfs(G[x][i], x, Z);
	}
}

void solve() {
	cin >> n >> k;
	
	for (int i = 0; i < nn; i++) G[i].clear();

	for (int i = 0; i < n - 1; i++) {
		int x, y; cin >> x >> y;
		G[x].push_back(y);
		G[y].push_back(x);
	}
	res = 1;
	dfs(1, 0, 0);

	cout << "Case #" << test << ": " << res << endl;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T = 1;
	cin >> T;
	for (; test <= T; test++)
	solve();
	return 0;
}