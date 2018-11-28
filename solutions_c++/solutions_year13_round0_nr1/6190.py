#include <stdio.h>

int main()
{
	FILE* fIn;
	FILE* fOut;
	fIn = fopen("A-large.in", "r");
	fOut = fopen("output.txt", "w");
	int Test_case;
	fscanf( fIn, "%d", &Test_case );
	for( int tc = 1 ; tc <= Test_case ; tc++ )
	{
		int count_X = 0;
		int count_O = 0;
		int count_T = 0;
		bool end = false;
		bool full = true;
		char board[5][5];
		for( int i = 0 ; i < 4 ; i++ )
		{
			fscanf( fIn, "%s", board[i] );
			for( int j = 0 ; j < 4 ; j++ )
			{
				if( board[i][j] == '.' )
				{
					full = false;
				}
			}
		}
		for( int i = 0 ; i < 4 ; i++ )
		{
			if( end == true )
			{
				break;
			}
			for( int j = 0 ; j < 4 ; j++ )
			{
				if( board[i][j] == 'X' )
				{
					count_X++;
				}
				else if( board[i][j] == 'O' )
				{
					count_O++;
				}
				else if( board[i][j] == 'T' )
				{
					count_T++;
				}
			}
			if( count_T < 4 && count_X+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: X won\n", tc);
				end = true;
			}
			else if( count_T < 4 && count_O+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: O won\n", tc);
				end = true;
			}
			else
			{
				count_O = 0;
				count_X = 0;
				count_T = 0;
			}
		}
		for( int j = 0 ; j < 4 ; j++ )
		{
			if( end == true )
			{
				break;
			}
			for( int i = 0 ; i < 4 ; i++ )
			{
				if( board[i][j] == 'X' )
				{
					count_X++;
				}
				else if( board[i][j] == 'O' )
				{
					count_O++;
				}
				else if( board[i][j] == 'T' )
				{
					count_T++;
				}
			}
			if( count_T < 4 && count_X+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: X won\n", tc);
				end = true;
			}
			else if( count_T < 4 && count_O+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: O won\n", tc);
				end = true;
			}
			else
			{
				count_O = 0;
				count_X = 0;
				count_T = 0;
			}
		}
		if( end == false )
		{
			for( int i = 0 ; i < 4 ; i++ )
			{
				if( board[i][i] == 'X' )
				{
					count_X++;
				}
				else if( board[i][i] == 'O' )
				{
					count_O++;
				}
				else if( board[i][i] == 'T' )
				{
					count_T++;
				}
			}
			if( count_T < 4 && count_X+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: X won\n", tc);
				end = true;
			}
			else if( count_T < 4 && count_O+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: O won\n", tc);
				end = true;
			}
			else
			{
				count_X = 0;
				count_O = 0;
				count_T = 0;
			}
		}
		if( end == false )
		{
			int temp = 3;
			for( int i = 0 ; i < 4 ; i++ )
			{
				if( board[i][temp] == 'X' )
				{
					count_X++;
				}
				else if( board[i][temp] == 'O' )
				{
					count_O++;
				}
				else if( board[i][temp] == 'T' )
				{
					count_T++;
				}
				temp--;
			}
			if( count_T < 4 && count_X+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: X won\n", tc);
				end = true;
			}
			else if( count_T < 4 && count_O+count_T == 4 )
			{
				fprintf( fOut, "Case #%d: O won\n", tc);
				end = true;
			}
			else
			{
				count_X = 0;
				count_O = 0;
				count_T = 0;
			}
		}
		if( end == false )
		{
			if( full == true )
			{
				fprintf( fOut, "Case #%d: Draw\n", tc);
			}
			else
			{
				fprintf( fOut, "Case #%d: Game has not completed\n", tc );
			}
		}
	}
	return 0;
}