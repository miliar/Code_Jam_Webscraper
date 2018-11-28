#include <stdio.h>

int T;
int column[2][4];
int row[2][4];
int diagram[2][2];
int threePow[] = { 1, 3, 9, 27 };
bool dotFlag = false;
bool ansFlag = false;
char temp;
int ans;

int main()
{
	scanf( "%d", &T );
	for( int p = 0; p < T; ++p )
	{
		for( int i = 0; i < 2; ++i )
		{
			for( int k = 0; k < 4; ++k )
			{
				column[i][k] = 0;
				row[i][k] = 0;
			}
			for( int k = 0; k < 2; ++k )
			{
				diagram[i][k] = 0;
			}
		}
		dotFlag = false;
		for( int i = 0; i < 4; ++i )
		{
			for( int j = 0; j < 4; ++j )
			{
				scanf( "%c", &temp );
				while( temp != 'X' && temp != 'O' && temp != 'T' && temp != '.' )
					scanf( "%c", &temp );
				switch( temp )
				{
				case '.':
					dotFlag = true;
					break;
				case 'X':
					column[0][i] += 1*threePow[j];
					column[1][i] += 1*threePow[j];
					row[0][j] += 1*threePow[i];
					row[1][j] += 1*threePow[i];
					if( i == j )
					{
						diagram[0][0] += 1*threePow[i];
						diagram[1][0] += 1*threePow[i];
					}
					if( ( i+ j ) == 3 )
					{
						diagram[0][1] += 1*threePow[i];
						diagram[1][1] += 1*threePow[i];
					}
					break;
				case 'O':
					column[0][i] += 2*threePow[j];
					column[1][i] += 2*threePow[j];
					row[0][j] += 2*threePow[i];
					row[1][j] += 2*threePow[i];
					if( i == j )
					{
						diagram[0][0] += 2*threePow[i];
						diagram[1][0] += 2*threePow[i];
					}
					if( ( i+ j ) == 3 )
					{
						diagram[0][1] += 2*threePow[i];
						diagram[1][1] += 2*threePow[i];
					}
					break;
				case 'T':
					column[0][i] += 1*threePow[j];
					column[1][i] += 2*threePow[j];
					row[0][j] += 1*threePow[i];
					row[1][j] += 2*threePow[i];
					if( i == j )
					{
						diagram[0][0] += 1*threePow[i];
						diagram[1][0] += 2*threePow[i];
					}
					if( ( i+ j ) == 3 )
					{
						diagram[0][1] += 1*threePow[i];
						diagram[1][1] += 2*threePow[i];
					}
					break;
				}
			}
		}

		ansFlag = false;
		for( int j = 0; j < 2; ++j )
		{
			for( int i = 0; i < 4; ++i )
			{
				if( column[j][i] == 27+9+3+1 )
				{
					printf( "Case #%d: X won\n", p+1 );
					ansFlag = true;
					break;
				}
				if( column[j][i] == 54+18+6+2 )
				{
					printf( "Case #%d: O won\n", p+1 );
					ansFlag = true;
					break;
				}
				if( row[j][i] == 27+9+3+1 )
				{
					printf( "Case #%d: X won\n", p+1 );
					ansFlag = true;
					break;
				}
				if( row[j][i] == 54+18+6+2 )
				{
					printf( "Case #%d: O won\n", p+1 );
					ansFlag = true;
					break;
				}
			}
			if( ansFlag )
				break;
			for( int i = 0; i < 2; ++i )
			{
				if( diagram[j][i] == 27+9+3+1 )
				{
					printf( "Case #%d: X won\n", p+1 );
					ansFlag = true;
					break;
				}
				if( diagram[j][i] == 54+18+6+2 )
				{
					printf( "Case #%d: O won\n", p+1 );
					ansFlag = true;
					break;
				}
			}
			if( ansFlag )
				break;
		}
		if( !ansFlag )
		{
			if( dotFlag )
				printf( "Case #%d: Game has not completed\n", p+1 );
			else
				printf( "Case #%d: Draw\n", p+1 );
		}
	}
	return 0;
}