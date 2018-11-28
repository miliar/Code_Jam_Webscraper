#include<cstdio>
#include<cstring>

using namespace std;

const int MAXN = 8;
char s[MAXN][MAXN];

void read() {
    int i, j;

    for ( i = 0; i < 4; ++ i ) {
        scanf ( "%s", s[i] );
    }

}

bool check ( char c ) {
    int i, j;

    for ( i = 0; i < 4; ++ i ) {
        int br = 0, t = 0;
        for ( j = 0; j < 4; ++ j ) {
            if ( s[i][j] == c ) br ++;
            else if ( s[i][j] == 'T' ) t ++;
        }
        if ( br + t == 4 ) return 1;
    }

    for ( i = 0; i < 4; ++ i ) {
        int br = 0, t = 0;
        for ( j = 0; j < 4; ++ j ) {
            if ( s[j][i] == c ) br ++;
            else if ( s[j][i] == 'T' ) t ++;
        }
        if ( br == 4 ) return 1;
    }

    int br = 0, t = 0;
    for ( i = 0; i < 4; ++ i ) {
        if ( s[i][i] == c ) br ++;
        else if ( s[i][j] == 'T' ) t ++;
    }

    if ( br + t == 4 ) return 1;

    br = 0, t = 0;
    i = 0, j = 3;

    while ( i < 4 && j >= 0 ) {
        if ( s[i][j] == c ) br ++;
        else if ( s[i][j] == 'T' ) t ++;
        i ++;
        j --;
    }

    if ( br + t == 4 ) return 1;

    return 0;

}

bool find ( int c ) {
    int i, j;

    for ( i = 0; i < 4; ++ i ) {
        for ( j = 0; j < 4; ++ j ) {
            if ( s[i][j] == c ) return 1;
        }
    }

    return 0;

}

int main() {

    //freopen ( "poker.in" , "r", stdin );
    //freopen ( "poker.out", "w", stdout );

    int i, tests;

    scanf ( "%d", &tests );

    for ( i = 1; i <= tests; ++ i ) {
        read();
        if ( check ( 'X' ) ) printf ( "Case #%d: X won\n", i );
        else if ( check ( 'O' ) ) printf ( "Case #%d: O won\n", i );
        else if ( find ( '.' ) ) printf ( "Case #%d: Game has not completed\n", i );
        else printf ( "Case #%d: Draw\n", i );
    }

    return 0;

}
