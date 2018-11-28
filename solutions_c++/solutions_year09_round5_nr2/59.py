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

void outdata() {
}

const int MOD = 10009;

typedef vector<int> nums;
vector<nums> a;
int n, K;
string pol;
int res[12];

int eval(string& p, nums& k) {
    int m = 1;
    int res = 0;
    fors(i, p) {
        if (p[i] == '+' || p[i] == '=') {
            res = (res + m) % MOD;
            m = 1;
        } else {
            m = m * k[p[i] - 'a'] % MOD;
        }
    }
    return res % MOD;
}

void add(nums& a, nums& b, int zn) {
    forv(i, a) a[i] += zn * b[i];
}

int fac[10];

void rec(int p, int k, int mul, nums& cur) {
    if (p >= a.size()) {
        res[k] = (res[k] + eval(pol, cur) * fac[k] / mul) % MOD;
        return ;
    }
    rec(p + 1, k, mul, cur);
    int cmul = 1;
    for(int i = 1; k + i <= K; ++i) {
        cmul *= i;
        add(cur, a[p], i);
        rec(p + 1, k + i, mul * cmul, cur);
        add(cur, a[p], -i);
    }
}

void solve() {
    fac[0] = 1;
    forn(i, 10) if (i > 0) fac[i] = i * fac[i - 1];
    nums cur(26, 0);
    memset(res, 0, sizeof res);
    rec(0, 0, 1, cur);
    for(int i = 1; i <= K; ++i) {
        cout << " " << res[i];
    }
    cout << endl;
}

void readdata() {
    cin >> pol;
    pol += '=';
    cin >> K;
    cin >> n;
    a.clear();
    forn(i, n) {
        string s;
        cin >> s;
        nums x(26, 0);
        fors(j, s) {
            x[s[j] - 'a']++;
        }
        a.pb(x);
    }
}

int main() {
    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ":";
        readdata();
	    solve();
    	outdata();
    }
	return 0;
}
