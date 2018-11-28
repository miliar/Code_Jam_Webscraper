#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;


ll gcd( ll a, ll b ){
	if( b )
		return gcd( b, a % b );
	return a;
}

ll mdc( ll a, ll b ){
	return a * b / gcd( a, b );
}
 

int main(){
	ll n, pd, pg;
	int casos;
	scanf( "%d", &casos );
	for( int i = 1; i <= casos; ++i ){
		printf( "Case #%d: ", i );
		scanf( "%lld %lld %lld", &n, &pd, &pg );
	
	
		ll num1 = pd / gcd( pd, 100 ), den1 = 100 / gcd( pd, 100 );
		bool dm = false;
	

		if( den1 > n )
			dm = true;
		ll a = pg - num1, b = 100 - den1;
					
		if( b < a || a < 0 || b < 0 )
			dm = true;				
		
		if( dm )
			printf( "Broken\n" );
		else
			printf( "Possible\n" );
	}
	

}

