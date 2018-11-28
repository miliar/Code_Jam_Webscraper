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
const int MOD = 100003;
const int NMAX = 1000;

long long d[NMAX][NMAX];
long long c[NMAX][NMAX];

long long C(int i, int j) {
	if (i < j) return 0;
	if (j == 0) return 1;
    if (c[i][j] != -1) return c[i][j];
	return c[i][j] = (C(i - 1, j - 1) + C(i - 1, j)) % MOD;
}

long long calc(int i, int j) {
    if (d[i][j] != -1) return d[i][j];
    long long& res = d[i][j];
    if (i == 1) return res = 1;
    res = 0;
    forn(k, min(i - 1, j - i)) {
        res = (res + calc(i - k - 1, i) * C(j - i - 1, k)) % MOD;
    }
    return res;
}

void readdata() {
    long long ans = 0;
    cin >> n;
    forn(i, n - 1) ans = (ans + calc(i + 1, n)) % MOD;
    cout << ans << endl;
}

int main() {
    memset(d, 255, sizeof(d));
    memset(c, 255, sizeof(c));
    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ": ";
        readdata();
    }
	return 0;
}
