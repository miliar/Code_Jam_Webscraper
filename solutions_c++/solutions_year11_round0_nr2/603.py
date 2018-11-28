//For Future
//By JFantasy

#include <cstdio>
#include <cstring>

const int maxn = 30;

int rep[maxn][maxn] , del[maxn][maxn] , n;
char str[maxn*maxn] , ans[maxn*maxn];

void init() {
	memset( rep , 0 , sizeof(rep) );
	memset( del , 0 , sizeof(del) );
	int x;
	scanf( "%d" , &x );
	while ( x-- ) {
		char s[5];
		scanf( "%s" , s );
		int x = s[0]-'A'+1 , y = s[1]-'A'+1 , z = s[2]-'A'+1;
		rep[x][y] = rep[y][x] = z;
	}
	scanf( "%d" , &x );
	while ( x-- ) {
		char s[5];
		scanf( "%s" , s );
		int x = s[0]-'A'+1 , y = s[1]-'A'+1;
		del[x][y] = del[y][x] = 1;
	}
	scanf( "%d%s" , &n , str );
}

void work( int cas ) {
	int len = 0;
	memset( ans , 0 , sizeof(ans) );
	for ( int i = 0; i < n; i++ ) {
		ans[len++] = str[i];
		if ( len == 1 ) continue;
		int x = ans[len-1]-'A'+1 , y = ans[len-2]-'A'+1;
		if ( rep[x][y] ) {
			len -= 2;
			ans[len++] = char( 'A' + rep[x][y] - 1 );
		} else {
			for ( int j = len-1; j > 0; j-- ) {
				y = ans[j-1]-'A'+1;
				if ( del[x][y] ) {
					len = 0;
					break;
				}
			}
		}
	}
	printf( "Case #%d: [" , cas );
	for ( int i = 0; i < len; i++ ) {
		printf( "%c" , ans[i] );
		if ( i < len-1 ) printf( ", " );
	}
	printf( "]\n" );
}

int main() {
	int cas , t = 0;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		init();
		work(++t);
	}
	return 0;
}