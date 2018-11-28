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

int n;
vector<int> x, y, r;
double ans;

void outdata() {
    printf("%0.10lf\n", ans);
}

double calc(int i, int j) {
    double d = hypot(x[i] - x[j], y[i] - y[j]);
    return (d + r[i] + r[j]) * 0.5;
}

void solve() {
    if (n == 1) {
        ans = r[0];
        return ;
    }
    if (n == 2) {
        ans = max(r[0], r[1]);
        return ;
    }
    if (n == 3) {
        ans = 1e+100;
        forn(i, 3) forn(j, i) {
            int t = 3 - i - j;
            ans = min(ans,
                max((double)r[t], calc(i, j)));
        }
    }
}

void readdata() {
    cin >> n;
    x.resize(n);
    y.resize(n);
    r.resize(n);
    forn(i, n) {
        cin >> x[i] >> y[i] >> r[i];
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
