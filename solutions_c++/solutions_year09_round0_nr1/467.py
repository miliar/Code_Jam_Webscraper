#include <cstdio>
#include <cstring>

int l, d, n;
char words[5005][20];
int patt[20];

int main( void )
{
//	freopen( "A.in", "r", stdin );

	scanf( "%d %d %d", &l, &d, &n );
	for( int i = 0; i < d; ++i ) scanf( "%s", words[i] );

	for( int prob = 0; prob < n; ) {
		int at = 0;
		char buff[100000]; scanf( "%s", buff );
		char* p = buff;

		memset(patt, 0, sizeof(patt));
		for( ; at < l && *p; ++at, ++p ) {
			if( *p == '(' ) {
				++p;
				while( *p != ')' ) {
					patt[at] |= 1 << (*p-'a');
					++p;
				}
			} else {
				patt[at] |= 1 << (*p-'a');
			}
		}

/*		for( int i = 0; i < l; ++i ) {
			if( i ) putchar( ' ' );
			printf( "%d", patt[i] );
		}
		putchar( '\n' );*/

		int res = 0;

		if( at == l && !*p ) {
			for( int i = 0; i < d; ++i ) {
				bool match = true;

				for( int j = 0; j < l; ++j ) {
					if( !(patt[j] & (1 << (words[i][j]-'a'))) ) { match = false; break; }
				}
				if( match ) ++res;
			}
		}
		
		printf( "Case #%d: %d\n", ++prob, res );
	}

	return 0;
}

