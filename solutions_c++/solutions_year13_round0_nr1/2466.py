#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>

void main()
{
	FILE *fin  = fopen( "in.txt", "r" );
	assert( fin );

	int nCases;
	assert( fscanf( fin, "%d\n", &nCases ) == 1 );

	FILE *fout = fopen( "out.txt", "w" );

	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		char board[4][4];
		char c;

		int y, x;
		for( int y = 0; y < 4; y++ )
		{
			for( int x = 0; x < 4; x++ )
			{
				c = fgetc( fin );
				assert( c == 'X' || c == 'O' || c == '.' || c == 'T' );
				board[y][x] = c;
			}
			fgetc( fin );
		}

		fgetc( fin );

		bool xwon, owon;
		bool xcanwin = false, ocanwin = false;
		for( y = 0; y < 4; y++ )
		{
			xwon = true;
			owon = true;

			bool local_xcanwin = true, local_ocanwin = true;
			for( x = 0; x < 4; x++ )
			{
				if ( board[y][x] != 'X' && board[y][x] != 'T' )
					xwon = false;
				if ( board[y][x] != 'O' && board[y][x] != 'T' )
					owon = false;

				if ( board[y][x] == 'X' ) local_ocanwin = false;
				if ( board[y][x] == 'O' ) local_xcanwin = false;
			}
			if ( local_xcanwin ) xcanwin = true;
			if ( local_ocanwin ) ocanwin = true;

			if ( xwon || owon ) break;
		}

		if ( xwon || owon )
			goto next;

		for( x = 0; x < 4; x++ )
		{
			xwon = true;
			owon = true;

			bool local_xcanwin = true, local_ocanwin = true;
			for( y = 0; y < 4; y++ )
			{
				if ( board[y][x] != 'X' && board[y][x] != 'T' )
					xwon = false;
				if ( board[y][x] != 'O' && board[y][x] != 'T' )
					owon = false;
				if ( board[y][x] == 'X' ) local_ocanwin = false;
				if ( board[y][x] == 'O' ) local_xcanwin = false;
			}
			if ( local_xcanwin ) xcanwin = true;
			if ( local_ocanwin ) ocanwin = true;

			if ( xwon || owon ) break;
		}


		{
			xwon = true;
			owon = true;
			bool local_xcanwin = true, local_ocanwin = true;
			for( x = 0; x < 4; x++ )
			{
				if ( board[x][x] != 'X' && board[x][x] != 'T' )
					xwon = false;
				if ( board[x][x] != 'O' && board[x][x] != 'T' )
					owon = false;
				if ( board[x][x] == 'X' ) local_ocanwin = false;
				if ( board[x][x] == 'O' ) local_xcanwin = false;
			}
			if ( local_xcanwin ) xcanwin = true;
			if ( local_ocanwin ) ocanwin = true;

			if ( xwon || owon ) goto next;
		}

		{
			xwon = true;
			owon = true;
			bool local_xcanwin = true, local_ocanwin = true;
			for( x = 0; x < 4; x++ )
			{
				if ( board[x][3-x] != 'X' && board[x][3-x] != 'T' )
					xwon = false;
				if ( board[x][3-x] != 'O' && board[x][3-x] != 'T' )
					owon = false;
				if ( board[x][3-x] == 'X' ) local_ocanwin = false;
				if ( board[x][3-x] == 'O' ) local_xcanwin = false;
			}
			if ( local_xcanwin ) xcanwin = true;
			if ( local_ocanwin ) ocanwin = true;

			if ( xwon || owon ) goto next;
		}

next:
		assert( !( xwon && owon ) );

		fprintf( fout, "Case #%d: ", iCase + 1 );
		if ( xwon || ( xcanwin && !ocanwin ) )
			fprintf( fout, "X won", iCase + 1 );
		else if ( owon || ( ocanwin && !xcanwin ) )
			fprintf( fout, "O won", iCase + 1 );
		else if ( xcanwin || ocanwin )
			fprintf( fout, "Game has not completed", iCase + 1 );
		else
			fprintf( fout, "Draw", iCase + 1 );
		fprintf( fout, "\n" );
	}

	fclose( fin );
	fclose( fout );
}
