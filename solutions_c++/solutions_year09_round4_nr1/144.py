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
vector<int> a;
int ans;

void outdata() {
    cout << ans << endl;
}

void solve() {
    ans = 0;
    forv(i, a) {
        int rj = i;
        for(int j = i; j < n; ++j) {
            if (a[j] <= i) {
                rj = j;
                break;
            }
        }
        while (rj > i) {
            swap(a[rj], a[rj - 1]);
            --rj;
            ++ans;
        }
    }
}

void readdata() {
    cin >> n;
    a.resize(n);
    forn(i, n) {
        a[i] = 0;
        string s;
        cin >> s;
        forn(j, n) if (s[j] == '1') {
            a[i] = j;
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
