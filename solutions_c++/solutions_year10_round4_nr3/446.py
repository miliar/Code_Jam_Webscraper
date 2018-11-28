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

typedef pair<int, int> point;
typedef map<point, int> ps;

int n;
const int NMAX = 111;
int c[NMAX][NMAX];
int nc[NMAX][NMAX];
int ans;

void outdata() {
}

bool fin()
{
    forn(i, NMAX) forn(j, NMAX) if (c[i][j] == 1) return false;
    return true;
}

bool print()
{
	forn(i, 5) {
		forn(j, 5) {
			cout << c[i][j];
		}
		cout << endl;
	}
    return true;
}

void solve() {
    ans = 0;
    while (!fin()) {
        forn(i, NMAX) forn(j, NMAX) {
			nc[i][j] = c[i][j];
            if (i == 0 || j == 0) {
                continue;
            }
            if (c[i][j] == 1) {
                if (c[i - 1][j] == 0 && c[i][j - 1] == 0) {
                    nc[i][j] = 0;
                }
            } else {
                if (c[i - 1][j] == 1 && c[i][j - 1] == 1) {
                    nc[i][j] = 1;
                }
            }
        }
        ++ans;
		memmove(c, nc, sizeof c);
    }
}

void readdata() {
    memset(c, 0, sizeof c);
    cin >> n;
    forn(t, n) {
        int xl, xr, yl, yr;
        cin >> xl >> yl >> xr >> yr;
        for(int i = xl; i <= xr; ++i) {
            for(int j = yl; j <= yr; ++j) {
                c[i][j] = 1;
            }
        }
    }
}

int main() {
    int tst;
    cin >> tst;
    forn(i, tst) {
        readdata();
        solve();
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
	return 0;
}
