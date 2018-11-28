#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>

#include <iostream>

//#include <cctype>
#include <cmath>

#include <fstream>

using namespace std;

string SolveCaseTTT()
{
	const int NUM_POS = 4;
	
	const char * STR_X_WON			= "X won";
	const char * STR_O_WON			= "O won";
	const char * STR_DRAW			= "Draw";
	const char * STR_NOT_FINISHED	= "Game has not completed";
	
	vector<string> board;

	for (int i = 0; i < NUM_POS; i++)
	{
		char line[10] = {0};
		cin.getline(line,10);
		board.push_back(line);
	}

	{
		char line[10] = {0};
		cin.getline(line,10);
	}

	//cout << endl;
	//for (int i = 0; i < NUM_POS; i++)
	//{
	//	cout << "line #" << i << " : [" << board[i] << "]" << endl;
	//}

	vector<string> v;
	v.push_back(board[0]);
	v.push_back(board[1]);
	v.push_back(board[2]);
	v.push_back(board[3]);

	for (int i = 0; i < NUM_POS; i++)
	{
		ostringstream ss;
		ss << board[0][i] << board[1][i] << board[2][i] << board[3][i];
		v.push_back(ss.str());
	}

	{
		ostringstream ss;
		ss << board[0][0] << board[1][1] << board[2][2] << board[3][3];
		v.push_back(ss.str());
	
		ss.str("");
		ss << board[0][3] << board[2][1] << board[1][2] << board[3][0];
		v.push_back(ss.str());
	
	}

	int numdot = 0;
	
	for (int i = 0; i < v.size(); i++)
	{
		//cout << "v[" << i << "] = " << v[i] << endl;
		int numx = 0;
		int numo = 0;
		int numt = 0;

		for (int j = 0; j < NUM_POS; j++)
		{
			if ('X' == v[i][j]) numx++;
			if ('O' == v[i][j]) numo++;
			if ('T' == v[i][j]) numt++;
			if ('.' == v[i][j]) numdot++;
		}

		if (NUM_POS == numx+numt) return STR_X_WON;
		if (NUM_POS == numo+numt) return STR_O_WON;
	}

	if (0 < numdot) return STR_NOT_FINISHED;

	return STR_DRAW;

}

void TTT()
{
	char line[10] = {0};
	cin.getline(line,10);
	
	int testCases = atoi(line);
	for(int i = 0; i < testCases; ++i)
	{
		cout << "Case #" << (i + 1) << ": " << SolveCaseTTT();
		cout << endl;
	}
}


//-----------------------------------------------------------------------------------------------//
//----- main function ---------------------------------------------------------------------------//
//-----------------------------------------------------------------------------------------------//
int main()
{
	TTT();
	return 0;
}
