#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;


enum SpaceType { NEITHER, PLAYERX, PLAYERO, BOTH };

enum GameResult { UNFINISHED, PLAYERX_WIN, PLAYERO_WIN, DRAW };

typedef char Game[4][4];

void printGame( Game agame )
{
	for (int i=0; i<4; ++i)
	{

		for (int j=0; j<4; ++j)
		{
			cout << agame[i][j];
		}

		cout << endl;
	}

	cout << endl;

}

GameResult checkGame( Game agame )
{
	bool full = true;

	int xsqrs = 0;
	int osqrs = 0;

	// check rows
	for (int i=0; i<4; ++i)
	{
		//cout << "checking row: " << i << endl;
		xsqrs = 0;
		osqrs = 0;

		for (int j=0; j<4; ++j)
		{
			//cout << i << j << agame[i][j] << endl;
			switch (agame[i][j])
			{

				case NEITHER:
					full = false;
					break;
				case PLAYERX:
					++xsqrs;
					break;
				case PLAYERO:
					++osqrs;
					break;
				case BOTH:
					++xsqrs;
					++osqrs;
					break;
			}
		}

		if (xsqrs==4)
			return PLAYERX_WIN;
		if (osqrs==4)
			return PLAYERO_WIN;
	}

	// check columns
	for (int i=0; i<4; ++i)
	{
		//cout << "checking column: " << i << endl;
		xsqrs = 0;
		osqrs = 0;

		for (int j=0; j<4; ++j)
		{
			switch (agame[j][i])
			{
				case NEITHER:
					full = false;
					break;
				case PLAYERX:
					++xsqrs;
					break;
				case PLAYERO:
					++osqrs;
					break;
				case BOTH:
					++xsqrs;
					++osqrs;
					break;
			}
		}

		if (xsqrs==4)
			return PLAYERX_WIN;
		if (osqrs==4)
			return PLAYERO_WIN;
	}

	// check first diagonal
	xsqrs = 0;
	osqrs = 0;

	//cout << "checking diagonal 1" << endl;
	for (int i=0; i<4; ++i)
	{
		switch (agame[i][i])
		{
			case NEITHER:
				full = false;
				break;
			case PLAYERX:
				++xsqrs;
				break;
			case PLAYERO:
				++osqrs;
				break;
			case BOTH:
				++xsqrs;
				++osqrs;
				break;
		}
	}

	if (xsqrs==4)
		return PLAYERX_WIN;
	if (osqrs==4)
		return PLAYERO_WIN;

	// check second diagonal
	xsqrs = 0;
	osqrs = 0;

	//cout << "checking diagonal 2" << endl;
	for (int i=0; i<4; ++i)
	{
		switch (agame[3-i][i])
		{
			case NEITHER:
				full = false;
				break;
			case PLAYERX:
				++xsqrs;
				break;
			case PLAYERO:
				++osqrs;
				break;
			case BOTH:
				++xsqrs;
				++osqrs;
				break;
		}
	}

	if (xsqrs==4)
		return PLAYERX_WIN;
	if (osqrs==4)
		return PLAYERO_WIN;

	// another result
	if (full == false)
		return UNFINISHED;

	return DRAW;

}

int main( int argc, const char* argv[] )
{
	
	ifstream myFile(argv[1]);
	int numGames = 0;

	if (myFile.is_open())
	{

		string line;
		getline (myFile, line);
   		stringstream convert(line);
   		convert >> numGames;
   		//cout << numGames << endl;

   		for (int i=0; i<numGames; ++i)
   		{
   			Game mygame;

   			for (int j=0; j<4; ++j)
   			{
   				getline(myFile, line);

   				//cout << "got a line: " << line << endl;

   				for (int k=0; k<4; ++k)
   				{
   	   				char space = line[k];

	   				switch (space)
	   				{
	   					case '.':
	   						mygame[j][k] = NEITHER;
	   						break;

	   					case 'X':
	   						mygame[j][k] = PLAYERX;
	   						break;

	   					case 'O':
	   						mygame[j][k] = PLAYERO;
	   						break;

	   					case 'T':
	   						mygame[j][k] = BOTH;
	   						break;
	   				}				
   				}

   			}

   			//printGame(mygame);

   			cout << "Case #" << (i+1) << ": ";

   			GameResult result = checkGame(mygame);
   			switch (result)
   			{
   				case UNFINISHED:
   					cout << "Game has not completed" << endl;
   					break;

   				case PLAYERX_WIN:
   					cout << "X won" << endl;
   					break;

   				case PLAYERO_WIN:
   					cout << "O won" << endl;
   					break;

   				case DRAW:
   					cout << "Draw" << endl;
   					break;
   			}

   			// advance
   			getline(myFile, line);
   		}
/*
		while ( myFile.good() )
		{
			getline (myFile, line);
			cout << line << endl;
		}
*/
	}

	

	/*
	// Prints each argument on the command line.
	for(int i = 0; i < argc; i++)
	{
		std::cout << i << " " << argv[i] << std::endl;
	}
	*/
}