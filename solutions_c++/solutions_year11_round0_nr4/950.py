// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
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

int main() {
    cin >> T;
    FOR(t,1,T) {
        cin >> N;
        int x;
        vector<int> start;
        int ans=0;
        REP(n,N) { cin >> x; --x; if (x!=n) ++ans; }
        printf("Case #%d: %d\n",t,ans);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
