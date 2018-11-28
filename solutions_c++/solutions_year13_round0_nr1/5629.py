#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char board[4][4];

void displayInput();

int main( int argc, char* argv[] )
{
	string fileName = string( argv[1] );
	ifstream inputFile( fileName );
	ofstream outputFile( "output.txt" );

	int numTest;
	inputFile >> numTest;

	for ( int k = 1; k <= numTest; k++ )
	{
		bool end = false;

		for ( int i = 0; i < 4; i++ )
			inputFile >> board[i];

		displayInput();

		for ( int i = 0; i < 4; i++ )
		{
			if ( ( board[i][0] != 'T'  && board[i][0] != '.' )
				&& ( board[i][0] == board[i][1] || board[i][1] == 'T' ) 
				&& ( board[i][0] == board[i][2] || board[i][2] == 'T' )
				&& ( board[i][0] == board[i][3] || board[i][3] == 'T' ) )
			{
				outputFile << "Case #" << k << ": " << board[i][0] << " won" << endl;
				end = true;
				break;
			}
			else if ( board[i][0] == 'T' && board[i][1] != '.' && board[i][1] == board[i][2] && board[i][1] == board[i][3] )
			{
				outputFile << "Case #" << k << ": " << board[i][1] << " won" << endl;
				end = true;
				break;
			}
		}

		if ( end )
			continue;

		for ( int i = 0; i < 4; i++ )
		{
			if ( ( board[0][i] != 'T'  && board[0][i] != '.' )
				&& ( board[0][i] == board[1][i] || board[1][i] == 'T' )
				&& ( board[0][i] == board[2][i] || board[2][i] == 'T' )
				&& ( board[0][i] == board[3][i] || board[3][i] == 'T' ) )
			{
				outputFile << "Case #" << k << ": " << board[0][i] << " won" << endl;
				end = true;
				break;
			}
			else if ( board[0][i] == 'T' && board[1][i] != '.' && board[1][i] == board[2][i] && board[1][i] == board[3][i] )
			{
				outputFile << "Case #" << k << ": " << board[1][i] << " won" << endl;
				end = true;
				break;
			}
		}

		if ( end )
			continue;

		if ( ( board[0][0] != 'T'  && board[0][0] != '.' )
				&& ( board[0][0] == board[1][1] || board[1][1] == 'T' ) 
				&& ( board[0][0] == board[2][2] || board[2][2] == 'T' )
				&& ( board[0][0] == board[3][3] || board[3][3] == 'T' ) )
			{
				outputFile << "Case #" << k << ": " << board[0][0] << " won" << endl;
				end = true;
			}
			else if ( board[0][0] == 'T' && board[1][1] != '.' && board[1][1] == board[2][2] && board[1][1] == board[3][3] )
			{
				outputFile << "Case #" << k << ": " << board[1][1] << " won" << endl;
				end = true;
			}

		if ( end )
			continue;

		if ( ( board[0][3] != 'T'  && board[0][3] != '.' )
				&& ( board[0][3] == board[1][2] || board[1][2] == 'T' ) 
				&& ( board[0][3] == board[2][1] || board[2][1] == 'T' )
				&& ( board[0][3] == board[3][0] || board[3][0] == 'T' ) )
		{
			outputFile << "Case #" << k << ": " << board[0][3] << " won" << endl;
			end = true;
		}
		else if ( board[0][3] == 'T' && board[1][2] != '.' && board[1][2] == board[2][1] && board[1][2] == board[3][0] )
		{
			outputFile << "Case #" << k << ": " << board[1][2] << " won" << endl;
			end = true;
		}

		if ( end )
			continue;

		for ( int i = 0; i < 4; i++ )
		{
			int j = 0;

			while ( board[i][j] != '.'  && j < 4 )
			{
				j++;

				if ( i == 3 && j == 3 )
				{
					outputFile << "Case #" << k << ": " "Draw" << endl;
					end = true;
				}
			}
		}

		if ( end )
			continue;

		outputFile << "Case #" << k << ": " "Game has not completed" << endl;	
	}

	inputFile.close();
	outputFile.close();

	system( "PAUSE" );
	return 0;
}

void displayInput()
{
	for ( int i = 0; i < 4; i++ )
	{
		for ( int j = 0; j < 4; j ++ )
			cout << board[i][j];
		cout << endl;
	}
	cout << endl;
}