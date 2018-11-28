#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define one(x,i) ((x) >> (i) & 1)

int n, m;
vector <int> a[2222];
vector < vector <int> > s;
int init;
bool good[2222];
bool was[2222];
int c[2222];
int u[2222];
int v[2222];

void dfs(int v, int m, int k = 0) {
	if (k == m && v == init) {
		vector <int> a;
		for (int i = 0; i < n; ++i)
			if (good[i]) a.pb(i);
		s.pb(a);
		return;
	}
	if (was[v]) return;
	was[v] = true;
	for (int i = 0; i < sz(a[v]); ++i)
		if (good[a[v][i]]) dfs(a[v][i], m, k + 1);
}

bool rec(int k, int m) {
	if (k == n) {
		for (int i = 0; i < sz(s); ++i) {
			set <int> st;
			for (int j = 0; j < sz(s[i]); ++j) st.insert(c[s[i][j]]);
			if (sz(st) != m) return false;
		}
		return true;
	}
	for (int i = 1; i <= m; ++i) {
		c[k] = i;
		if (rec(k + 1, m)) return true;
		c[k] = 0;
	}
	return false;
}

void solve(int testcase)
{
	printf("Case #%d: ", testcase);
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i) a[i].clear();
	s.clear();
	for (int i = 0; i < n - 1; ++i) {
		a[i].pb(i + 1);
		a[i + 1].pb(i);
	}
	a[n - 1].pb(0);
	a[0].pb(n - 1);
	for (int i = 0; i < m; ++i) scanf("%d", &u[i]);
	for (int i = 0; i < m; ++i) scanf("%d", &v[i]);
	for (int i = 0; i < m; ++i) {
		--u[i], --v[i];
		a[u[i]].pb(v[i]);
		a[v[i]].pb(u[i]);
	}
	for (int p = 0; p < 1 << n; ++p) {
		if (__builtin_popcount(p) < 3) continue;
		for (int i = 0; i < n; ++i)
			if (one(p, i)) good[i] = true; else good[i] = false;
		for (int i = 0; i < n; ++i)
			if (good[i]) {
				init = i;
				for (int j = 0; j < n; ++j) was[j] = false;
				dfs(i, __builtin_popcount(p));
				break;
			}
	}
// 	for (int i = 0; i < sz(s); ++i) {
// 		for (int j = 0; j < sz(s[i]); ++j) cout << s[i][j] << " ";
// 		cout << endl;
// 	}
	int res = -1;
	for (int i = 1; i <= n; ++i)
		if (!rec(0, i)) {
			res = i - 1;
			break;
		}
	rec(0, res);
	printf("%d\n", res);
	for (int i = 0; i < n; ++i)
		printf("%d%c", c[i], " \n"[i + 1 == n]);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
