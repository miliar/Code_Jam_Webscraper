#include <cstring>
#include <cstdlib>
#include <limits>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

const int MAX_N = 10000 + 10;
const ll INV = numeric_limits<ll>::max();

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }

ll solve3(ll L, ll H, ll M) {
	// find p in [L, H] s.t. p | M (M != 0)
	if (L > M) return -1;
	if (H > M) H = M;
	ll invL = (M + H - 1) / H, invH = M / L;
	if (invH - invL < H - L) {
		for (ll i = invH; i >= invL; --i)
			if (M % i == 0)
				return M / i;
	} else {
		for (ll i = L; i <= H; ++i)
			if (M % i == 0)
				return i;
	}
	return -1;
}

ll solve2(ll L, ll H, ll X, ll Y) {
	// find p in [L, H] s.t. X | p and p | Y
	ll lo = (L + X - 1) / X, hi = H / X;
	if (lo > hi) return -1;
	if (Y == 0) return lo * X;
	return solve3(lo, hi, Y / X) * X;
}

ll N, L, H, p[MAX_N], a[MAX_N + 1], b[MAX_N + 1];

ll solve() {
	cin >> N >> L >> H;
	for (ll i = 0; i < N; ++i) {
		cin >> p[i];
		if (p[i] == 0) {
			--N;
			--i;
		}
	}
	sort(p, p + N);

	a[0] = 1;
	for (ll i = 0; i < N; ++i)
		if (a[i] == INV) {
			a[i + 1] = INV;
		} else {
			ll u = a[i] / gcd(a[i], p[i]), v = p[i];
			if (H / u < v || u * v > H)
				a[i + 1] = INV;
			else
				a[i + 1] = u * v;
		}

	b[N] = 0;
	for (ll i = N - 1; i >= 0; --i)
		b[i] = gcd(p[i], b[i + 1]);

	for (ll i = 0; i <= N; ++i) {
		if (i > 0 && i < N && p[i - 1] == p[i]) continue;

		ll lo = L, hi = H;
		if (i > 0) lo = max(lo, p[i - 1]);
		if (i + 1 < N) hi = min(hi, p[i]);
		if (lo > hi) continue;

		if (a[i] == INV || b[i] % a[i] != 0) continue;
		ll t = solve2(lo, hi, a[i], b[i]);
		if (t >= 0) return t;
	}
	return -1;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc) {
            cout << "Case #" << cc + 1 << ": ";
		    ll t = solve();
		   	if (t < 0) cout << "NO"; else cout << t;
			cout << endl;
	}
    return 0;
}
