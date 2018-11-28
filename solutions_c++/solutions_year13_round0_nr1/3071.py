#include <iostream>
#include <stdio.h>
#include <memory.h>

using namespace std;

bool complete;
char board[4][4];

//#define DEBUG

void d(string str)
{
#ifdef DEBUG
	cout << str << endl;
#endif
}

void printResult(int n)
{
	int Xscore = 0;
	int Oscore = 0;
	printf("Case #%d: ", n + 1);
	for(int i = 0; i < 4; ++i)
	{
		Xscore = 0;
		Oscore = 0;
		for(int j = 0; j < 4; ++j)
		{
			switch( board[i][j] )
			{
				case 'X':
					++Xscore;
					break;
				case 'O':
					++Oscore;
					break;
				case 'T':
					++Xscore;
					++Oscore;
					break;
				case '.':
					break;
				default:
					cout << "error!!!" << endl;
					return;
			}
		}
		if(Xscore == 4)
		{
			cout << "X won" << endl;
			return;
		}
		else if(Oscore == 4)
		{
			cout << "O won" << endl;
			return;
		}
	}
	for(int i = 0; i < 4; ++i)
	{
		Xscore = 0;
		Oscore = 0;
		for(int j = 0; j < 4; ++j)
		{
			switch( board[j][i] )
			{
				case 'X':
					++Xscore;
					break;
				case 'O':
					++Oscore;
					break;
				case 'T':
					++Xscore;
					++Oscore;
					break;
				case '.':
					break;
				default:
					cout << "error!!!" << endl;
					return;
			}
		}
		if(Xscore == 4)
		{
			cout << "X won" << endl;
			return;
		}
		else if(Oscore == 4)
		{
			cout << "O won" << endl;
			return;
		}
	}

	Xscore = 0;
	Oscore = 0;
	for(int i = 0; i < 4; ++i)
	{
		switch(board[i][i])
		{
			case 'X':
				++Xscore;
				break;
			case 'O':
				++Oscore;
				break;
			case 'T':
				++Xscore;
				++Oscore;
				break;
			case '.':
				break;
			default:
				cout << "error!!!" << endl;
				return;
		}
		if(Xscore == 4)
		{
			cout << "X won" << endl;
			return;
		}
		else if(Oscore == 4)
		{
			cout << "O won" << endl;
			return;
		}
	}

	Xscore = 0;
	Oscore = 0;
	for(int i = 0; i < 4; ++i)
	{
		switch(board[3-i][i])
		{
			case 'X':
				++Xscore;
				break;
			case 'O':
				++Oscore;
				break;
			case 'T':
				++Xscore;
				++Oscore;
				break;
			case '.':
				break;
			default:
				cout << "error!!!" << endl;
				return;
		}
		if(Xscore == 4)
		{
			cout << "X won" << endl;
			return;
		}
		else if(Oscore == 4)
		{
			cout << "O won" << endl;
			return;
		}
	}

	if(complete)
	{
		cout << "Draw" << endl;
	}
	else
	{
		cout << "Game has not completed" << endl;
	}
}

void readBoard()
{
	string line;
	complete = true;
	for(int i = 0; i < 4; ++i)
	{
		cin >> line;
		d(line);
		for(int j = 0; j < 4; ++j)
		{
			board[i][j] = line[j];
			if(line[j] == '.')
			{
				complete = false;
			}
		}
	}
}

int main()
{
	int N;
	cin >> N;

	for(int i = 0; i < N; ++i)
	{
		readBoard();
		printResult(i);
	}
	return 0;
}

