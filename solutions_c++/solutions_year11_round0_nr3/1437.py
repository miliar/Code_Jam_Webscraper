#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long ll;

int num[ 2000 ], n;

int main(){
	int casos;
	
	scanf( "%d", &casos );
	for( int c = 1; c <= casos; ++c ){
		printf( "Case #%d: ", c );
		
		scanf( "%d", &n );
		int acc = 0;
		ll soma = 0;
		for( int i = 0; i < n; ++i ){
			scanf( "%d", num + i );
			acc = acc xor num[ i ];
			soma += num[ i ];
		}
		
		if( acc )
			printf( "NO\n" );
		else{
			int menor = num[ 0 ];
			for( int i = 1; i < n; ++i )
				menor = min( menor, num[ i ] );
			printf( "%lld\n", soma - menor );
		}
		
	}
}


