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
int f, t;
int ans;

void outdata() {
}

void solve() {
}

void readdata() {
    cin >> n >> m >> f >> t;
    vector<int> x(n), v(n);;
    forn(i, n) {
        cin >> x[i];
    }
    forn(i, n) {
        cin >> v[i];
    }
    int ko = 0, get = 0;
    ans = 0;
    forn(i, n) if (get < m) {
        if (f - x[n - 1 - i] <= v[n - 1 - i] * t) {
            ans += ko;
            ++get;
        } else {
            ++ko;
        }
    }
    if (get == m) {
        cout << ans << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ": ";
        readdata();
        solve();
    }
	return 0;
}
