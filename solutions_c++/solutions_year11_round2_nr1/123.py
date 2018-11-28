// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int T, N;
vector<string> R;

double getWP(int tim, int skip=-1) {
    int good=0, all=0;
    REP(n,N) {
        if (n==skip) continue;
        if (R[tim][n]=='.') continue;
        ++all;
        if (R[tim][n]=='1') ++good;
    }
    return 1.*good/all;
}

int main() {
    cin >> T;
    FOR(t,1,T) {
        cin >> N;
        R.clear();
        REP(n,N) { string line; cin >> line; R.push_back(line); }
        vector<double> WP(N);
        REP(n,N) WP[n] = getWP(n);
        vector<double> OWP(N,0.);
        REP(n,N) {
            int opp=0;
            REP(i,N) if (R[n][i]!='.') { ++opp; OWP[n] += getWP(i,n); }
            OWP[n] /= opp;
        }
        vector<double> OOWP(N,0.);
        REP(n,N) {
            int opp=0;
            REP(i,N) if (R[n][i]!='.') { ++opp; OOWP[n] += OWP[i]; }
            OOWP[n] /= opp;
        }
        printf("Case #%d:\n",t);
        REP(n,N) printf("%.12f\n",0.25*WP[n] + 0.50*OWP[n] + 0.25*OOWP[n]);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
