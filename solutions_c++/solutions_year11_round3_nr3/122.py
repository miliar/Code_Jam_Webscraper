#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

main(){
	int t, n, L, H, tt = 0;
	int i, j, a[10010];
	
	freopen( "CS.in", "r", stdin );
	freopen( "CS.out", "w", stdout );
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d %d %d", &n, &L, &H );
		for ( i = 0; i < n; i ++ )
			scanf ( "%d", a + i );
		for ( i = L; i <= H; i ++ ){
			for ( j = 0; j < n; j ++ )
				if ( a[j] % i != 0 && i % a[j] != 0 )
					break;
			if ( j == n )
				break;
		}
		if ( i <= H )
			printf( "Case #%d: %d\n", ++ tt, i );
		else
			printf( "Case #%d: NO\n", ++ tt );
	}
	
	return 0;
}
