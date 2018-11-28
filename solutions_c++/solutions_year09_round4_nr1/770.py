#include<iostream>
using namespace std;

char board[50][50];
int ans, n;

void change( int m, int k ){
    char tmp[50];
    int i;
    for( i = 0; i < n; i++ )
        tmp[i] = board[m][i];
    for( i = 0; i < n; i++ )
        board[m][i] = board[k][i];
    for( i = 0; i < n; i++ )
        board[k][i] = tmp[i];
}

bool check( ){
	int i, j;
	for( i = 0; i < n; i++ )
		for( j = i + 1; j < n; j++ )
			if( board[i][j] == '1' ) return false;
	return true;
}

bool ok( int m ){
	int i;
	for( i = m + 1; i < n; i++ )
		if( board[m][i] == '1' ) return false;
	return true;
}

void deal( ){
    int i, j, k, u;
	for( i = 0; i < n; i++ ){
		if( check( ) ) return;
		if( ok( i ) ) continue;
		u = -1;
		for( j = i + 1; j < n; j++ ){
			for( k = n - 1; k >= 0; k-- ){
				if( board[j][k] == '1' ){
					u = j;
					break;
				}
			}
			if( k == -1 ){ k = 0; u = j; }
			if( k <= i ) break;
		}
		for( k = u; k > i; k-- ){
			change( k, k - 1 );
			ans++;
		}
    }
}

int main( ){
    int i, t, cas;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
    scanf( "%d", &t );
    for( cas = 1; cas <= t; cas++ ){
        scanf( "%d", &n );
        for( i = 0; i < n; i++ )
            scanf( "%s", &board[i] );
        ans = 0;
		deal( );
        printf( "Case #%d: %d\n", cas, ans );
    }
    return 0;
}
