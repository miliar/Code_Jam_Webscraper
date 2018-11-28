
#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

ofstream outfile;
ifstream infile;

void setup()
{
	infile.open( "input.in");
	outfile.open( "output.txt");
}

void cleanup()
{
	infile.close();
	outfile.close();
}

int main()
{
	setup();

	int numberOfPuzzles;
	infile >> numberOfPuzzles;

	for( int i = 0; i < numberOfPuzzles; i ++)
	{
		int numberOfGooglers;
		infile >> numberOfGooglers;
		int numberOfSuprises;
		infile >> numberOfSuprises;
		int minimumBestResult;
		infile >> minimumBestResult;

		int googlerScores[100];
		for( int j = 0; j < numberOfGooglers; j ++)
		{
			infile >> googlerScores[j];
		}

		// calculate the minimum automatic best result without suprising
		int minimumNoSuprise = minimumBestResult * 3 - 2; // for 8, this would be 7+7+8 or 8+(8-1)+(8-1)
		// calculate the minimum can-be-best-if-suprising
		int minimumWithSuprise = minimumBestResult * 3 - 4; // for 8 this would be 6+6+8 or 8+(8-2)+(8-2)

		if( minimumNoSuprise < 0)
		{
			minimumNoSuprise = 0;
		}
		if( minimumWithSuprise < 0)
		{
			minimumWithSuprise = 0;
		}

		// outlying cases
		if( minimumBestResult == 1)
		{
			minimumWithSuprise = 0;
		}
		if( minimumBestResult == 0)
		{
			minimumWithSuprise = 0;
		}

		int cando = 0;
		int boarderlineCount = 0;
		for( int j = 0; j < numberOfGooglers; j ++)
		{
			if( googlerScores[j] >= minimumBestResult)
			{
				if( googlerScores[j] >= minimumNoSuprise)
				{
					cando ++;
				}
				else if( googlerScores[j] == minimumWithSuprise || googlerScores[j] == minimumWithSuprise + 1) // 6,6,8 or 6,7,8
				{
					boarderlineCount ++;
				}
			}
		}
		if( boarderlineCount > numberOfSuprises)
		{
			cando += numberOfSuprises;
		}
		else
		{
			cando += boarderlineCount;
		}

		cout << "Case #" << (i+1) << ": " << cando << endl;
		outfile << "Case #" << (i+1) << ": " << cando << endl;
	}

	cleanup();
	system("pause");
}

