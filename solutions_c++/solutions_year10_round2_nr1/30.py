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
set<string> ex;
int ans;

void outdata() {
}

void solve() {
}

void readdata() {
    cin >> n >> m;
    ex.clear();
    ex.insert("");
    forn(ii, n) {
        string s, cs;
        cin >> s;
        s += "/";
        fors(i, s) {
            if (s[i] == '/') {
                ex.insert(cs);
            }
            cs.push_back(s[i]);
        }
    }
    ans = 0;
    forn(ii, m) {
        string s, cs;
        cin >> s;
        s += "/";
        fors(i, s) {
            if (s[i] == '/') {
                ans += ex.insert(cs).second;
            }
            cs.push_back(s[i]);
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
