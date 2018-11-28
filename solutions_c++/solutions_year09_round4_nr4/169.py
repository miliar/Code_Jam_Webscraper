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

double X[100], Y[100], R[100] ;
int n ;

double sqr( int X ) 
{
    return (double)X*X ;
}

double Distance( int i, int j )
{
    return sqrt( sqr( X[i] - X[j] ) + sqr( Y[i] - Y[j] ) ) ;
}

void process()
{
    if ( n == 1 ) printf("%.6lf\n",R[0]*1.0) ;
    else if ( n == 2 ) printf("%.6lf\n",max( R[0]*1.0, R[1]*1.0 ) ) ;
    else if ( n == 3 ) {
        double res = 1e+17 ;
        double val = max( R[0] * 2 , R[1] + R[2] + Distance( 1, 2) ) ;
        res = min( res, val ) ;
        
        val = max( R[1] * 2 , R[0] + R[2] + Distance( 0, 2 ) ) ;
        res = min( res, val ) ;
        
        val = max( R[2] * 2 , R[0] + R[1] + Distance( 0, 1 ) ) ;
        res = min( res, val ) ;
        printf("%.6lf\n",res/2) ;
    }
}

void info_in()
{
    cin >> n ;
    REP(i,n) cin >> X[i] >> Y[i] >> R[i] ;
}

main()
{
    int test ;
    cin >> test; 
    FOR(Case,1,test) {
        info_in() ;
        cout << "Case #" << Case << ": " ;
        process() ;
    }
}
