#include <iostream>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <numeric>
#define FOR(i,A) for(typeof (A).begin() i = (A).begin() ; i != (A).end() ; i++)
#define mp make_pair
#define clr(v,x) memset( v, x , sizeof v ) 
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define TAM 110

using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef pair<int,ii> pii ;

int mx[ 31 ][ 2 ] ;
int v[ TAM ] ;
int p , n ;
int dp[ TAM ][ TAM ] ;

int calc(int x , int s ){
    if( s < 0 ) return -100000 ;
    if( x == n ) return s == 0 ? 0 : -100000 ;
    int &res = dp[ x ][ s ] ;
    if( res != -1 ) return res ;
    res = -100000 ;
    if( mx[ v[ x ] ][ 0 ] != -1 )
		res = max( res , calc( x + 1 , s ) + ( mx[ v[ x ] ][ 0 ] >= p ) );
    if( mx[ v[ x ] ][ 1 ] != -1 )
		res = max( res , calc( x + 1 , s - 1 ) + ( mx[ v[ x ] ][ 1 ] >= p ) );
    if( res < 0 ) res = -100000 ;
    return res ;
}
    
int main(){
    clr( mx , -1 ) ;
    for(int i = 0; i <= 10 ; i++)
	    for(int j = i; j <= i + 2 ; j++)
		    for(int k = j; k <= i + 2 ; k++){
				int s = i + j + k ;
				if( k - i == 2 ) mx[ s ][ 1 ] = max( mx[ s ][ 1 ] , k ) ;
				else mx[ s ][ 0 ] = max( mx[ s ][ 0 ] , k ) ;
    }
    int test ;
	cin >> test ;
    for(int k = 1; k <= test ; k++){
            int s ;
            cin >> n >> s >> p ;
			for(int i = 0 ; i < n ; i++) cin >> v[ i ] ;
            clr( dp , -1 ) ;
			printf("Case #%d: %d\n" , k , max( 0 , calc( 0 , s ) ) ) ;
    }
	return 0 ;
}
