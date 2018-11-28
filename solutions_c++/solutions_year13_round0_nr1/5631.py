#include <iostream>
#include <string>

using namespace std;

int counter = 0;

bool isSame( char c1, char c2 )
{
	if( c1 != '.' && ( c1 == c2 || c1 == 'T' || c2=='T' ) )
		return true;
	return false;
}

void printWinner( bool xWon )
{
	cout << "Case #" << counter << ": ";
	if( xWon )
	{
		cout << "X won" << endl;
	}
	else
	{
		cout << "O won" << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	
	char table[4][4];
	
	while( T-- )
	{
		counter++;
		
		string str;
		bool findDot = false;
		
		for (int i = 0; i < 4; i++)
		{
			cin >> str;
			
			for (int j = 0; j < 4; j++)
			{
				table[i][j] = str[j];
				
				if( str[j] == '.' )
					findDot = true;
			}
		}
		
		bool xWon = false;
		bool oWon = false;
		
		for (int i = 0; i < 4; i++)
		{
			if( isSame( table[i][0], table[i][1] ) 
			    && isSame( table[i][1], table[i][2] )
			    && isSame( table[i][2], table[i][3] ) )
			{
				if( table[i][0] == 'X' || table[i][1] == 'X' )
				{
					xWon = true;
					break;
				}
				else
				{
					oWon = true;
					break;
				}
			}

			if( isSame( table[0][i], table[1][i] ) 
			    && isSame( table[1][i], table[2][i] )
			    && isSame( table[2][i], table[3][i] ) )
			{
				if( table[0][i] == 'X' || table[1][i] == 'X' )
				{
					xWon = true;
					break;
				}
				else
				{
					oWon = true;
					break;
				}
			}
		}

		if( xWon || oWon )
		{
			printWinner( xWon );
			continue;
		}
		
		// ghotr

		if( isSame( table[0][3], table[1][2] ) 
			&& isSame( table[1][2], table[2][1] )
			&& isSame( table[2][1], table[3][0] ) )
		{
			if( table[3][0] == 'X' || table[0][3] == 'X' )
			{
				xWon = true;
			}
			else
			{
				oWon = true;
			}
		}

		if( isSame( table[0][0], table[1][1] ) 
			&& isSame( table[1][1], table[2][2] )
			&& isSame( table[2][2], table[3][3] ) )
		{
			if( table[0][0] == 'X' || table[1][1] == 'X' )
			{
				xWon = true;
			}
			else
			{
				oWon = true;
			}
		}


		if( xWon || oWon )
		{
			printWinner( xWon );
			continue;
		}
		
		cout << "Case #" << counter << ": ";
		
		if( findDot )
		{
			cout << "Game has not completed" << endl;
		}
		else
		{
			cout << "Draw" << endl;
		}
	}
	
	return 0;
}
