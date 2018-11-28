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

string p = "welcome to code jam";
string s;

void outdata() {
}

void solve() {
    vector<vector<int> > d(s.length() + 1, vector<int>(p.length() + 1));
    d[0][0] = 1;
    fors(i, s) {
        d[i + 1] = d[i];
        fors(j, p) {
            if (p[j] == s[i]) {
                d[i + 1][j + 1] += d[i][j];
                d[i + 1][j + 1] %= 10000;
            }
        }
    }
    printf("%0.4d\n", d[s.length()][p.length()]);
}

void readdata() {
    getline(cin, s);
}

int main() {
    int tst;
    cin >> tst;
    string s;
    getline(cin, s);
    forn(i, tst) {
        printf("Case #%d: ", i + 1);
    	readdata();
        solve();
    	outdata();
    }
	return 0;
}
