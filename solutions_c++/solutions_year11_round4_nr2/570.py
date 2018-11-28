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

int R, C, D ;
long long A[3][507][507] ;
long long Mass[507][507] ;

long long cal( int sh, int i, int j, int p, int q )
{
	return A[sh][p][q] + A[sh][i-1][j-1] - A[sh][p][j-1] - A[sh][i-1][q] ;
}

int ToaDo( int x )
{
	return x*2 - 1 ;
}

int ok( int K )
{
	FOR(i,1,R-K+1)
		FOR(j,1,C-K+1) {			
			int p = i + K - 1 ;
			int q = j + K - 1 ;
			int tamx = (i + p - 1) ;
			int tamy = (j + q - 1) ;
			long long totalX = ( cal( 2, i, j, p, q ) - Mass[i][j] - Mass[i][q] - Mass[p][j] - Mass[p][q] ) * tamx ;
			long long totalY = ( cal( 2, i, j, p, q ) - Mass[i][j] - Mass[i][q] - Mass[p][j] - Mass[p][q] ) * tamy ;
			
			long long valX = cal( 0, i, j, p, q ) - ToaDo(i) * Mass[i][j] - ToaDo(i) * Mass[i][q] - ToaDo(p) * Mass[p][j] - ToaDo(p) * Mass[p][q] ;
			long long valY = cal( 1, i, j, p, q ) - ToaDo(j) * Mass[i][j] - ToaDo(q) * Mass[i][q] - ToaDo(j) * Mass[p][j] - ToaDo(q) * Mass[p][q] ;
			
			//cout << cal(2, i, j, p, q ) << endl ;
			if ( totalX == valX && totalY == valY )
				return 1 ;
		}
	return 0 ;
}

void solve( int Case )
{
	cin >> R >> C >> D ;
	REP(i,3) memset( A[i], 0, sizeof(A[i]) ) ;
	REP(i,R) {
		string s ;
		cin >> s ;
		REP(j,C) {
			Mass[i+1][j+1] = (s[j] - '0' + D) ;
			A[0][i+1][j+1] = (s[j] - '0' + D) * (2*i+1) ;
			A[1][i+1][j+1] = (s[j] - '0' + D) * (2*j+1) ;
			A[2][i+1][j+1] = (s[j] - '0' + D) ;
		}
	}
	
	FOR(i,1,R)
		FOR(j,1,C) 
		REP(k,3) A[k][i][j] += A[k][i-1][j] + A[k][i][j-1] - A[k][i-1][j-1] ;
	
	DOW(K, min(R,C), 3 ) 
		if ( ok(K) ) {
			cout << "Case #" << Case << ": " << K << endl ;
			return ;
		}
	cout << "Case #" << Case << ": " << "IMPOSSIBLE" << endl ;
}

main()
{
	int Test ;
	cin >> Test ;
	FOR(Case,1,Test) solve( Case ) ;
}