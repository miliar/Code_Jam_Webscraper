//{{{
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <utility>
#include <queue>
#include <sstream>
using namespace std;
 
typedef long long ll;
typedef pair<int,int> ii;
#define size(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define REP(i,n) FOR(i,0LL,(n)-1) 
//}}}

ll T;
int L, N, C;

ll dist[2000];
ll A[2000];

ll solve() {
    ll ret = 987654321987654321LL;
    if( L == 0 ) {
        ll sum = 0;
        REP(i,N) sum += dist[i];
        ret = min( ret, sum );
    }
    else if( L == 1 ) {
        ll best = 987654321987654321LL;
        REP(first,N) {
            ll total = 0;
            REP(i,N) {
                if( first == i ) {
                    ll diff = T - total;
                    diff = max( 0LL, diff );
                    total += min( dist[i], min( diff + (dist[i]-diff) / 2, diff + dist[i]/2 ) );
                }
                else {
                    total += dist[i];
                }
            }
            best = min( best, total );
        } 
        ret = min( ret, best );
    }
    else if( L == 2 ) {
        ll best = 987654321987654321LL;
        for(int first=0;first<N;++first) for(int second=first+1;second<N;++second) {
            ll total = 0;
            REP(i,N) {
                if( first == i ) {
                    ll diff = T - total;
                    diff = max( 0LL, diff );
                    total += min( dist[i], min( diff + (dist[i]-diff) / 2, diff + dist[i]/2 ) );
                }
                else if( second == i ) {
                    ll diff = T - total;
                    diff = max( 0LL, diff );
                    total += min( dist[i], min( diff + (dist[i]-diff) / 2, diff + dist[i]/2 ) );
                }
                else {
                    total += dist[i];
                }
            }
            best = min( best, total );
        } 
        ret = min( ret, best );
    }
    return ret;
}

int main() {
    // freopen("inp","r",stdin);
    int tn;
    scanf("%d", &tn);

    FOR(cc,1,tn) {
        cin >> L >> T >> N >> C;
        // cerr << L << " " << T << " " << N << " " << C << endl;
        REP(i,C) cin >> A[i];
        REP(i,N) dist[i] = A[i%C] * 2;
        REP(i,N) fprintf( stderr, "%d ", dist[i] ); fprintf(stderr,"\n");
        ll ret = solve();
        printf("Case #%d: ", cc);
        printf("%I64d\n", ret);
    }
}

