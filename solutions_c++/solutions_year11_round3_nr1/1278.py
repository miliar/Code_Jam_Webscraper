/* 
 * File:   main.cpp
 * Author: tom
 *
 * Created on 22 May 2011, 9:05 PM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;

/*
 * 
 */
const int MAX = 50;
int nX, nY;
char board[MAX][MAX];

bool isBlue(int x, int y) { return board[x][y] == '#'; }
bool isRed(int x, int y);
bool canPlaceTile(int x, int y);
bool makeRed();

int main()
{
	ifstream in("in");
	ofstream out("out");

	int numT = 0;

	in >> numT;

	for (int t = 1; t <= numT; t++)
	{
		out << "Case #" << t << ":" << "\n";
		in >> nX >> nY;
		for (int i = 0; i < nX; i++)
		{
			for (int j = 0; j < nY; j++)
			{
				in >> board[i][j];
			}
		}

		bool isPossible = makeRed();

		if (!isPossible)
		{
			out << "Impossible" << "\n";
		}
		else
		{
			for (int i = 0; i < nX; i++)
			{
				for (int j = 0; j < nY; j++)
				{
					out << board[i][j];
				}
				out << "\n";
			}
		}
	}

	return 0;
}

bool isRed(int x, int y)
{
	if (board[x][y] == '/' || board[x][y] == '\\')
		return true;
	else
		return false;
}

bool canPlaceTile(int x, int y)
{
	if (x == nX - 1 || y == nY - 1)
		return false;

	if (!isBlue(x + 1, y) ||
			!isBlue(x, y + 1) ||
			!isBlue(x+1, y+1)
			)
	{
		return false;
	}

	return true;
}

void placeTile(int x, int y)
{
	board[x][y] = '/';
	board[x+1][y] = '\\';
	board[x][y+1] = '\\';
	board[x+1][y+1] = '/';
}

bool makeRed()
{
	for (int x = 0; x < nX; x++)
	{
		for (int y = 0; y < nY; y++)
		{
			if (isBlue(x, y))
			{
				if (!canPlaceTile(x, y))
					return false;
				else
					placeTile(x, y);
			}
		}
	}

	return true;
}