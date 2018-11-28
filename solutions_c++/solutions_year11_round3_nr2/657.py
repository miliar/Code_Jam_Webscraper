#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long ll;
int l, t, n, c; 
ll a[ 2000 ];
ll dist[ 2000 ];
bool marc[ 2000 ];

int main(){
	int casos;
	scanf( "%d", &casos );
	for( int k = 1; k <= casos; ++k ){
		memset( marc, false, sizeof( marc ) );
		
		printf( "Case #%d: ", k );
		scanf( "%d %d %d %d", &l, &t, &n, &c );
		for( int i = 0; i < c; ++i )
			scanf( "%lld", a + i );
		
		for( int i = 0; i < n; ++i )
			dist[ i ] = 2 * a[ i % c ];
		

		while( l ){
			ll ini = 0, ind = 0;	

			while( ind < n && ini + dist[ ind ] <= t ){
				ini += dist[ ind ];
				++ind;
			} 
			
			//printf( "%lld %lld\n", ini, ind );
			if( ind != n ){
				ll cidade = ind, best;
				best = dist[ ind ] - ( ini + dist[ ind ] - t ) / 2;
				for( int i = ind + 1; i < n; ++i ){
					if( !marc[ cidade ] && dist[ i ] > best ){
						best = dist[ i ];
						cidade = i;
					}
				}
			
			//	printf( "%d %d\n", best, cidade );
				if( cidade == ind ){
					dist[ cidade ] = best;
					marc[ cidade ] = true;
				}else{
					marc[ cidade ] = true;
					dist[ cidade ] /= 2;
				}
			}else
				break;
			--l;
		}
		
		ll soma = 0;
		for( int i = 0; i < n; ++i )
			soma += dist[ i ];
		printf( "%lld\n", soma );
		
	}
}
