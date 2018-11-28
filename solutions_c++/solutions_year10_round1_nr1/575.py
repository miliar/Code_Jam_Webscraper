# include <iostream>

using namespace std;

const int MaxN = 55;

int n, k;
char board[ MaxN ][ MaxN ];

int test;

int get( char ch ) {
    if ( ch == 'R' )
        return 0;
    return 1;
}

void rotate() {
    char tmp[ MaxN ][ MaxN ];

    for ( int i = 0; i < n; i++ )
        for ( int j = 0; j < n; j++ )
            tmp[ j ][ n - i - 1 ] = board[ i ][ j ];

    for ( int i = 0; i < n; i++ )
        for ( int j = 0; j < n; j++ )
            board[ i ][ j ] = tmp[ i ][ j ];
}

void gravity() {
    for ( int c = 0; c < n; c++ ) {
        for ( int i = n - 1; i >= 0; i-- )
            if ( board[ i ][ c ] != '.' ) {
                for ( int j = i + 1; j < n && board[ j ][ c ] == '.'; j++ )
                    swap( board[ j ][ c ], board[ j - 1 ][ c ] );
            }
    }
}

const int dx[] = { 0, 1, 1,  1 };
const int dy[] = { 1, 0, 1, -1 };

bool check( int r, int c ) {
    for ( int dir = 0; dir < 4; dir++ ) {
        int cr = r;
        int cc = c;

        int i;
        for ( i = 1; i < k; i++ ) {
            int nr = cr + dx[ dir ];
            int nc = cc + dy[ dir ];

            if ( nr < 0 || nr >= n || nc < 0 || nc >= n ) break;
            if ( board[ nr ][ nc ] != board[ cr ][ cc ] ) break;

            cr = nr;
            cc = nc;
        }

        if ( i == k )
            return true;
    }

    return false;
}

int main() {
    scanf( "%d", &test );
    for ( int testId = 1; testId <= test; testId++ ) {
        scanf( "%d%d", &n, &k );
        for ( int i = 0; i < n; i++ )
            scanf( "%s", &board[ i ] );

        rotate();
        gravity();

        bool player[ 2 ] = { 0, 0 };
        for ( int i = 0; i < n; i++ )
            for ( int j = 0; j < n; j++ )
                if ( board[ i ][ j ] != '.' && check( i, j ) )
                    player[ get( board[ i ][ j ] ) ] = true;

        printf( "Case #%d: ", testId );
        if ( player[ 0 ] && player[ 1 ] ) printf( "Both\n" );
        else if ( player[ 0 ] ) printf( "Red\n" );
        else if ( player[ 1 ] ) printf( "Blue\n" );
        else printf( "Neither\n" );
    }

    return 0;
}