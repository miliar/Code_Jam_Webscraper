#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

const int maxn = 105 ;
const int maxk = 30 ;

int trace[maxn], edge[maxn][maxn] ;
int A[maxn][maxk], matchX[maxn], matchY[maxn] ;
int n, K ;

int findpath( int x )
{
    memset( trace, -1, sizeof(trace) ) ;
    queue<int> q ;
    q.push( x ) ;
    
    while ( !q.empty() ) {
        int x = q.front() ;
        q.pop() ;
        REP(y,n)
            if ( edge[x][y] && trace[y] == -1 && matchX[x] != y ) {
                trace[y] = x ;
                if ( matchY[y] == -1 ) return y ;
                q.push( matchY[y] ) ;
            }
    }
    return -1 ;
}

void enlarge( int y )
{
    while ( y > -1 ) {
        int x = trace[y] ;
        int next = matchX[x] ;
        matchX[x] = y ;
        matchY[y] = x ;
        y = next ;
    }
}

void process()
{
    memset( matchX, -1, sizeof(matchX) ) ;
    memset( matchY, -1, sizeof(matchY) ) ;
    
    int res = 0 ;
    REP(x,n) {
        int y = findpath( x ) ;
        if ( y == -1 ) continue ;
        enlarge( y ) ;
        res++ ;
    }
    cout << n - res << endl ;
}

void init() 
{
    memset( edge, 0, sizeof(edge) ) ;
    REP(u,n)
        REP(v,n) {
            if ( u == v ) continue ;
            int ok = 1 ;
            REP(i,K)
                if ( A[u][i] <= A[v][i] ) ok = 0 ;
            edge[u][v] = ok ;
        }
}

void info_in()
{
    cin >> n >> K ;
    REP(i,n)
        REP(j,K) cin >> A[i][j] ;
}

main()
{
    int test ;
    cin >> test ;
    FOR(Case,1,test) {
        info_in() ;
        cout << "Case #" << Case << ": " ;
        init()    ;
        process() ;
    }
}
