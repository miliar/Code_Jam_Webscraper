#include <stdio.h>
#include <string.h>

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <queue>

using namespace std ;
#define lint long long
#define FOREACH(it,v) for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )
#define ALL(v) (v).begin(),(v).end()

const int infinity = 0x3fffffff ;
const lint linfinity = 0x3fffffffffffffffLL ;

const int maxn = 10005 ;
const double eps = 1e-10 ;

int n , d[maxn] , l[maxn] , D ;
int dp[maxn] ;


int solve(){
	dp[0] = d[0] ;

	for( int i = 1 ; i < n ; ++i )
		dp[i] = -1 ;

	for( int i = 0 ; i < n-1 ; ++i ){
		for( int j = i+1 ; j < n ; ++j )
			if( d[j]-d[i] <= dp[i] ){
				dp[j] = max( dp[j] , min(l[j] , d[j]-d[i]) ) ;
			}
			else break ;
	}

	for( int i = 0 ;i < n ;++i )
		if( dp[i] >= 0 && d[i] + dp[i] >= D )
			return true ;
	
	return false ;
}

int main(){

	int cases ;
	cin >> cases ;

	for( int cs = 1 ; cs <= cases ; cs++ ){
		cin >> n ;
		for( int i = 0 ;i < n ; ++i )
			cin >> d[i] >> l[i] ;
		cin >> D ;

		cout << "Case #" << cs << ": " ;
		if( solve() ) cout << "YES" << endl ;
		else cout << "NO" << endl ;
	}

	return 0 ;
}
