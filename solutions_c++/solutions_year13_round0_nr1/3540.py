#include <cstdio>
#include <iostream>

using namespace std;

bool checkline( char field[][ 4 ], int pos, char c ) {
    int T = 0, i = 0;
    for ( i = 0; i < 4; ++i ) {
        if ( field[ pos ][ i ] != c ) {
            if ( field[ pos ][ i ] == 'T' ) {
                ++T;
            }
            else {
                return false;
            }
        }
    }
    if ( T > 1 ) {
        return false;
    }
    return true;
}

bool checkheight( char field[][ 4 ], int pos, char c ) {
    int i, T = 0;
    for ( i = 0; i < 4; ++i ) {
        if ( field[ i ][ pos ] != c ) {
            if ( field[ i ][ pos ] == 'T' ) {
                ++T;
            }
            else {
                return false;
            }
        }
    }
    if ( T > 1 ) {
        return false;
    }
    return true;
}

bool checkdiagonals( char field[][ 4 ], char c ) {
    int i, j, T = 0;
    bool found = true;
    for ( i = 0, j = 0; i < 4; ++i, ++j ) {
        if ( field[ i ][ j ] != c ) {
            if ( field[ i ][ j ] == 'T' ) {
                ++T;
            }
            else {
                found = false;
            }
        }
    }
    if ( T > 1 ) {
        found = false;
    }
    if ( found ) {
        return true;
    }
    found = true;
    T = 0;
    for ( i = 0, j = 3; i < 4; ++i, --j ) {
        if ( field[ i ][ j ] != c ) {
            if ( field[ i ][ j ] == 'T' ) {
                ++T;
            }
            else {
                found = false;
            }
        }
    }
    if ( T > 1 ) {
        return false;
    }
    if ( found ) {
        return true;
    }
}

char check( char field[][ 4 ] ) {
    bool found = false;
    int k, j, i;
    for ( i = 0; i < 4; ++i ) {
        if ( checkline( field, i, 'X' ) ) {
            return 'X';
        }
        else if ( checkline( field, i, 'O' ) ) {
            return 'O';
        }
    }
    for ( i = 0; i < 4; ++i ) {
        if ( checkheight( field, i, 'X' ) ) {
            return 'X';
        }
        else if ( checkheight( field, i, 'O' ) ) {
            return 'O';
        }
    }
    if ( checkdiagonals( field, 'X' ) ) {
        return 'X';
    }
    if ( checkdiagonals( field, 'O' ) ) {
        return 'O';
    }
    for ( i = 0; i < 4; ++i ) {
        for ( j = 0; j < 4; ++j ) {
            if ( field[ i ][ j ] == '.' ) {
                found = true;
                break;
            }
        }
    }
    if ( !found ) {
        return 'd';
    }
    return 'g';
}

int main() {
    freopen( "a.in", "r", stdin );
    freopen( "a.out", "w", stdout );
    int i, t, k;
    char field[ 4 ][ 4 ], c;
    scanf( "%d", &t );
    for ( int j = 1; j <= t; ++j ) {
        for ( i = 0; i < 4; ++i ) {
            scanf( "%*c" );
            for ( k = 0; k < 4; ++k ) {
                scanf( "%c", &field[ i ][ k ] );
            }
        }
        scanf( "%*c" );
        c = check( field );
        if ( c == 'X' ) {
            printf( "Case #%d: X won\n", j );
        }
        if ( c == 'O' ) {
            printf( "Case #%d: O won\n", j );
        }
        if ( c == 'd' ) {
            printf( "Case #%d: Draw\n", j );
        }
        if ( c == 'g' ) {
            printf( "Case #%d: Game has not completed\n", j );
        }
    }
    return 0;
}
