#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
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

const int maxc = 100007 ;

int N, K, B, T ;
int X[100], V[100], d[107][107] ;
VI mark ;

int can_finish( int tt )
{	
	if ( T * V[tt] < B - X[tt] ) return maxc ;
	
	int res = 0 ;
	FOR(i,tt+1,N) {
		if ( mark[i] ) {			
			res++ ;
		}
	}	
	return res ;
}

main()
{
	int test ;
	cin >> test ;
	FOR(Case,1,test) {		
		cin >> N >> K >> B >> T ;
		
		FOR(i,1,N) cin >> X[i] ;
		FOR(i,1,N) cin >> V[i] ;										
		
		int res = 0 ;
		mark = VI( N+1, 0 ) ;
		DOW(i,N,1) {
			if ( !K ) break ;
			int val = can_finish( i ) ;
			//cout << val << " " ;
			if ( val < maxc ) {
				K-- ;
				res += val ;				
			}
			else mark[i] = 1 ;
		}
		//cout << endl ;
		cout << "Case #" << Case << ": " ;
		if ( K ) cout << "IMPOSSIBLE" << endl ;
		else cout << res << endl ;
	}
}