#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
using namespace std;

int a[100];
char readin[300];

main(){
	freopen( "Ds.in", "r", stdin );
	freopen( "Ds.out", "w", stdout );
	
	int n, t, tt = 0;
	int i, j, top, mask;
	long long num, sqrted;
	
	scanf ( "%d", &t );
	while( t -- ){
		top = 0;
		scanf ( "%s", readin );
		for ( i = 0; readin[i]; i ++ )
			if ( readin[i] == '?' )
				a[ top ++ ] = i;
		n = strlen( readin );
		for ( mask = ( 1 << top ) - 1; mask >= 0; mask -- ){
			j = 0;
			num = 0;
			for ( i = 0; readin[i]; i ++ )
				if ( readin[i] == '?' ){
					if ( mask&(1<<j) )
						num += ( 1LL << ( n - i - 1 ) );
					j ++;
				}
				else
					if ( readin[i] == '1' )
						num += ( 1LL << ( n - i - 1 ) );
			sqrted = ( long long )sqrt( 1.0 * num );
//			cout << sqrted << " " << num << endl;
			while( sqrted * sqrted < num )
				sqrted ++;
			while( sqrted * sqrted > num )
				sqrted --;
	//		cout << sqrted << " " << num << endl;
			if ( sqrted * sqrted == num )
				break;
		}
		printf( "Case #%d: ", ++ tt );
		j = 0;
		for ( i = 0; readin[i]; i ++ )
			if ( readin[i] == '?' ){
				if ( mask&(1<<j) )
					printf( "1" );
				else
					printf( "0" );
				j ++;
			}
			else
				printf( "%c", readin[i] );
		printf( "\n" );
	}
	
	return 0;
}
