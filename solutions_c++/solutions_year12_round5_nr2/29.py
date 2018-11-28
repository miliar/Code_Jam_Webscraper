#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

const int dx[6] = {0, -1, -1, 0, 1, 1};
const int dy[6] = {1, 0, -1, -1, 0, 1};

int cor[110000], ed[110000], x[110000], y[110000], s, m, id[110000], p[110000], t[110000];
vector<string> nans;
vector<pair<int, int> > v;
bool fork, bridge, ring;
vector<pair<int, int> > corns;
int ans;

void read() {
	cin >> s >> m;
	forn(i, m)
		scanf("%d%d", &x[i], &y[i]);
}

vector<int> get_ne(int cur) {
	vector<int> res;
	forn(dir, 6) {
		int nx = v[cur].fs + dx[dir];
		int ny = v[cur].sc + dy[dir];

		int pos = int(lower_bound(all(v), mp(nx, ny)) - v.begin());
		if (pos < (int)v.size() && v[pos] == mp(nx, ny))
			res.pb(pos);
		else
			res.pb(-1);
	}
	return res;
}

bool is_corner(pair<int, int> v) {
	return binary_search(all(corns), v);
}

int get(int v) {
	return p[v] == v ? v : p[v] = get(p[v]);
}

int edge(pair<int, int> v) {
	if (v.sc == 1)
		return 1 << 0;
	if (v.fs == 1)
		return 1 << 1;
	if (v.fs == 2 * s - 1)
		return 1 << 2;
	if (v.sc == 2 * s - 1)
		return 1 << 3;
	if (v.fs - v.sc == s - 1)
		return 1 << 4;
	if (v.fs - v.sc == -s + 1)
		return 1 << 5;
	return 0;
}

void merge(int v1, int v2) {
	v1 = get(v1);
	v2 = get(v2);
	if (v1 != v2) {
		p[v1] = v2;
		cor[v2] += cor[v1];
		ed[v2] |= ed[v1];
	}
}

void check(int v) {
	v = get(v);

	if (cor[v] >= 2)
		bridge = true;
	int cnt = 0;
	forn(i, 6)
		if (ed[v] & (1 << i))
			cnt++;
	if (cnt >= 3)
		fork = true;
}

void f() {
	nans.clear();
	v.clear();
	forn(i, m)
		v.pb(mp(x[i], y[i]));
	sort(all(v));

	ring = false, bridge = false, fork = false;
	forn(i, m) {
		id[i] = int(lower_bound(all(v), mp(x[i], y[i])) - v.begin());
		t[id[i]] = i;
	}

	forn(i, m) {
		p[i] = i;
		cor[i] = ed[i] = 0;
		if (is_corner(v[i]))
			cor[i]++;
		else
			ed[i] = edge(v[i]);
	}

	forn(i, m) {
		vector<int> g = get_ne(id[i]);
		forn(j, g.size())
			if (g[j] != -1 && t[g[j]] >= i)
				g[j] = -1;
		forn(j, g.size())
			if (g[j] != -1)
				g[j] = get(g[j]);
		forn(j, g.size())
			if (g[j] != -1) {
				int l = 1, r = 5;
				while (g[(j + l) % 6] == g[j])
					l++;
				while (g[(j + r) % 6] == g[j])
					r--;
				
				for (int t = l; t <= r; t++)
					if (g[(j + t) % 6] == g[j])
						ring = true;
			}

		forn(j, g.size())
			if (g[j] != -1)
				merge(id[i], g[j]);

		check(id[i]);
		if (ring || bridge || fork) {
			ans = i;
			break;
		}
	}

	if (ring)
		nans.pb("ring");
	if (bridge)
		nans.pb("bridge");
	if (fork)
		nans.pb("fork");
}

void solve() {
	corns.clear();
	corns.pb(mp(1, 1));
	corns.pb(mp(s, 1));
	corns.pb(mp(1, s));
	corns.pb(mp(2 * s - 1, 2 * s - 1));
	corns.pb(mp(s, 2 * s - 1));
	corns.pb(mp(2 * s - 1, s));
	sort(all(corns));

	f();

	if (nans.empty())
		puts("none");
	else {
		sort(all(nans));
		forn(i, nans.size())
			printf(i ? "-%s" : "%s", nans[i].c_str());
		printf(" in move %d\n", ans + 1);
	}
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
	
	int tt;
	cin >> tt;
	forn(ii, tt) {
		cerr << ii << "/" << tt << ' ' << clock() << endl;
		read();
		printf("Case #%d: ", ii + 1);
		solve();
	}

	cerr << tt << "/" << tt << ' ' << clock() << endl;
	
	return 0;
}