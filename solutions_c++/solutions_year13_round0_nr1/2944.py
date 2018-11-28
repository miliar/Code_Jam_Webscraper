//Google Codejam
//2013 Qualification Round
//Alan Richards - alarobric

//Problem A
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
using namespace std;

#define FOR(i, n) for(int i=0; i<(n); i++)
#define FOREACH(iter, c) for(auto iter=c.begin(); iter!=c.end(); iter++)

vector<int> arrM;

string Solve(int i_case)
{
	char in;
	char board[4][4];
	bool emptySquares = false;
	int i,j;
	FOR(i, 4)
		FOR(j,4)
		{
			cin >> in;
			board[i][j] = in;
			if (in == '.')
				emptySquares = true;
		}
		
	//rows
	FOR(i,4)
	{
		bool OCouldWin = true;
		bool XCouldWin = true;
		FOR(j,4)
		{
			if (board[i][j] == 'O')
				XCouldWin = false;
			else if (board[i][j] == 'X')
				OCouldWin = false;
			else if (board[i][j] == '.')
			{
				XCouldWin = OCouldWin = false;
			}
		}
		if (OCouldWin)
			return "O won";
		if (XCouldWin)
			return "X won";
	}
	//columns
	FOR(j,4)
	{
		bool OCouldWin = true;
		bool XCouldWin = true;
		FOR(i,4)
		{
			if (board[i][j] == 'O')
				XCouldWin = false;
			else if (board[i][j] == 'X')
				OCouldWin = false;
			else if (board[i][j] == '.')
			{
				XCouldWin = OCouldWin = false;
			}
		}
		if (OCouldWin)
			return "O won";
		if (XCouldWin)
			return "X won";
	}
	//diagonals
	{
		bool OCouldWin = true;
		bool XCouldWin = true;
		FOR(i,4)
		{
			if (board[i][i] == 'O')
				XCouldWin = false;
			else if (board[i][i] == 'X')
				OCouldWin = false;
			else if (board[i][i] == '.')
			{
				XCouldWin = OCouldWin = false;
			}
		}
		if (OCouldWin)
			return "O won";
		if (XCouldWin)
			return "X won";
	}
	{
		bool OCouldWin = true;
		bool XCouldWin = true;
		FOR(i,4)
		{
			if (board[i][3-i] == 'O')
				XCouldWin = false;
			else if (board[i][3-i] == 'X')
				OCouldWin = false;
			else if (board[i][3-i] == '.')
			{
				XCouldWin = OCouldWin = false;
			}
		}
		if (OCouldWin)
			return "O won";
		if (XCouldWin)
			return "X won";
	}
	if (emptySquares)
		return "Game has not completed";
	return "Draw";
}

int main()
{
	std::cerr << "GCJ Practice" << std::endl;
	int numCases;
	std::cin >> numCases;
	for (int i=1; i<=numCases; i++)
	{
		std::cout << "Case #" << i << ": " << Solve(i) << std::endl;
	}
	return 0;
}