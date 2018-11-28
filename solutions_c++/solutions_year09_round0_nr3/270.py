#include <iostream>

using namespace std;

char str[ 10000 ];
int i, j;
int hash[ 10000 ];
char rt[] = "welcome to code jam";


int main() {
	int t ;

	freopen ("C-large.in", "r", stdin );
	freopen ( "C-large.out", "w", stdout );

	scanf("%d", &t);

	getchar();

	int ty = t;

	while( t-- ) {
		memset( hash, 0, sizeof( hash ));

		gets( str );

		for(i = 0; str[i]; i++) {
			for(j = 0; rt[j]; j++) {
				if( rt[j] == str[i] ) {
					if( j == 0 ) {
						hash[ 0 ] ++;
						hash[ 0 ] %= 10000;
					}else {
						hash[ j ] += hash[ j-1 ];
						hash[ j ] %= 10000;
					}
				}
			}
		}

		printf( "Case #%d: %04d\n", ty - t, hash[ 18 ] );
	}
	return 0;
}

