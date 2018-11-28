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

const int NMAX = 11;

int n, m;
vector<string> s;
vector<int> br;
int d[3 + NMAX][1 << NMAX];
int ans;

void outdata() {
	cout << ans << endl;
}

void solve() {
	memset(d, 255, sizeof d);
	d[0][0] = 0;
	forn(t, n + 1) {
		forn(mprev, 1 << m) {
			if (d[t][mprev] == -1) continue;
    		forn(msk, 1 << m) {
    			if ((msk & br[t]) != 0) {
    				continue;
    			}
    			bool ok =  true;
    			forn(i, m) if (i > 0 && (msk & (1 << i)) && (msk & (1 << (i - 1)))) {
    				ok = false;
    				break;
    			}
    			if (!ok) continue;
    			forn(i, m) if (i > 0 && (msk & (1 << i)) && (mprev & (1 << (i - 1)))) {
    				ok = false;
    				break;
    			}
    			if (!ok) continue;
    			forn(i, m) if (i < m - 1 && (msk & (1 << i)) && (mprev & (1 << (i + 1)))) {
    				ok = false;
    				break;
    			}
    			if (!ok) continue;
    			int kadd = 0;
    			forn(i, m) if (msk & (1 << i)) ++kadd;
    			d[t + 1][msk] = max(d[t + 1][msk], d[t][mprev] + kadd);
    		}
		}
	}
	ans = d[n + 1][0];
}

void readdata() {
	cin >> n >> m;
	s.resize(n);
	forn(i, n) cin >> s[i];
	br.resize(n);
	forn(i, n) {
		int msk = 0;
		forn(q, m) if (s[i][q] == 'x') {
			msk ^= (1 << q);
		}
		br[i] = msk;
	}
	br.pb((1 << m) - 1);
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
