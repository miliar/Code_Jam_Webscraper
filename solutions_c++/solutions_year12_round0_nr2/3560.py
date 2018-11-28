#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

class Checker
{
public: 
	bool m_canBeSupr ( int number )
	{
		if ( number > 1 && number < 29 )
			return true;
		else
			return false;
	};
	int m_MaxOfSupr ( int number )
	{
		if ( number % 3 == 0 )
			return ( ( number / 3 ) + 1 );
		else if ( number % 3 == 1 )
			return ( ( number / 3 ) + 1 );
		else if ( number % 3 == 2 )
			return ( ( number / 3 ) + 2 );
	};
	int m_MaxOfNonSupr ( int number )
	{
		if ( number % 3 == 0 )
			return ( number / 3 );
		else if ( number % 3 == 1 )
			return ( ( number / 3 ) + 1 );
		else if ( number % 3 == 2 )
			return ( ( number / 3 ) + 1 );
	}
};

int main()
{
	FILE *input, *output;
	unsigned char InputSymbol = 0;
	int a, numberOfTests, i, j, result [ 100 ], numberOfGooglers, numberOfSurprises, maxScore;
	int *googlerPoints [ 100 ];
	Checker checker;
	if ( ( input = fopen ( "C:\\test.txt", "r" ) ) == 0 )
		return -1;
	fscanf ( input, "%d", &numberOfTests );
	for ( i = 0 ; i < numberOfTests; i++ )
	{
		fscanf ( input, "%d", &numberOfGooglers );
		fscanf ( input, "%d", &numberOfSurprises );
		fscanf ( input, "%d", &maxScore );
		googlerPoints [ i ] = new int [ numberOfGooglers ] ;
		result [ i ] = 0;
		for ( j = 0; j < numberOfGooglers; j++ )
		{
			fscanf ( input, "%d", ( googlerPoints [ i ] + j ) );
		}
		for ( j = 0; j < numberOfGooglers; j++ )
		{
			if ( (a = checker . m_MaxOfNonSupr ( googlerPoints [ i ][ j ] )) >= maxScore )
			{
				result [ i ] ++;
			}
			else if ( checker . m_canBeSupr ( googlerPoints [ i ][ j ] ) && numberOfSurprises > 0 )
			{
				if ( (a = checker . m_MaxOfSupr ( googlerPoints [ i ][ j ] )) >= maxScore )
				{
					numberOfSurprises--;
					result [ i ] ++;
				}
			}
		}
	}
	fclose ( input );
	if ( ( output = fopen ( "C:\\Output.txt", "w" ) ) == 0 )
		return -1;
	for ( i = 0; i < numberOfTests; i++ )
	{
		fprintf ( output, "Case #%d: %d\n", i+1, result[i]);
	}
	fclose ( output );
	return 0;
}