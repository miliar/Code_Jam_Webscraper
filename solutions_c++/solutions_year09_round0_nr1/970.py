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

int l, n, tst;
vector<string> w;

void outdata() {
}

void solve() {
    forn(ii, tst) {
        string p;
        cin >> p;
        vector<int> msk(l);
        int pos = 0;
        forn(i, l) {
            msk[i] = 0;
            if (p[pos] == '(') {
                ++pos;
                while (p[pos] != ')') {
                    msk[i] |= (1 << (p[pos] - 'a'));
                    ++pos;
                }
                ++pos;
            } else {
                msk[i] = (1 << (p[pos] - 'a'));
                ++pos;
            }
        }
        int res = 0;
        forv(i, w) {
            string cw = w[i];
            bool ok = true;
            forn(t, l) {
                if ((msk[t] & (1 << (cw[t] - 'a'))) == 0) {
                    ok = false;
                    break;
                }
            }
            res += ok;
        }
        cout << "Case #" << 1 + ii << ": " << res << endl;
    }
}

void readdata() {
    cin >> l >> n >> tst;
    w.resize(n);
    forn(i, n) {
        cin >> w[i];
    }
}

int main() {
	readdata();
	solve();
	outdata();
	return 0;
}
