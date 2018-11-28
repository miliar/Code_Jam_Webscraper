#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:30000000")

#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8
const int INF = (int)1E+9;

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define PII pair<int, int>
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())
typedef long long int64;

int n, k;
const int NMAX = 530;
vector<int> g[NMAX];
int p[NMAX];
int64 ans;
int64 mod = 1000000009;

void outdata() {
	cout << ans % mod << endl;
}

int64 calc(int x, int y) {
	if (x > y) return 0;
	int64 res = 1;
	forn(i, x) res = (res * (y - i) ) % mod;
	return res;
}

void go(int v, int par) {
	p[v] = par;
	ans = (ans * calc((int)g[v].size() - (par != 0), k - (int)g[par].size())) % mod;
	forv(i, g[v]) if (g[v][i] != par) {
		go(g[v][i], v);
	}
}

void solve() {
	ans = 1;
	go(1, 0);
}

void readdata() {
	cin >> n >> k;
	forn(i, n + 1) g[i].clear();
	forn(i, n - 1) {
		int x, y;
		cin >> x >> y;
		g[x].pb(y);
		g[y].pb(x);
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		cerr << i + 1 << endl;
		readdata();
		solve();
		outdata();
	}
	return 0;
}

