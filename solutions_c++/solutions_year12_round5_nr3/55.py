#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

ll T, M, F, N;
pair<ll, ll> food[300];
vector<pair<ll, ll> > opts;

ll getval(ll x) {
	if (opts[sz(opts)-1].second < x-1) return M+1;
	ll res = 0;
	FOR(i, 0, sz(opts)) {
		if (opts[i].second >= x-1) {
			ll pr = (i == 0) ? (-1) : opts[i-1].second;
			if ((x - 1 - pr) > M/opts[i].first) return M+1; 
			res += (x - 1 - pr) * opts[i].first;
			if (res > M) return M+1;
			break;
		}
		ll pr = (i == 0) ? (-1) : opts[i-1].second;
		if ((opts[i].second - pr) > M/opts[i].first) return M+1; 
		res += (opts[i].second - pr) * opts[i].first;
		if (res > M) return M+1;
	}
	return res;
}

ll get_cost(ll n, ll d) {
	if (d > M/F) return 4*M - (M - n);
	ll f = d*F;
	ll x = n/d;
	ll n2 = n - x*d;
	ll n1 = d - n2;
	ll p1 = getval(x), p2 = getval(x+1);
	if (p1 > M || (n2 > 0 && p2 > M)) return 4*M - n;
	if (n1 > M/p1 || (n2 > 0 && n2 > M/p2)) {
		if (n1+n2 > p1+p2) {
			return 4*M - (M - n);
		} else {
			return 4*M - n;
		}
	}
	ll v1 = n1*p1;
	ll v2 = n2*p2;
	return f + v1 + v2;
}

ll calc_opt(ll n) {
	ll a = 1, b = n;
	while (1) {
		if (b-a < 1000000) {
			ll res = M+1;
			FOR(i, a, b+1) res = min(res, get_cost(n, i));
			return res;
		}
		ll m1 = a + (b-a)/3, m2 = a + 2*((b-a)/3);
		ll v1 = get_cost(n, m1), v2 = get_cost(n, m2);
		if (v1 < v2) {
			b = m2;
		} else {
			a = m1;
		}
	}
	return -1;
}

bool check(ll n) {
	if (n == 0) return true;
	ll opt = calc_opt(n);
	return (opt <= M);
}

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		opts.clear();
		cin >> M >> F >> N;
		FOR(i, 0, N) cin >> food[i].first >> food[i].second;
		sort(food, food + N);
		ll tm = 0;
		FOR(i, 0, N) {
			int ii = i;
			while (ii+1 < N && food[ii+1].first == food[i].first) ii++;
			ll s = 0;
			FOR(j, i, ii+1) s = max(s, food[j].second);
			i = ii;
			if (s < tm) continue;
			opts.push_back(make_pair(food[i].first, s));
			tm = s+1;
		}
		ll a = 0, b = M;
		while (a < b) {
			ll m = (a + b + 1) / 2;
			if (check(m)) {
				a = m;
			} else {
				b = m-1;
			}
		}
		cout << "Case #" << cs << ": " << a << endl;
	}
	return 0;
}
