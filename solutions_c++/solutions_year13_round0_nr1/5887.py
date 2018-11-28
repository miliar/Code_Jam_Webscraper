#include <stdio.h>

int check( char board[][5] , int tx , int ty , char player )
{
        int flagRow;
        int flagCol;
        int i, j;

        if ( tx != -1 )
                board[tx][ty] = player;

        for ( i = 0 ; i < 4 ; ++i )
        {
                flagRow = 1;
                flagCol = 1;

                for ( j = 0 ; j < 4 ; ++j )
                {
                        if ( board[i][j] != player )
                        {
                                flagRow = 0;
                        }

                        if ( board[j][i] != player )
                        {
                                flagCol = 0;
                        }
                }

                if ( flagRow || flagCol ) return 1;
        }

        return ( ( player == board[0][0] && player == board[1][1] && player == board[2][2] && player == board[3][3] )
                || ( player == board[0][3] && player == board[1][2] && player == board[2][1] && player == board[3][0] ) );
}

int main()
{
        FILE *fpo;
        char board[4][5];
        int k, t;
        int i, j;
        int tx, ty;
        int hasEmpty;

        fpo = fopen( "D:\\Documents and Settings\\zilizh\\Desktop\\gcj\\gcja.out" , "w" );
        scanf( "%d" , &t );
        k = 1;
        while ( k <= t )
        {
                hasEmpty = 0;

                tx = -1;
                for ( i = 0 ; i < 4 ; ++i )
                {
                        scanf( "%s" , board[i] );
                        for ( j = 0 ; j < 4 ; ++j )
                        {
                                if ( board[i][j] == '.' )
                                        hasEmpty = 1;
                                if ( board[i][j] == 'T' )
                                {
                                        tx = i;
                                        ty = j;
                                }
                        }
                }

                fprintf( fpo , "Case #%d: " , k++ );

                if ( check( board , tx , ty , 'X' ) )
                {
                        fprintf( fpo , "X won\n" );
                }
                else if ( check( board , tx , ty , 'O' ) )
                {
                        fprintf( fpo , "O won\n" );
                }
                else if ( hasEmpty )
                {
                        fprintf( fpo , "Game has not completed\n" );
                }
                else
                {
                        fprintf( fpo , "Draw\n" );
                }
        }

        return 0;
}
