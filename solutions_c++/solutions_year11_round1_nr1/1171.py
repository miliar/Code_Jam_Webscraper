/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2011-05-21 Sat 08:30 AM    
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

int main() {
    int t, ncase = 0, pd, pg;
    LL n, d, g;

    cin >> t;
    while( t-- ) {
        cin >> n >> pd >> pg;
        
        if( pd == 0 ) d = 1;
        else if( 100 % pd == 0 ) d = 100 / pd;
        else {
            FOR(i,1,100) if( (i*100) % pd == 0 ) {
                d = (i * 100) / pd;
                break;
            }
        }
        
        if( d > n ) {
            printf("Case #%d: Broken\n", ++ncase);
            continue;
        }else if( pd && !pg ) {
            printf("Case #%d: Broken\n", ++ncase);
            continue;
        }else if( pg == 100 && pd != 100 ) {
            printf("Case #%d: Broken\n", ++ncase);
            continue;
        }

//        cout << d<< endl;
    
        printf("Case #%d: Possible\n", ++ncase);
    }

    return 0;
}

