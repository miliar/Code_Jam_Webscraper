#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef long long int64;

#define forit(a,b) for(typeof((b).end()) a=(b).begin();a!=(b).end();a++)
#define clr(a,b) memset(a,b,sizeof a)
#define all(a) a.begin(),a.end()
#define sorta(a) sort(all(a))

int N;
int64 a[ 10100 ] , L , H;
/*
int pr[ 10000000 ] , cpr = 0;
bool isbad[ 100000001 ];
*/

int main(){
	/*
	for( int q = 1 ; q <= 30 ; q++ ){
		if( q % 3 == 0 ){
			int t = q , r = 0;
			while( t % 3 == 0 ) r++, t/=3;
			printf("%d %d\n",q,r);
		}
	}
	
	return 0;
	clr( isbad , 0 );
	for( int q = 2 ; q <= 100000000 ; q++ ){
		if( isbad[ q ] == 0 ){
			pr[ cpr ++ ] = q;
			for( int w = q ; w <= 100000000 ; w += q ) isbad[ w ] = 1;
		}
	}
	*/
	int test;
	scanf( "%d" ,&test );
	for( int ttest = 1 ; ttest <= test ; ttest++ ){
		scanf( "%d%lld%lld" ,&N ,&L ,&H );
		if( H < L ) swap( L , H );
		for( int q = 0 ; q < N ; q++ ){
			scanf( "%lld" ,&a[ q ] );
		}
		int64 ret = -1;
		for( int q = L ; q <= H ; q++ ){
			bool good = 1;
			for( int w = 0 ; w < N ; w++ ){
				if( a[ w ] % q == 0 || q % a[ w ] == 0 ) continue;
				good = 0;
			}
			if( good ){
				ret = q;
				break;
			}
		}
		if( ret > 0 ) printf( "Case #%d: %lld\n" ,ttest ,ret );
		else printf( "Case #%d: NO\n" ,ttest );
	}
	return 0;
}
