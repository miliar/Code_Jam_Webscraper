#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int ProcessMoves(std::vector < std::pair < char, int > > & moves);

int main(void)
{
	ifstream                                input;
	int                                     move      = 0;
	int                                     moves     = 0;
	int                                     testCase  = 0;
	int                                     testCases = 0;
	ofstream                                output;
	std::pair < char, int >                 pair;
	std::vector < std::pair < char, int > > movesVector;

	//----------------------------------------------------------------------------------------------
	//  Open the input file.
	//----------------------------------------------------------------------------------------------
	input.open("A-small.in");
	if (false == input.is_open())
	{
		cout << "Unable to open input file!" << endl;
		return 1;
	}

	//----------------------------------------------------------------------------------------------
	//  Open the output file.
	//----------------------------------------------------------------------------------------------
	output.open("A-small.out");
	if (false == output.is_open())
	{
		cout << "Unable to open output file!" << endl;
		input.close();
		return 2;
	}

	//----------------------------------------------------------------------------------------------
	//  Load the input file.
	//----------------------------------------------------------------------------------------------
	input >> testCases;

	//----------------------------------------------------------------------------------------------
	//  Read all the test cases.
	//----------------------------------------------------------------------------------------------
	for (testCase = 1; testCase <= testCases; testCase++)
	{
		//------------------------------------------------------------------------------------------
		//  Read all the moves of the test case.
		//------------------------------------------------------------------------------------------
		input >> moves;
		for (move = 0; move < moves; move++)
		{
			input >> pair.first;
			input >> pair.second;
			movesVector.push_back(pair);
		}

		output << "Case #" << testCase << ": " << ProcessMoves(movesVector) << endl;
		movesVector.erase(movesVector.begin(), movesVector.end());
	}

	input.close();
	output.close();

	return 0;
}

int ProcessMoves(std::vector < std::pair < char, int > > & moves)
{
	int    bluePosition   = 1;
	int    blueTime       = 0;
	int    moveTime       = 0;
	int    orangePosition = 1;
	int    orangeTime     = 0;
	int    time           = 0;
	size_t move;

	for (move = 0; move < moves.size(); move++)
	{
		switch (moves[move].first)
		{
			case 'B':
				moveTime  = abs(moves[move].second - bluePosition);
				moveTime -= orangeTime;

				if (0 > moveTime)
					moveTime = 1;
				else
					moveTime++;

				bluePosition  = moves[move].second;
				blueTime     += moveTime;
				orangeTime    = 0;
				time         += moveTime;
				break;

			case 'O':
				moveTime  = abs(moves[move].second - orangePosition);
				moveTime -= blueTime;

				if (0 > moveTime)
					moveTime = 1;
				else
					moveTime++;

				orangePosition  = moves[move].second;
				blueTime        = 0;
				orangeTime     += moveTime;
				time           += moveTime;
				break;
		}
	}

	return time;
}
