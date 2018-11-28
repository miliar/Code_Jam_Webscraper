/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2011-05-21 Sat 10:05 PM    
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

#define M 105

char g[M][M];
int n;

int main() {
    int t, ncase = 0;

    cin >> t;
    while( t-- ) {
        cin >> n;
        REP(i,n) cin >> g[i];
        double wp[M] = {}, owp[M] = {}, oowp[M] = {};
        double ans[M];

        // wp
        REP(i,n) {
            int win = 0, loss = 0;
            REP(j,n) if( g[i][j] != '.' ) {
                if( g[i][j] == '1' ) win ++;
                else loss ++;
            }
            wp[i] = ( win + 0. ) / ( win + loss + 0. );
        }

        // owp
        REP(i,n) {
            double sum = 0, tot = 0;
            REP(j,n) if( g[i][j] != '.' ) {
                int win = 0, loss = 0;
                REP(k,n) if( k != i && g[j][k] != '.' ) {
                    if( g[j][k] == '1' ) win ++;
                    else loss ++;
                }
                tot ++;
                sum += ( win + 0. ) / ( win + loss + 0. );
//                if( i == 3 ) cout <<"add "<< j <<" "<< sum <<" "<< win <<" "<<loss<< endl;
            }
//            if( i == 3 ) cout << sum <<" "<< tot << endl;
            owp[i] = sum / tot;
        }

        // oowp
        REP(i,n) {
            double sum = 0, tot = 0;
            REP(j,n) if( g[i][j] != '.' ) {
                sum += owp[j], tot ++;
            }
            oowp[i] = sum / tot;
        }

//        REP(i,n) cout << i <<" "<< owp[i] << endl;

        REP(i,n) ans[i] = .25 * wp[i] + 0.50 * owp[i] + .25 * oowp[i];
        printf("Case #%d:\n", ++ncase );
        REP(i,n) printf("%.10lf\n", ans[i] );

    }


    return 0;
}

