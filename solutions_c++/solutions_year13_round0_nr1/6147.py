// tictac.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

ifstream input;

char state[4][4];

bool check(char needle, int x, int y)
{
	bool vertical = true;
	for(int i = 0; i < 4; i++)
		if(state[i][y] != needle && state[i][y] != 'T')
			vertical = false;

	if(vertical)
		return true;

	bool horizontal = true;
	for(int j = 0; j < 4; j++)
		if(state[x][j] != needle && state[x][j] != 'T')
			horizontal = false;
	
	if(horizontal)
		return true;

	bool diagonal = true;
	for(int i = 0; i < 4; i++)
		if(state[i][i] != needle && state[i][i] != 'T')
			diagonal = false;

	if(diagonal)
		return true;

	diagonal = true;
	for(int i = 0; i < 4; i++)
		if(state[3 - i][i] != needle && state[3 - i][i] != 'T')
			diagonal = false;
	
	if(diagonal)
		return true;

	return false;
}

bool find(char needle)
{
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(state[i][j] == needle)
			{
				if(check(needle, i, j))
					return true;
			}

	return false;
}

char solve()
{
	bool completed = true;
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			input >> state[i][j];

			if(state[i][j] == '.')
				completed = false;
		}
	}

	if(find('X'))
		return 'X';

	if(find('O'))
		return 'O';

	return !completed ? 'G' : 'D';
}

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream output;

	input.open("input.txt");
	output.open("output.txt");

	short t;
	input >> t;

	for(short i = 0; i < t; i++)
	{
		char result = solve();

		output << "Case #" << i + 1 << ": ";
		switch(result)
		{
		case 'X':
			output << "X won";
			break;
		case 'O':
			output << "O won";
			break;
		case 'D':
			output << "Draw";
			break;
		case 'G':
			output << "Game has not completed";
			break;
		}
		output << endl;
	}

	input.close();
	output.close();

	return 0;
}

