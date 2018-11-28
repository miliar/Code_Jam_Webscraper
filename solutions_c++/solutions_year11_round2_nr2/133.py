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

bool check(const vector<long long>& a, long long t, long long d)
{
    long long lp = a[0] - t;
    forv(i, a) if (i > 0) {
        long long rd = lp + d;
        long long cnp = max(rd, a[i] - t);
        if (abs(cnp - a[i]) > t) return false;
        lp = cnp;
    }
    return true;
}

void readdata() {
    long long n, d;
    cin >> n >> d;
    d *= 2;
    vector<long long> a;
    forn(i, n) {
        int k, pos;
        cin >> pos >> k;
        forn(_, k) a.pb(pos * 2);
    }
    sort(all(a));
    long long l = 0, r = (long long)(1e+15);
    while (l < r) {
        long long m = (l + r) / 2;
        if (check(a, m, d)) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    printf("%0.2lf\n", r * 0.5);
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


