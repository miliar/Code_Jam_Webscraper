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
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()
#define push(a,b) (a).push_back((b))

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

string S[50] ;
int n ;

void process()
{
    int res = 0 ;
    REP(i,n) {
        FOR(j,i,n-1) {
            int ok = 1 ;
            FOR(p,i+1,n-1)
                if ( S[j][p] == '1' ) { ok = 0 ; break ; }
            if ( !ok ) continue ;
            res += j-i ;
            DOW(p,j,i+1) swap( S[p], S[p-1] ) ;
            break ;
        }
    }
    cout << res << endl ;
}

void info_in()
{
    cin >> n ;
    REP(i,n) cin >> S[i] ;
}

main()
{
    int test ;
    cin >> test ;
    FOR(Case,1,test) {
        info_in() ;
        cout << "Case #" << Case << ": " ;
        process() ;
    }
}

