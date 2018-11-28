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

int T, N, M, U[2100], V[2100], alive[2010];
vector< vector<int> > kusy;

int F[12];
int maxF;

bool skus(int kam) {
    if (kam == N ) {
        REP(i,SIZE(kusy)) {
            vector<bool> seen(maxF+1,false);
            REP(j,SIZE(kusy[i])) seen[ F[kusy[i][j]] ] = true;
            bool ok = true;
            FOR(f,1,maxF) ok &= seen[f];
            if (!ok) return false;
        }
        return true;
    } else {
        FOR(f,1,maxF) {
            F[kam] = f;
            if (skus(kam+1)) return true;
        }
        return false;
    }
}

int main() {
    cin >> T;
    FOR(t,1,T) {
        cin >> N >> M;
        REP(m,M) cin >> U[m];
        REP(m,M) cin >> V[m];
        REP(m,M) { --U[m]; --V[m]; alive[m]=1; }
        vector<int> obvod;
        REP(n,N) obvod.push_back(n);

        kusy.clear();
        vector< pair<int,int> > interface;

        REP(kolo,M) {
            int najlepsi = N+3, nid = -1;
            REP(m,M) if (alive[m]) {
                int x = find( obvod.begin(), obvod.end(), U[m] ) - obvod.begin();
                int y = find( obvod.begin(), obvod.end(), V[m] ) - obvod.begin();
                if (x > y) swap(x,y);
                if (y-x < najlepsi) { najlepsi=y-x; nid=m; }
                if (SIZE(obvod)-y+x < najlepsi) { najlepsi=SIZE(obvod)-y+x; nid=m; }
            }
            alive[nid] = 0;
            int x = find( obvod.begin(), obvod.end(), U[nid] ) - obvod.begin();
            int y = find( obvod.begin(), obvod.end(), V[nid] ) - obvod.begin();
            if (x > y) swap(x,y);
            if (y-x < SIZE(obvod)-y+x) {
                vector<int> toto = vector<int>( obvod.begin()+x, obvod.begin()+y+1 );
                kusy.push_back(toto);
                obvod.erase( obvod.begin()+x+1, obvod.begin()+y );
            } else {
                vector<int> toto1 = vector<int>( obvod.begin()+y, obvod.end() );
                vector<int> toto2 = vector<int>( obvod.begin(), obvod.begin()+x+1 );
                toto1.insert( toto1.end(), toto2.begin(), toto2.end() );
                kusy.push_back(toto1);
                obvod = vector<int>( obvod.begin()+x, obvod.begin()+y+1 );
            }
        }
        kusy.push_back( obvod );
        maxF = 2;
        while (skus(0)) ++maxF;
        --maxF;
        skus(0);
        printf("Case #%d: %d\n",t,maxF);
        REP(n,N) printf("%d%s",F[n],(n==N-1) ? "\n" : " ");
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
