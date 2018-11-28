#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

int n, m, r;
int d[200][200];
int e[200][200];
const int mod = 10007;
int ans;

void outdata() {
	cout << ans << endl;
}

void solve() {
	d[0][0] = (1 - e[0][0]);
	forn(i, n) forn(j, m) if (i + j > 0) {
		if (e[i][j]) continue;
		if (i > 0 && j > 1) d[i][j] += d[i - 1][j - 2];
		if (i > 1 && j > 0) d[i][j] += d[i - 2][j - 1];
		d[i][j] %= mod;
	}
	ans = d[n - 1][m - 1] % mod;
}

void readdata() {
	memset(d, 0, sizeof d);
	memset(e, 0, sizeof e);
	cin >> n >> m >> r;
	forn(i, r) {
		int x, y;
		cin >> x >> y;
		--x, --y;
		e[x][y] = true;
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		cerr << i << endl;
		readdata();
		solve();
		outdata();
	}
	return 0;
}
