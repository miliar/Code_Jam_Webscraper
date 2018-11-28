#define FILENAME "a"

#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string.h>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CTO500 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()
#define VI vector<int>
#define VII vector<VI >
#define CL(a,b) memset(a,b,sizeof(a))  
#define UN(v) SORT(v),v.erase(unique(ALL(v)),v.end())  

typedef pair<int, int> PII;
typedef long long i64; 

void init(string file) {
    string ifile = file + ".in";
    string ofile = file + ".out";
	freopen(ifile.c_str(), "rt", stdin);
	freopen(ofile.c_str(), "wt", stdout);
}

void move(int dest, int& x) {
    if (dest > x) ++x; else if (dest < x) --x;
}

void solve() {
    int tests; cin >> tests;
    REP(test,tests){
        int n; cin >> n;
        string s; int m;
        vector<PII > a, b;
        REP(i,n){
            cin >> s >> m;
            if (s == "O") a.pb(PII(i,m)); else b.pb(PII(i,m));
        }
        a.pb(PII(n,CTO500));
        b.pb(PII(n,CTO500));
        int ac = 0, bc = 0, ax = 1, bx = 1;
        int i = 0, res = 0;
        while (i < n) {
            ++res;
            if (a[ac].X == i && a[ac].Y == ax) {
                ++i, ++ac; 
                move(b[bc].Y, bx);
            }
            else if (b[bc].X == i && b[bc].Y == bx) {
                ++i, ++bc; 
                move(a[ac].Y, ax);
            } else {
                move(a[ac].Y, ax);
                move(b[bc].Y, bx);
            }
        }
        printf("Case #%d: %d\n", test+1, res);
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
