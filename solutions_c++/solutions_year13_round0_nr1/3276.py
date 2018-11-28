#include "stdafx.h"
#include <iostream>

#define BOARD_HEIGHT 4
#define BOARD_WIDTH  4

enum RESULT
{
	X_WON,
	O_WON,
	DRAW,
	GAME_NOT_COMPLETE,
};

typedef struct {
	char cells[ BOARD_HEIGHT ][ 32 ];
} BOARD;

static RESULT TicTacToe_CalcState( BOARD& board )
{
	bool gameNotComplete = false;

	// 1. calc rows and columns
	for( int i = 0; i < BOARD_HEIGHT; i++ )
	{
		int X_WON_ROW    = 0;
		int O_WON_ROW    = 0;
		int X_WON_COLUMN = 0;
		int O_WON_COLUMN = 0;
		for( int j = 0; j < BOARD_WIDTH; j++ )
		{
			// track across rows
			if( board.cells[i][j] == 'X' )      X_WON_ROW++;
			else if( board.cells[i][j] == 'O' ) O_WON_ROW++;
			else if( board.cells[i][j] == 'T' )
			{
				X_WON_ROW++;
				O_WON_ROW++;
			}
			else if( board.cells[i][j] == '.' )
			{
				gameNotComplete = true;
			}
			else
			{
				// WTH!
				printf( "Invalid input %c\n", board.cells[i][j] );
			}

			// track across columns
			if( board.cells[j][i] == 'X' )      X_WON_COLUMN++;
			else if( board.cells[j][i] == 'O' ) O_WON_COLUMN++;
			else if( board.cells[j][i] == 'T' )
			{
				X_WON_COLUMN++;
				O_WON_COLUMN++;
			}
		}

		if( X_WON_ROW >= 4 || X_WON_COLUMN >= 4 )
		{
			return RESULT::X_WON;
		}
		else if( O_WON_ROW >= 4 || O_WON_COLUMN >= 4 )
		{
			return RESULT::O_WON;
		}
	}

	// 2. calc diagonals

	// top left to bottom right
	int X_WON_DIAGNOALS = 0;
	int O_WON_DIAGNOALS = 0;
	for ( int i = 0; i < BOARD_WIDTH; i++ )
	{
		if( board.cells[i][i] == 'X' )      X_WON_DIAGNOALS++;
		else if( board.cells[i][i] == 'O' ) O_WON_DIAGNOALS++;
		else if( board.cells[i][i] == 'T' )
		{
			X_WON_DIAGNOALS++;
			O_WON_DIAGNOALS++;
		}

		if( X_WON_DIAGNOALS >= 4 )
		{
			return RESULT::X_WON;
		}
		else if( O_WON_DIAGNOALS >= 4 )
		{
			return RESULT::O_WON;
		}
	}

	// bottom left to top right
	X_WON_DIAGNOALS = 0;
	O_WON_DIAGNOALS = 0;
	for ( int i = BOARD_WIDTH - 1; i >= 0; i-- )
	{
		int j = BOARD_WIDTH - 1 - i;
		if( board.cells[i][j] == 'X' )      X_WON_DIAGNOALS++;
		else if( board.cells[i][j] == 'O' ) O_WON_DIAGNOALS++;
		else if( board.cells[i][j] == 'T' )
		{
			X_WON_DIAGNOALS++;
			O_WON_DIAGNOALS++;
		}

		if( X_WON_DIAGNOALS >= 4 )
		{
			return RESULT::X_WON;
		}
		else if( O_WON_DIAGNOALS >= 4 )
		{
			return RESULT::O_WON;
		}
	}


	if( gameNotComplete )
	{
		// 3. game has not completed
		return RESULT::GAME_NOT_COMPLETE;
	}
	else
	{
		// 4. draw
		return RESULT::DRAW;
	}
}

static void TicTacToe_ReadInput()
{
	char  Buffer[ 32 ];
	int  numBoards;

	// read number of boards
	scanf( "%d", &numBoards );

	for( int i = 0; i < numBoards; ++i )
	{
		// read board info
		BOARD board;
		memset( &board, 0, sizeof(board) );
		for( int j = 0; j < BOARD_HEIGHT; j++ )
		{
			// scan row info
			scanf( "%s", board.cells[j] );
		}

		// calc results
		RESULT result = TicTacToe_CalcState( board );

		// output results
		switch( result )
		{
		case X_WON:
			printf( "Case #%d: X won\n", i + 1 );
			break;
		case O_WON:
			printf( "Case #%d: O won\n", i + 1 );
			break;
		case DRAW:
			printf( "Case #%d: Draw\n", i + 1 );
			break;
		case GAME_NOT_COMPLETE:
			printf( "Case #%d: Game has not completed\n", i + 1 );
			break;
		}
	}

	scanf( "%s", Buffer );
}

int _tmain(int argc, _TCHAR* argv[])
{
	TicTacToe_ReadInput();

	return( 0 );
}

