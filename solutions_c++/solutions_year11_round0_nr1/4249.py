/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2011-05-07 Sat 09:40 AM    
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<cassert>
#include<climits>
using namespace std;

#define REP(i,n) for(int i=0, _e(n); i<_e; i++)
#define FOR(i,a,b) for(int i(a), _e(b); i<=_e; i++)
#define FORD(i,a,b) for(int i(a), _e(b); i>=_e; i--) 
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )

#define sz size()
#define pb push_back
#define VI vector<int>
#define VS vector<string>

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

#define D(x) if(1) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) if(1) cout << __LINE__ <<" "<< #x " = " << (x) \
    <<", " << #y " = " << (y) << endl;

char r[105][3];
int p[105], n;
int d[105][105][105]; 

int main() {

    int t, ncase = 0;
    cin >> t;
    while( t-- ) {
        cin >> n;
        REP(i,n) cin >> r[i] >> p[i];
        SET( d, 63 );
        int inf = d[0][0][0];

        queue<int> q;
        q.push( 1 ); q.push( 1 ); q.push( 0 );
        d[1][1][0] = 0;

        while( !q.empty() ) {
            int o = q.front(); q.pop();
            int b = q.front(); q.pop();
            int hit = q.front(); q.pop();

            int cost = d[o][b][hit] + 1;
            if( ( o == p[hit] && r[hit][0] == 'O' ) ||
                ( b == p[hit] && r[hit][0] == 'B' ) ) {
                
                FOR(i,-1,1) FOR(j,-1,1) {
                    int O = o, B = b;
                    if( o == p[hit] && r[hit][0] == 'O' ) B = b+j; else O = o + i;
                    
                    if( B <= 0 || B > 100 ) continue;
                    if( O <= 0 || O > 100 ) continue;
                    if( d[O][B][hit+1] > cost ) {
                        d[O][B][hit+1] = cost;
                        if( hit+1 < n ) {
                            q.push( O ); q.push( B ); q.push( hit+1 );
                        }
                    }
                }
            }

            FOR(i,-1,1) FOR(j,-1,1) {
                int O = o + i, B = b + j;
                if( O > 0 && O <= 100 && B > 0 && B <= 100 ) {
                    if( d[O][B][hit] > cost ) {
                        d[O][B][hit] = cost;
                        q.push( O ); q.push( B ); q.push( hit );
                    }
                }
            }
        }

        int ans = inf;
        FOR(i,1,100) FOR(j,1,100) ans = min( ans, d[i][j][n] );
        printf("Case #%d: %d\n", ++ncase, ans );

    }
        
    return 0;
}

