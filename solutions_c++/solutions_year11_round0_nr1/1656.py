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

int move(int a, int b, int w) {
    int res = abs(a - b) - w;
    return max(res, 0) + 1;
}

void readdata() {
    int k;
    cin >> k;
    int op = 1, bp = 1, bw = 0, ow = 0;
    int ans = 0;
    forn(i, k) {
        string C;
        int m;
        cin >> C >> m;
        if (C == "B") {
            int go = move(bp, m, bw);
            bw = 0;
            ow += go;
            ans += go;
            //cerr << "b " << go << endl;
            bp = m;
        } else {
            int go = move(op, m, ow);
            ow = 0;
            bw += go;
            ans += go;
            op = m;
            //cerr << "o " << go << endl;
        }
    }
    cout << ans << endl;
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
