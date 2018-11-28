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

const int MOD = 100003 ;
long long d[507][507] ;
int C[507][507] ;

void init()
{
	C[0][0] = 1 ;
	FOR(j,1,500) {
		C[0][j] = 1 ;
		FOR(i,1,j) {
			C[i][j] = ( C[i-1][j-1] + C[i][j-1] ) % MOD ;
		}
	}	
}

main()
{
	init() ;
	int test ;
	cin >> test ;
	FOR(Case,1,test) {
		int n ;
		cin >> n ;		
		
		memset( d, 0, sizeof(d) ) ;
		
		FOR(i,2,n) {
			d[i][1] = 1 ;
			FOR(j,2,i-1) {
				d[i][j] = 0 ;
				FOR(k,1,j-1) d[i][j] += ( d[j][k] * C[j-k-1][i-j-1] ) % MOD ;			
			}
		}
		
		long long res = 0 ;
		FOR(i,1,n) res = ( res + d[n][i] ) % MOD ;
		cout << "Case #" << Case << ": " << res << endl ;
	}
}