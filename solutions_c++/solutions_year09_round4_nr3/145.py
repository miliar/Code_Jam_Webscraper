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

int n, k;
vector< vector<int> > a;
vector< vector<bool> > g;
vector<bool> u;
vector<int> m;
int ans;

void outdata() {
    cout << ans << endl;
}

bool go(int v) {
    if (u[v]) return false;
    u[v] = true;
    forv(i, g[v]) if (g[v][i]) {
        if (m[i] == -1 || go(m[i])) {
            m[i] = v;
            return true;
        }
    }
    return false;
}

bool major(vector<int>& a, vector<int>& b) {
    forv(i, a) if (a[i] <= b[i]) return false;
    return true;
}

void solve() {
    g = vector<vector<bool> >(n, vector<bool>(n, false));
    forn(i, n) forn(j, n) if (major(a[i], a[j])) {
        g[i][j] = true;
    }

    ans = 0;
    u.resize(n);
    m = vector<int>(n, -1);
    forn(i, n) {
        fill(all(u), false);
        if (go(i)) ++ans;
    }
    ans = n - ans;
}

void readdata() {
    cin >> n >> k;
    a.resize(n);
    forn(i, n) {
        a[i].resize(k);
        forn(j, k) {
            cin >> a[i][j];
        }
    }
}

int main() {
    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ": ";
        readdata();
	    solve();
    	outdata();
    }
	return 0;
}
