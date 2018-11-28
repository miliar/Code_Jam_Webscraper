#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[1100];

main(){
	freopen( "CL.in", "r", stdin );
	freopen( "CL.out", "w", stdout );
	
	int t, tt = 0;
	int n, res;
	int i;
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d", &n );
		for ( i = 0; i < n; i ++ )
			scanf ( "%d", a + i );
		res = 0;
		for ( i = 0; i < n; i ++ )
			res ^= a[i];
		if ( res ){
			printf( "Case #%d: NO\n", ++ tt );
			continue;
		}
		sort ( a, a + n );
		for ( i = 1; i < n; i ++ )
			res += a[i];
		printf( "Case #%d: %d\n", ++ tt, res );
	}
	
	return 0;
}
