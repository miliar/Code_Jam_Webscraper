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
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int T;
long long D;
int C;
vector<long long> X;

bool dasa(double cas) {
    double kde = X[0]-cas;
    for (int i=1; i<SIZE(X); ++i) {
        kde += D;
        if (kde > X[i]+cas) return false;
        if (kde < X[i]-cas) kde = X[i]-cas;
    }
    return true;
}

int main() {
    cin >> T;
    FOR(t,1,T) {
        cin >> C >> D;
        X.clear();
        REP(c,C) {
            int x, v; cin >> x >> v;
            while (v--) X.push_back(x);
        }

        if (SIZE(X)==0) {
            printf("Case #%d: %.12f\n",t,0.);
            continue;
        }

        double lo=0, hi=1e20;
        REP(loop,1000) {
            double med = (lo+hi)/2;
            if (dasa(med)) hi=med; else lo=med;
        }
        printf("Case #%d: %.12f\n",t,hi);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
