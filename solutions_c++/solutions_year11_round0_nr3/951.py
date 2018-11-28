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
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int T, N, C[1024];
#define M 1048576
int best[M], nbest[M];

int main() {
    cin >> T;
    REP(t,T) {
        cin >> N;
        REP(n,N) cin >> C[n];
        int x = 0;
        REP(n,N) x ^= C[n];
        int s = 0;
        REP(n,N) s += C[n];
        if (x != 0) { printf("Case #%d: NO\n",t+1); continue; }
        memset(best,-1,sizeof(best));
        best[0]=0;
        REP(n,N) {
            memcpy(nbest,best,sizeof(best));
            REP(m,M) if (best[m] != -1) nbest[m ^ C[n]] = max( nbest[m ^ C[n]], best[m] + C[n] );
            memcpy(best,nbest,sizeof(best));
        }
        int ans = -1;
        REP(m,M) if (best[m]!=s && best[m]>ans) ans=best[m];
        if (ans==-1) {
            printf("Case #%d: NO\n",t+1);
        } else {
            printf("Case #%d: %d\n",t+1,ans);
        }
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
