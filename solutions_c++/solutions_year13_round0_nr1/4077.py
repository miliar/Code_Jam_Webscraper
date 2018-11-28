#ifdef DEBUG_OUTPUT
#include "debug_output.h"
#else
#define DEBUG(x)
#endif

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
using namespace std;


// Enlarge MSVS stack size
#pragma comment(linker, "/STACK:16777216")

#define pb push_back
#define all(c) c.begin(), c.end()
#define mp(x, y) make_pair(x, y)
#define sz(x) static_cast<int>(x.size())
typedef long long int64;

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("_.in", "r", stdin);
    freopen("_.out", "w", stdout);
	std::ios_base::sync_with_stdio (false);
}

void input(vector<string>& board)
{
	for (int i = 0; i < 4; ++i)
	{
		string line;
		getline(cin, line);
		if (line.length() == 0)
			i--;
		else
			board.push_back(line);
	}
}

string GetGameState(vector<string> board)
{
	bool existEmpty = false;
	for (int i = 0; i < 4; i++)
	{
		int xCount = 0;
		int yCount = 0;
		for (int j = 0; j < 4; ++j)
		{
			if (board[i][j] == 'X')
				xCount++;
			else if (board[i][j] == 'O')
				yCount++;
			else if (board[i][j] == 'T')
			{
				xCount++;
				yCount++;
			} 
			else 
			{
				existEmpty = true;
				break;
			}	
		}

		if (xCount == 4)
			return "X won";
		if (yCount == 4)
			return "O won";
	}

	for (int j = 0; j < 4; j++)
	{
		int xCount = 0;
		int yCount = 0;
		for (int i = 0; i < 4; ++i)
		{
			if (board[i][j] == 'X')
				xCount++;
			else if (board[i][j] == 'O')
				yCount++;
			else if (board[i][j] == 'T')
			{
				xCount++;
				yCount++;
			} 
			else 
			{
				existEmpty = true;
				break;
			}	
		}

		if (xCount == 4)
			return "X won";
		if (yCount == 4)
			return "O won";
	}

	{
		int xCount = 0;
		int yCount = 0;
		for (int i = 0; i < 4; i++)
		{
			if (board[i][i] == 'X')
				xCount++;
			else if (board[i][i] == 'O')
				yCount++;
			else if (board[i][i] == 'T')
			{
				xCount++;
				yCount++;
			} 
			else 
			{
				break;
			}	
		}

		if (xCount == 4)
			return "X won";
		if (yCount == 4)
			return "O won";
	}

	{
		int xCount = 0;
		int yCount = 0;
		for (int i = 0; i < 4; i++)
		{
			int j = 4 - i - 1;
			if (board[i][j] == 'X')
				xCount++;
			else if (board[i][j] == 'O')
				yCount++;
			else if (board[i][j] == 'T')
			{
				xCount++;
				yCount++;
			} 
			else 
			{
				break;
			}	
		}

		if (xCount == 4)
			return "X won";
		if (yCount == 4)
			return "O won";
	}


	if (!existEmpty)
		return "Draw";
	else 
		return "Game has not completed";
}

int main()
{
    initialize();

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++)
	{
		vector<string> dashboard;
		input(dashboard);

		string gameResult = GetGameState(dashboard);
		cout << "Case #" << i + 1 << ": " << gameResult << endl;
	}

    
    return 0;
}
