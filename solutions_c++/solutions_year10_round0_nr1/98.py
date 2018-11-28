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

string ANSWER[2] = { "OFF" , "ON" } ;

main()
{
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	int F[31], light[31] ;
	FOR(i,1,30) F[i] = (1<<i) - 1 ;
	int test ;
	cin >> test ;
	FOR(Case,1,test) {
		int N, K ;
		cin >> N >> K ;
		//memset( light, 0, sizeof(light) ) ;
		
		K = K % ( F[N] + 1 ) ;
		//cout << K << " " <<F[N] << endl ;
		DOW(i,N,1) {
			if ( K == F[i] ) {
				light[i] = 1 ;
				K = F[i-1] ;
			}
			else {
				light[i] = 0 ;
				if ( K > F[i-1] ) K -= F[i-1] - 1 ;
			}
		}
		
		cout << "Case #" << Case << ": " << ANSWER[light[N]] << endl ;
	}
}