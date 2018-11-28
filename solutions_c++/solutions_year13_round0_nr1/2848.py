#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for( int test = 1; test <= T; test++ )
	{
		const int rowsN=4, columnsN=4;
		
		int rows[2][4];
		int columns[2][4];
		memset( rows,0,sizeof rows );
		memset( columns,0,sizeof columns );

		int nothing = 0;

		int haveResult = 0;

		int diag[2][2];
		memset( diag, 0, sizeof diag );

		for(int r=0; r<rowsN; r++ )
		{
			for(int c=0;c<columnsN;c++)
			{
				bool isDiagonal1 = r==c;
				bool isDiagonal2 = 
					( c == 0 && r == 3 ) ||
					( c == 1 && r == 2 ) ||
					( c == 2 && r == 1 ) ||
					( c== 3 && r == 0 );

				char el;
				cin >> el;
				switch ( el )
				{
				case '.':
					nothing++;
					break;
				case 'X':
					rows[0][r]++;
					columns[0][c]++;
					if( isDiagonal1 )
					{
						diag[0][0]++;
					}
					else if( isDiagonal2 )
					{
						diag[0][1]++;
					}
					break;
				case 'O':
					rows[1][r]++;
					columns[1][c]++;
					if( isDiagonal1 )
					{
						diag[1][0]++;
					}
					else if( isDiagonal2 )
					{
						diag[1][1]++;
					}
					break;
				case 'T':
					rows[0][r]++;
					columns[0][c]++;
					rows[1][r]++;
					columns[1][c]++;
					if( isDiagonal1 )
					{
						diag[1][0]++;
						diag[0][0]++;
					}
					else if( isDiagonal2 )
					{
						diag[1][1]++;
						diag[0][1]++;
					}
					break;
				}

				if( rows[0][r] == 4 || columns[0][c] == 4 || diag[0][1] == 4 || diag[0][0] == 4 )
				{
					haveResult = 1;
				}
				else if( rows[1][r] == 4 || columns[1][c] == 4 || diag[1][1] == 4 || diag[1][0] == 4)
				{
					haveResult = 2;
				}
			}
		}
		
		cout << "Case #" << test << ": ";
		if( haveResult == 1 )
		{
			cout << "X won";
		}
		else if( haveResult == 2 )
		{
			cout << "O won";
		}
		else if( nothing > 0 )
		{
			cout << "Game has not completed";
		}
		else
		{
			cout << "Draw";
		}


		cout << endl;

		
	}

	return 0;
}