#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long ll;
int n, l, h; 
int freq[ 200 ];

int main(){
	int casos;
	scanf( "%d", &casos );
	for( int k = 1; k <= casos; ++k ){
		printf( "Case #%d: ", k );
		scanf( "%d %d %d", &n, &l, &h );
		
		for( int i = 0; i < n; ++i )
			scanf( "%d", freq + i );
		
		int resp = -1;
		bool dm;
		for( int L = l; L <= h; ++L ){
			dm = false;
			for( int i = 0; i < n; ++i ){
				if( freq[ i ] % L && L % freq[ i ] ){
					dm = true;
					break;
				}				
			}
			if( !dm ){
				resp = L;	
				break;
			}
		}
		
		if( resp != -1 )
			printf( "%d\n", resp );
		else
			printf( "NO\n" );
	}
}
