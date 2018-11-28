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

int n, m;
vector<string> comp, quer;
vector<vector<int> > d;
int ans;

void outdata() {
	cout << ans << endl;
}

void solve() {
	d = vector<vector<int> >(n + 1, vector<int>(m + 1, 1000000000));
	forn(i, n) {
		d[i][0] = 0;
	}
    forn(q, m) {
		forn(i, n) forn(j, n) if (comp[j] != quer[q]) {
			d[j][q + 1] = min(d[j][q + 1], d[i][q] + (j != i));
		}
    }
    ans = d[0][m];
    forn(i, n) ans = min(ans, d[i][m]);
}

void readdata() {
	comp.clear();
	quer.clear();
	string s;
	cin >> n;
	forn(i, n) {
		do {
			getline(cin, s);
		} while (s.empty());
		comp.pb(s);
	}
	cin >> m;
	forn(i, m) {
		do {
			getline(cin, s);
		} while (s.empty());
		quer.pb(s);
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		readdata();
		solve();
		cout << "Case #" << i + 1 << ": "; 
		outdata();
	}
	return 0;
}
