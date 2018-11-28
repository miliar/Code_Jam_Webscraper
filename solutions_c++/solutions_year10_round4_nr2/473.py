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

int k, n, p;
int m[2000];
int c[20][2000];
int res[20][2000][20];
int result;

void outdata() {
}

void solve() {
}

const int INF = (int)1e+9;

int calc(int r, int g, int km) {
	if (r < 0) {
		return m[g] >= km ? 0 : INF;
	}
    int& ans = res[r][g][km];
    if (ans != -1) return ans;
    ans = calc(r - 1, g * 2, km + 1) + calc(r - 1, g * 2 + 1, km + 1);
    if (ans > INF) ans = INF;
    ans = min(ans, calc(r - 1, g * 2, km) + calc(r - 1, g * 2 + 1, km) + c[r][g]);
    return ans;
}

void readdata() {
    cin >> p;
    forn(i, 1 << p) cin >> m[i];
    forn(t, p) {
        forn(i, 1 << (p - t - 1))
            cin >> c[t][i];
    }
    memset(res, 255, sizeof res);
    result = calc(p - 1, 0, 0);
}

int main() {
    int tst;
    cin >> tst;
    forn(i, tst) {
        readdata();
        solve();
        cout << "Case #" << i + 1 << ": " << result << endl;
    }
	return 0;
}
