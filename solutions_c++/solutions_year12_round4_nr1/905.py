/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2012-05-26 Sat 10:12 PM    
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

#define M 10005
int d[M], l[M], len, n;
int m[M];

int main() {
    
    int t, ncase = 0;
    scanf("%d",&t);
    while( t-- ) {
        scanf("%d",&n);
        REP(i,n) scanf("%d %d",&d[i],&l[i]);
        REP(i,n) m[i] = 0; 
        scanf("%d",&len);
       
        m[0] = d[0];
        bool yes = 0;
        REP(i,n) if( m[i] ) {
            // checking if I can go to end
            if( d[i] + m[i] >= len ) yes = 1;
//            D2( i, m[i] );

            // at first swinging
            FOR(j,i+1,n-1) if( d[j] - d[i] <= m[i] ) 
                m[j] = max( m[j], min( d[j] - d[i], l[j] ) );
            else break;
        }

        if( yes ) printf("Case #%d: YES\n", ++ncase );
        else printf("Case #%d: NO\n", ++ncase );

    }

        
    return 0;
}

