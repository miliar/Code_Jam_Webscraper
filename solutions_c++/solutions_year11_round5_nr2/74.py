#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
using namespace std;

int a[1011];
int all[10111];
map< int, int > canuse;

main(){
	freopen( "BL.in", "r", stdin );
	freopen( "BL.out", "w", stdout );
	
	int t, tt = 0;
	int i, j, k;
	int n;
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d", &n );
		for ( i = 0; i < n; i ++ )
			scanf ( "%d", a + i );
		for ( i = n; i > 0; i -- ){
			memset ( all, 0, sizeof ( all ) );
			canuse.clear();
			for ( j = 0; j < n; j ++ )
				all[ a[j] ] ++;
			for ( j = 0; j <= 10000; j ++ )
				while( all[j] )
					if ( canuse[j] ){
						canuse[j] --;
						canuse[j+1] ++;
						all[j]--;
					}
					else{
						for ( k = 0; k < i; k ++ )
							if ( all[j+k] == 0 )
								break;
							else
								all[j+k] --;
						if ( k != i ){
							j = 20000;
							break;
						}
						canuse[j+k] ++;
					}
			if ( j < 20000 )
				break;
		}
		printf( "Case #%d: %d\n", ++ tt, i );
	}
	
	return 0;
}
