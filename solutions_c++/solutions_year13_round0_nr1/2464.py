
#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <stdexcept>
#include <fstream>
#include <map>
#include <limits>
#include <math.h>
#include <iomanip>
#include <iomanip>
#include <algorithm>

typedef __int64 int64_t;

using namespace std;

char Solve(const vector<vector<char>>& board)
{
	int i, j;
	bool isFinish = true;

	for (i = 0; i < 4; ++i)
	{
		char lastValue = 'T';
		char player = 0;

		for (j = 0; j < 4; ++j)
		{
			char b = board[i][j];
			if (b != lastValue && b != 'T' && lastValue != 'T')
				break;
			if (b != 'T'&& b != '.')
				player = b;
			if (b != 'T' && b == '.')
				isFinish = false;
			lastValue = b;
		}
		if (j == 4 && player != 0)
			return player;
	}

	for (i = 0; i < 4; ++i)
	{
		char lastValue = 'T';
		char player = 0;

		for (j = 0; j < 4; ++j)
		{
			char b = board[j][i];
			if (b != lastValue && b != 'T' && lastValue != 'T')
				break;
			if (b != 'T'&& b != '.')
				player = b;
			lastValue = b;
		}
		if (j == 4 && player != 0)
			return player;
	}

	char lastValue = 'T';
	char player = 0;

	for (j = 0; j < 4; ++j)
	{
		char b = board[j][j];
		if (b != lastValue && b != 'T' && lastValue != 'T')
			break;
		if (b != 'T'&& b != '.')
			player = b;
		lastValue = b;
	}
	if (j == 4 && player != 0)
		return player;

	lastValue = 'T';
	player = 0;
	for (j = 0; j < 4; ++j)
	{
		char b = board[j][3 - j];
		if (b != lastValue && b != 'T' && lastValue != 'T')
			break;
		if (b != 'T'&& b != '.')
			player = b;
		lastValue = b;
	}
	if (j == 4 && player != 0)
		return player;

	return (isFinish) ? 'D' : 'N'; 

}


int main(int argc, char** argv)
{
	const string inputFilename = "A-small-attempt0.in";
	const string outputFilename = inputFilename + ".out";
	ifstream ifs( inputFilename.c_str() );
	ofstream file( outputFilename.c_str());
	int nbTest = 0;

	ifs >> nbTest;
	string line;
	getline(ifs, line);

	for( int test = 1; test <= nbTest; ++test )
	{
		ostringstream ostr;
		int64_t n, d;
				
		vector<vector<char>> values;
		
		for (int i = 0; i < 4; ++i)
		{
			getline(ifs, line);
			values.push_back(vector<char>(line.begin(), line.end()));
		}
		getline(ifs, line);
		ostr << "Case #" << test << ": ";

		char res = Solve(values);
		switch (res)
		{
		case 'O': ostr << "O won"; break;
		case 'X': ostr << "X won"; break;			
		case 'D': ostr << "Draw"; break;
		case 'N': ostr << "Game has not completed"; break;
		default:
			throw runtime_error("");

		}

		ostr << endl;

		cout << ostr.str();
		file << ostr.str();
	}

	cout << "Finish" << endl;
	return 0;
}



