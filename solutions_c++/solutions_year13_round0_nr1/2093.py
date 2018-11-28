#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#define BOARD_SIZE 4

int board [ BOARD_SIZE ] [ BOARD_SIZE ];

enum TPiece { EMPTY = '.', PLAYER_X = 'X', PLAYER_Y = 'O', JOKER = 'T' };
enum TRes { WIN_X, WIN_Y, INCOMPLETE, DRAW };
void _print ( void )
{
    for ( int i = 0; i < BOARD_SIZE; i ++ )
    {
        for ( int j = 0; j < BOARD_SIZE; j ++ )
            printf ( "%c", board [ i ] [ j ] );
        printf ( "\n" );
    }

    printf ( "-------\n" );
}

void Load ( void )
{
    memset ( board, 0, sizeof ( board ) );

    for ( int i = 0; i < BOARD_SIZE; i++ )
    {
        for ( int j = 0; j < BOARD_SIZE; j++ )
            board [ i ] [ j ] = getchar ( );

        assert ( getchar ( ) == '\n' );
    }
    assert ( getchar ( ) == '\n' );
   //  _print ( );
}

int Solve ( void )
{
    // check radky + zaplnenou tabulku
    int cntTable = 0;
    for ( int i = 0; i < BOARD_SIZE ; i++ )
    {
        int cntX = 0, cntY = 0;

        for ( int j = 0; j < BOARD_SIZE; j++ )
        {
            if ( board [ i ] [ j ] != EMPTY )
                cntTable += 1;

            switch ( board [ i ] [ j ] )
            {
                case PLAYER_X:  cntX += 1;              break;
                case PLAYER_Y:  cntY += 1;              break;
                case JOKER:     cntX += 1; cntY += 1;   break;
            }
        }

        if ( cntX == 4 )
            return WIN_X;
        if ( cntY == 4 )
            return WIN_Y;
    }

    // check sloupce
    for ( int j = 0; j < BOARD_SIZE ; j ++ )
    {
        int cntX = 0, cntY = 0;

        for ( int i = 0; i < BOARD_SIZE; i ++ )
        {
            switch ( board [ i ] [ j ] )
            {
                case PLAYER_X:  cntX += 1;              break;
                case PLAYER_Y:  cntY += 1;              break;
                case JOKER:     cntX += 1; cntY += 1;   break;
            }
        }

        if ( cntX == 4 )
            return WIN_X;
        if ( cntY == 4 )
            return WIN_Y;
    }

    // check uhlopricku
    int cntX = 0; int cntY = 0;
    for ( int i = 0; i < BOARD_SIZE; i++ )
    {
        switch ( board [ i ] [ i ] )
        {
            case PLAYER_X:  cntX += 1;              break;
            case PLAYER_Y:  cntY += 1;              break;
            case JOKER:     cntX += 1; cntY += 1;   break;
        }
    }
    if ( cntX == 4 ) return WIN_X;
    if ( cntY == 4 ) return WIN_Y;

    cntX = cntY = 0;
    for ( int i = BOARD_SIZE - 1; i >= 0; i -- )
    {
        switch ( board [ 3 - i ] [ i ] )
        {
            case PLAYER_X:  cntX += 1;              break;
            case PLAYER_Y:  cntY += 1;              break;
            case JOKER:     cntX += 1; cntY += 1;   break;
        }
    }
    if ( cntX == 4 ) return WIN_X;
    if ( cntY == 4 ) return WIN_Y;

    if ( cntTable != 16 )
        return INCOMPLETE;
    return DRAW;
}

int main ( void )
{
    int casesCnt;
    scanf ( "%d\n", & casesCnt );
    for ( int i = 1; i <= casesCnt; i++ )
    {
        Load ( );
        printf ( "Case #%d: ", i );
        switch ( Solve ( ) )
        {
            case INCOMPLETE:printf ( "Game has not completed" ); break;
            case WIN_X:     printf ( "X won" ); break;
            case WIN_Y:     printf ( "O won" ); break;
            case DRAW:      printf ( "Draw" ); break;
        }
        printf ( "\n" );
    }
    return EXIT_SUCCESS;
}
