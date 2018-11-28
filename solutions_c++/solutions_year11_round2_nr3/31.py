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

int n, m, x[3000], y[3000], ans[3000], C, ii;
vector<int> g[3000], g2[3000];
bool u[3000];

void read() {
	scanf("%d%d", &n, &m);
	forn(i, m) {
		scanf("%d", &x[i]);
		x[i]--;
	}
	forn(i, m) {
		scanf("%d", &y[i]);
		y[i]--;
	}
}

vector<vector<int> > cmp;

void paint(const vector<int> &v) {
	vector<char> have(C, 0);
	int s;
	forn(i, v.size())
		if (ans[v[i]] != -1) {
			have[ans[v[i]]] = 1;
			s = i;
		}

	if (s == (int)v.size() - 1 && ans[v[v.size() - 2]] == -1)
		s = 0;

	int p = 0;
	forn(i, v.size() - 2) {
		s = (s + 1) % int(v.size());
		if (ans[v[s]] != -1)
			throw;

		while (p < C && have[p])
			p++;
		if (p < C) {
			ans[v[s]] = p;
			have[p] = 1;
		}
		else {
			int ps = (s + (int)v.size() - 1) % int(v.size());
			while (p % C == ans[v[ps]])
				p++;

			ans[v[s]] = p % C;
			p++;
		}
	}

	int ns = (s + 1) % int(v.size());
	int ps = (s + (int)v.size() - 1) % int(v.size());
	while (ans[v[s]] == ans[v[ns]] || ans[v[s]] == ans[v[ps]])
		ans[v[s]] = (ans[v[s]] + 1) % C;

	/*

	int p = 0;
	forn(i, v.size())
		if (ans[v[i]] == -1) {
			while (p < C && have[p])
				p++;
			if (p < C) {
				ans[v[i]] = p;
				have[p] = 1;
			}
			else {
				ans[v[i]] = p % C;
				p++;
			}
		}
	*/

	p = 0;
	while (p < C && have[p])
		p++;
	if (p < C)
		throw;
}

void dfs(int v) {
	u[v] = true;

	forn(i, g2[v].size()) {
		int to = g2[v][i];
		if (u[to])
			continue;

		paint(cmp[to]);
		dfs(to);
	}
}

void gen() {
	n = 10;
	m = 1;
	forn(i, m) {
		x[i] = 2 * i;
		y[i] = 2 * i + 1;
	}
}

void solve() {
	read();
	//gen();

	forn(i, n) {
		g[i].clear();
		g2[i].clear();
	}

	forn(i, m) {
		if (x[i] > y[i])
			swap(x[i], y[i]);
		g[y[i]].pb(x[i]);
	}

	vector<int> st;
	cmp.clear();
	forn(i, n) {
		sort(all(g[i]));

		ford(j, g[i].size()) {
			vector<int> cur;
			while (g[i][j] != st.back()) {
				cur.pb(st.back());
				st.pop_back();
			}

			cur.pb(g[i][j]);
			cur.pb(i);

			cmp.pb(cur);
		}

		st.pb(i);
	}

	cmp.pb(st);

	map<pair<int, int>, int> ma;
	int root = 0;
	forn(i, cmp.size()) {
		forn(j, cmp[i].size()) {
			int v1 = cmp[i][j];
			int v2 = cmp[i][(j + 1) % int(cmp[i].size())];

			if (v1 > v2)
				swap(v1, v2);

			if (ma.count(mp(v1, v2))) {
				g2[i].pb(ma[mp(v1, v2)]);
				g2[ma[mp(v1, v2)]].pb(i);
			}
			else
				ma[mp(v1, v2)] = i;
		}

		if (cmp[i].size() < cmp[root].size())
			root = i;
	}

	memset(ans, -1, sizeof(ans));
	forn(i, cmp[root].size())
		ans[cmp[root][i]] = i;

	memset(u, 0, sizeof(u));
	C = (int)cmp[root].size();
	dfs(root);

	printf("%d\n", cmp[root].size());
	forn(i, n)
		printf(i ? " %d" : "%d", ans[i] + 1);
	puts("");
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		cerr << ii << endl;
		::ii = ii;
		printf("Case #%d: ", ii + 1);
		solve();
	}
	
	return 0;
}