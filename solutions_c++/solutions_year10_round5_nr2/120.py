#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;

int N;
ll L;
ll len[100];

inline ll mod(const ll& x, const ll& m) {
	return ((x % m) + m) % m;
}

ll gcd(ll a, ll b) {
	while(a && b) a > b ? a %= b : b %= a;
	return a | b;
}

ll egcd(ll a, ll b, ll& x, ll &y) {
	if (!b) { x = 1; y = 0; return a; }
	ll result = egcd(b, a%b, y, x);
	y -= x * (a/b);
	return result;
}

ll modinv(const ll& a, const ll& m) {
	if(a == 0) return 0;
	// ax + ym = 1
	ll x, y;
	ll g = egcd(a, m, x, y);
	if(g != 1) cerr << " egcd ERROR a=" << a << " m=" << m << " g=" << g << endl;
	return mod(x, m);
}

const ll MAXI = 100000;

ll cc[MAXI + 1];
ll dp(const ll& x) {
	if(x == 0) return 0;
	ll& ret = cc[x];
	if(ret >= 0) return ret;
	ret = MAXI * 2;
	for(int i = 0; i < N; ++i) {
		if(len[i] > x) continue;
		ll z = dp(x - len[i]) + 1;
		ret = min(ret, z);
	}
	return ret;
}

const string dun = "IMPOSSIBLE";

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> L >> N;
		ll maxi = 0;
		ll g = 0;
		for(int i = 0; i < N; ++i) {
			cin >> len[i];
			g = gcd(len[i], g);
			maxi = max(maxi, len[i]);
		}
		ll ans = -1;
		if (L % ans == 0) {
			// solve
			for(ll i = 0; i <= MAXI; ++i) {
				cc[i] = -1;
			}
			ll cutz = L - MAXI + 200;
			ll need = cutz / maxi;
			ll left = L - need * maxi;
			ll z = dp(left);
			if(z <= MAXI) {
				ans = z + need;
			}
		}
		if (ans == -1) {
			cout << "Case #" << tt << ": " << dun << endl;
		} else {
			cout << "Case #" << tt << ": " << ans << endl;
		}
	}
	return 0;
}

