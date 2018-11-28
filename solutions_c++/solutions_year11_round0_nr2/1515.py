#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

#define OUT(tp,t) printf( #t "=" tp " ", t  );

using namespace std;

bool op[256][256];
char com[256][256];
int N;

int main( ) {
	int re;
	int a;
	int n;
	char s[1000];

	//freopen( "D:\\b\\in.txt", "r", stdin );
	freopen( "D:\\b\\B-small-attempt0.in", "r", stdin );
	freopen( "D:\\b\\B-small-attempt0.out", "w", stdout );

	scanf( "%d", &re );
	int ri = 1;
	while( re-- ) {
		memset( op, 0, sizeof(op) );
		memset( com, 0, sizeof(com) );
		scanf( "%d", &n );
		while( n-- ) {
			scanf( "%s", s );
			com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
		}
		scanf( "%d", &n );
		while( n-- ) {
			scanf( "%s", s );
			op[s[0]][s[1]] = op[s[1]][s[0]] = true;
		}
		scanf( "%d", &n );
		scanf( "%s", s );
		char t[1000];
		int i, j, k=0;
		for( i=0 ; i<n ; i++ ) {
			if( k>0 && com[s[i]][t[k-1]] ) {
				t[k-1] = com[s[i]][t[k-1]];
			} else {
				t[k++] = s[i];
			}
			for( j=0 ; j<k ; j++ ) {
				if( k>0 && op[t[k-1]][t[j]] ) {
					k = 0; break;
				}
			}
		}

		t[k] = 0;
		printf( "Case #%d: [", ri++ );
		for( i=0 ; i<k ; i++ ) {
			if( i ) {putchar( ',' );putchar( ' ' );}
			putchar( t[i] );
		}
		putchar( ']' ); putchar( 10 );
	}

	return 0;
}
