#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <cstring>
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

void solve() {
}

void readdata() {
    int n;
    cin >> n;
    int sum = 0, mn = 100000000, xr = 0;
    forn(i, n) {
        int x;
        cin >> x;
        sum += x;
        mn = min(mn, x);
        xr = (xr ^ x);
    }
    if (xr == 0) cout << sum - mn; else cout << "NO";
    cout << endl;
}


int main() {
    int t;          
    cin >> t;
    forn(i, t) {
        cout << "Case #" << i + 1 << ": ";
    	readdata();
	    solve();
    	outdata();
    }
	return 0;
}
