/*
    Marko Bakovic
    Google Code Jam
    Problem A. Tic-Tac-Toe-Tomek
*/

#include <cstdio>
#include <algorithm>

using namespace std;

int cases;

char S[ 5 ][ 5 ];

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    scanf( "%d", &cases );

    for ( int cnt = 1; cnt <= cases; cnt++ )
    {
        for ( int i = 0; i < 4; i++ ) scanf( "%s", S[ i ] );

        bool winO = false, winX = false;
        for ( int i = 0; i < 4; i++ )
        {
            int cntO = 0, cntX = 0, cntT = 0;
            for ( int j = 0; j < 4; j++ )
            {
                if ( S[ i ][ j ] == 'O' ) cntO++;
                else if ( S[ i ][ j ] == 'X' ) cntX++;
                else if ( S[ i ][ j ] == 'T' ) cntT++;
            }
            if ( cntO + cntT == 4 ) winO = true;
            else if ( cntX + cntT == 4 ) winX = true;
        }
        for ( int j = 0; j < 4; j++ )
        {
            int cntO = 0, cntX = 0, cntT = 0;
            for ( int i = 0; i < 4; i++ )
            {
                if ( S[ i ][ j ] == 'O' ) cntO++;
                else if ( S[ i ][ j ] == 'X' ) cntX++;
                else if ( S[ i ][ j ] == 'T' ) cntT++;
            }
            if ( cntO + cntT == 4 ) winO = true;
            else if ( cntX + cntT == 4 ) winX = true;
        }
        int cntO = 0, cntX = 0, cntT = 0;
        for ( int i = 0; i < 4; i++ )
        {
            if ( S[ i ][ i ] == 'O' ) cntO++;
            else if ( S[ i ][ i ] == 'X' ) cntX++;
            else if ( S[ i ][ i ] == 'T' ) cntT++;
        }
        if ( cntO + cntT == 4 ) winO = true;
        else if ( cntX + cntT == 4 ) winX = true;
        cntO = 0; cntX = 0; cntT = 0;
        for ( int i = 0; i < 4; i++ )
        {
            if ( S[ 3 - i ][ i ] == 'O' ) cntO++;
            else if ( S[ 3 - i ][ i ] == 'X' ) cntX++;
            else if ( S[ 3 - i ][ i ] == 'T' ) cntT++;
        }
        if ( cntO + cntT == 4 ) winO = true;
        else if ( cntX + cntT == 4 ) winX = true;

        printf( "Case #%d: ", cnt );
        if ( winO ) printf( "O won\n" );
        else if ( winX ) printf( "X won\n" );
        else
        {
            bool found = false;
            for ( int i = 0; i < 4; i++ )
                for ( int j = 0; j < 4; j++ )
                    if ( S[ i ][ j ] == '.' )
            {
                found = true;
                break;
            }
            if ( found ) printf( "Game has not completed\n" );
            else printf( "Draw\n" );
        }
    }

    return 0;
}
