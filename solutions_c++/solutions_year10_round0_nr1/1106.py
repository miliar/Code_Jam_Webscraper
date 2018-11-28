#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main( ){
	int t, ca = 0, n, k, c;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	scanf( "%d", &t );
	while ( t-- ){
		scanf( "%d%d", &n, &k );
		c = (1<<n);
		k++;
		printf( "Case #%d: ", ++ca );
		if ( k%c == 0 ) printf( "ON\n" );
		else printf( "OFF\n" );
	}
}
