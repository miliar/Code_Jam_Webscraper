#include <iostream>
#include <fstream>
#include <map>

using namespace std;
const int MIN_NUM_ARGUMENTS = 2;
const int MAX_NO_OF_BUTTON_PRESS = 100;

int main( int argc, char* argv[] )
{
	if (argc < MIN_NUM_ARGUMENTS)
		cout << "Please enter the in file name!";

	ifstream aInFile;
	ofstream aOutFile;

	aInFile.open( argv[1] );
	aOutFile.open( argv[2] );

	int aNoOfTestCases = 0;
	aInFile >> aNoOfTestCases;

	cout << "No Of TestCases: " << aNoOfTestCases << endl;
	for( int i = 0; i < aNoOfTestCases; i++ )
	{
		int aNoOfButtons = 0;
		aInFile >> aNoOfButtons;

		char aNextMove[ MAX_NO_OF_BUTTON_PRESS ];
		char aOrangeMoves[ MAX_NO_OF_BUTTON_PRESS ];
		char aBlueMoves[ MAX_NO_OF_BUTTON_PRESS ];

		int aOrangeTotal = 0;
		int aBlueTotal = 0;
		int aTotalMoves = 0;

		for( int j = 0; j < aNoOfButtons; j++ )
		{
			char aNextChance;
			int aNextChanceButton;
			aInFile >> aNextChance;
			aInFile >> aNextChanceButton;

			aNextMove[ j ] = aNextChance;
			if( aNextChance == 'O' )
			{
				aOrangeMoves[ aOrangeTotal ]= aNextChanceButton;
				aOrangeTotal += 1;
			}
			else
			{
				aBlueMoves[ aBlueTotal ] = aNextChanceButton;
				aBlueTotal += 1;
			}
		}

		bool aOrangeNotPresent = false;
		bool aBlueNotPresent = false;
		aOrangeNotPresent = ( aOrangeTotal != 0 ? false : true );
		aBlueNotPresent = ( aBlueTotal != 0 ? false : true );

		int aOrangeCounter = 0;
		int aBlueCounter = 0;

		int aOrangeCurrentPos = 1;
		int aBlueCurrentPos = 1;
		for( int j = 0; j < aNoOfButtons; j++ )
		{
			int aCounter = 0;
			if( aNextMove[j] == 'O' )
			{
				int aNextOrangePos = aOrangeMoves[ aOrangeCounter ];
				if( aNextOrangePos != aOrangeCurrentPos )
				{
					aCounter = ( (aNextOrangePos < aOrangeCurrentPos) ? (aOrangeCurrentPos - aNextOrangePos) : (aNextOrangePos - aOrangeCurrentPos) ) + 1;
					aOrangeCurrentPos = aNextOrangePos;
				}
				else
				{
					aCounter++;
				}
				aOrangeCounter++;

				if( !aBlueNotPresent )
				{
					int aBlueNextPos = aBlueMoves[ aBlueCounter ];
					if( aBlueNextPos != aBlueCurrentPos )
					{
						int aBlueMovesReq = ( aBlueNextPos > aBlueCurrentPos) ? (aBlueNextPos - aBlueCurrentPos) : (aBlueCurrentPos - aBlueNextPos);
						if( aCounter < aBlueMovesReq )
							aBlueCurrentPos = ( aBlueNextPos > aBlueCurrentPos)? (aBlueCurrentPos + aCounter) : (aBlueCurrentPos - aCounter);
						else
							aBlueCurrentPos = aBlueNextPos;
					}
				}
			}
			else
			{
				int aNextBluePos = aBlueMoves[ aBlueCounter ];
				if( aNextBluePos != aBlueCurrentPos )
				{
					aCounter = ( (aNextBluePos < aBlueCurrentPos) ? (aBlueCurrentPos - aNextBluePos) : (aNextBluePos - aBlueCurrentPos) )+ 1;
					aBlueCurrentPos = aNextBluePos;
				}
				else
				{
					aCounter++;
				}
				aBlueCounter++;

				if( !aOrangeNotPresent )
				{
					int aOrangeNextPos = aOrangeMoves[ aOrangeCounter ];
					if( aOrangeNextPos != aOrangeCurrentPos )
					{
						int aOrangeMovesReq = ( aOrangeNextPos > aOrangeCurrentPos) ? (aOrangeNextPos - aOrangeCurrentPos) : (aOrangeCurrentPos - aOrangeNextPos);
						if( aCounter < aOrangeMovesReq )
							aOrangeCurrentPos = ( aOrangeNextPos > aOrangeCurrentPos)? (aOrangeCurrentPos + aCounter) : (aOrangeCurrentPos - aCounter);
						else
							aOrangeCurrentPos = aOrangeNextPos;
					}
				}
			}
			aTotalMoves += aCounter;
		}
		cout << "Case #" << (i + 1) << ": " << aTotalMoves << endl;
		aOutFile << "Case #" << (i + 1) << ": " << aTotalMoves << endl;
	}

	return 1;
}