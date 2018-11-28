#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int prime[1001000];

main(){
	freopen( "CL.in", "r", stdin );
	freopen( "CL.out", "w", stdout );

	int t, tt = 0;
	int i, j, res;
	long long now, N;
	memset ( prime, 0, sizeof ( prime ) );
	for ( i = 2; i < 1000000; i ++ )
		if ( !prime[i] )
			for ( j = i + i; j < 1000000; j += i )
				prime[j] = 1;
	
	scanf ( "%d", &t );
	while( t -- ){
		res = 0;
		scanf ( "%I64d", &N );
		for ( i = 2; i < 1000000; i ++ )
			if ( !prime[i] ){
				now = i;
				while( now <= N / i ){
					now *= i;
					res ++;
				}
			}
		if ( N != 1 )
			res ++;
		printf( "Case #%d: %d\n", ++ tt, res );
	}
	
	return 0;
}

