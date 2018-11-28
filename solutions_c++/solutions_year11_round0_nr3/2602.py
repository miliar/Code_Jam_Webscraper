#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n , arr[ 1111 ] , bit[ 22 ];

int main(){

	int t;
	scanf( "%d" ,&t );

	for( int tt = 0 ; tt < t ; tt++ ){
		
		scanf( "%d" ,&n );
		
		for( int q = 0 ; q < n ; q++ ){
			scanf( "%d" ,&arr[ q ] );
		}
		
		memset( bit , 0 , sizeof bit );
		
		int m = arr[ 0 ] , ret = 0;
		
		for( int q = 0 ; q < n ; q++ ){
			m = min( m , arr[ q ] );
			ret += arr[ q ];
			for( int b = 0 ; b < 21 ; b++ ){
				if( arr[ q ] & (1 << b) ){
					bit[ b ] ++;
				}
			}
		}
		
		ret -= m;
		
		for( int q = 0 ; q < 21 ; q++ ){
			if( bit[ q ] % 2 ){
				printf( "Case #%d: NO\n" ,tt + 1 );
				goto bad;
			}
		} 
	
		printf( "Case #%d: %d\n" ,tt + 1, ret );		
		
		bad:;
	}

	return 0;
}
