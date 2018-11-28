/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2012-04-14 Sat 07:43 PM    
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

struct triplet {
    int a, b, c;
    triplet( int x, int y, int z ) {
        a = x, b = y, c = z;
    }
};

vector<triplet> normal[35], surprising[35];
int t[M], p, s;

int main() {
       
    int T, ncase = 0, n;

    // initialization
    FOR(i,0,10) FOR(j,i,i+2) FOR(k,j,i+2) {
        int sum = i+j+k;
        if( k - i == 2 ) surprising[ sum ].pb( triplet( i, j, k ) );
        else normal[ sum ].pb( triplet( i, j, k ) );
    }

    cin >> T;
    while( T-- ) {
        cin >> n >> s >> p;
        REP(i,n) cin >> t[i];

        // now i have to run the dp
        int dp[M][M] = {};
        REP(i,n) REP(j,s+1) {
            REP(k,surprising[ t[i] ].sz) {
                if( surprising[ t[i] ][k].c >= p ) 
                    dp[i+1][j+1] = max( dp[i+1][j+1], 1+dp[i][j] );
                else
                    dp[i+1][j+1] = max( dp[i+1][j+1], dp[i][j] );
            }
            REP(k,normal[ t[i] ].sz) {
                if( normal[ t[i] ][k].c >= p ) 
                    dp[i+1][j] = max( dp[i+1][j], 1+dp[i][j] );
                else
                    dp[i+1][j] = max( dp[i+1][j], dp[i][j] );
            }
        }
    
        printf("Case #%d: %d\n", ++ncase, dp[n][s] );
    }

    return 0;
}

