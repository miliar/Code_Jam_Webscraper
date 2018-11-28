#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;
const int MAXN = 105;

int n, m;
int d;
vector<pair<int, int> > p;

bool test(double m) {
	int i;
	double lx = -1e+13;
	for (i = 0; i < n; ++ i) {
		double lp = max(lx + d, p[i].first - m);
		double rp = lp + (p[i].second - 1) * d;
		double dd = rp - p[i].first;
		if (dd > m + 1e-10) {
			return false;
		}
		lx = rp;
	}
	return true;
}

void solve() {
	int i, j, k;
	scanf("%d", &n);
	scanf("%d", &d);
	p.clear();
	for (i = 0; i < n; ++ i) {
		int x, v;
		scanf("%d %d", &x, &v);
		p.pb(mp(x, v));
	}
	sort(all(p));
	double l = 0, r = 1e+13, m;
	for(i = 0; i < 100; ++ i) {
		m = (l + r) / 2;
		if (test(m)) {
			r = m;
		} else {
			l = m;
		}
	}
	printf("%.9lf\n", r); 
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}