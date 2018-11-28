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

int main() {
    int T;
    cin >> T;
    FOR(t,1,T) {
        double X,S,R,runtime;
        cin >> X >> S >> R >> runtime;
        int N;
        cin >> N;
        vector< pair<double,double> > chodniky;
        REP(n,N) {
            double b,e,w;
            cin >> b >> e >> w;
            chodniky.push_back( make_pair(w, e-b) );
            X -= e-b;
        }
        chodniky.push_back( make_pair(0,X) );
        sort( chodniky.begin(), chodniky.end() );
        double total_time = 0;
        REP(i,SIZE(chodniky)) {
            // za ako dlho ho prejdem behom?
            double t1 = chodniky[i].second / (chodniky[i].first + R);
            if (t1 <= runtime) {
                total_time += t1;
                runtime -= t1;
            } else {
                total_time += runtime;
                double presiel = runtime * (chodniky[i].first + R);
                runtime = 0;
                double ostava = chodniky[i].second - presiel;
                total_time += ostava / (chodniky[i].first + S);
            }
        }
        printf("Case #%d: %.15f\n",t,total_time);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
