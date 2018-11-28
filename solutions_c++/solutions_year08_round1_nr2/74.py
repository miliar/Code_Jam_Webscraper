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

const int NMAX = 3000;

int n, m;
vector<int> g[NMAX], tp[NMAX], res;
bool aok;
int ed[NMAX];

void outdata() {
	if (!aok) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		forn(i, n) {
			if (i > 0) cout << " ";
			cout << res[i];
		}
		cout << endl;
	}
}

int bit(int x) {
	int res = 0;
	while (x) {
		res += (x & 1);
		x >>= 1;
	}
	return res;
}

void solve() {
	vector<int> msk(n, 0);
	aok = false;
	forn(iter, m * 2) {
		vector<bool> ok(m, false);
		bool gok = true;
		forn(i, m) {
			forv(j, g[i]) {
				if (msk[g[i][j]] == tp[i][j]) {
					ok[i] = true;
					break;
				}
			}
			if (!ok[i]) {
				gok = false;
			}
		}
		if (gok) {
			res = msk;
			aok = true;
			break;
		}
		forn(i, m) {
			if (!ok[i]) {
				if (ed[i] != -1) msk[ed[i]] = 1;
			}
		}
	}
}

void readdata() {
	cin >> n >> m;
	forn(i, m) {
		int t;
		cin >> t;
		g[i].clear();
		tp[i].clear();
		ed[i] = -1;
		forn(j, t) {
			int x, y;
			cin >> x >> y;
			g[i].pb(x - 1);
			tp[i].pb(y);
			if (y == 1) ed[i] = x - 1;
		}
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		cerr << "Case #" << i + 1 << ": \n";
		readdata();
		solve();
		outdata();
	}
	return 0;
}
