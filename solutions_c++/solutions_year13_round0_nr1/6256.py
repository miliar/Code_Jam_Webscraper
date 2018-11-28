// Tic-Tac-Toe-Tomek.cpp : fichier projet principal.

#include "stdafx.h"

#include <cstdio>
#include <iostream>

using namespace std;

int main(void)
{
	int T;

	if (NULL == freopen("A-large.in", "rt", stdin))
		return EXIT_FAILURE;

	if (NULL == freopen("A-large.out", "wt", stdout))
		return EXIT_FAILURE;

	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		char m[4][4], symbol;
		bool winner;
		int j, k;

		cout << "Case #" << i << ": ";

		for (int j = 0; j < 4; ++j)
			for (int k = 0; k < 4; ++k)
				cin >> m[j][k];

		winner = false;

		// Horizontal
		j = 0;
		while (!winner && j < 4)
		{
			if (m[j][0] == 'T')
			{
				k = 2;
				symbol = m[j][1];
				if (symbol != '.')
					while (m[j][k] == symbol && k < 4) ++k;
			}
			else
			{
				k = 1;
				symbol = m[j][0];
				if (symbol != '.')
					while ((m[j][k] == symbol || m[j][k] == 'T') && k < 4) ++k;
			}
			if (k == 4)
			{
				winner = true;
				cout << symbol << " won\n";
			}
			++j;
		}

		// Vertical
		k = 0;
		while (!winner && k < 4)
		{
			if (m[0][k] == 'T')
			{
				j = 2;
				symbol = m[1][k];
				if (symbol != '.')
					while (m[j][k] == symbol && j < 4) ++j;
			}
			else
			{
				j = 1;
				symbol = m[0][k];
				if (symbol != '.')
					while ((m[j][k] == symbol || m[j][k] == 'T') && j < 4) ++j;
			}
			if (j == 4)
			{
				winner = true;
				cout << symbol << " won\n";
			}
			++k;
		}

		// Diagonal
		if (!winner)
		{
			if (m[0][0] == 'T')
			{
				j = 2;
				symbol = m[1][1];
				if (symbol != '.')
					while (m[j][j] == symbol && j < 4) ++j;
			}
			else
			{
				j = 1;
				symbol = m[0][0];
				if (symbol != '.')
					while ((m[j][j] == symbol || m[j][j] == 'T') && j < 4) ++j;
			}
			if (j == 4)
			{
				winner = true;
				cout << symbol << " won\n"; 
			}
		}

		// Back diagonal
		if (!winner)
		{
			if (m[3][0] == 'T')
			{
				j = 1;
				k = 2;
				symbol = m[2][1];
				if (symbol != '.')
					while (m[j][k] == symbol && k < 4) --j, ++k;
			}
			else
			{
				j = 2;
				k = 1;
				symbol = m[3][0];
				if (symbol != '.')
					while ((m[j][k] == symbol || m[j][k] == 'T') && k < 4) --j, ++k;
			}
			if (k == 4)
			{
				winner = true;
				cout << symbol << " won\n"; 
			}
		}

		//
		if (!winner)
		{
			bool not_completed = false;
			j = 0;
			while (!not_completed && j < 4)
			{
				k = 0;
				while (m[j][k] != '.' && k < 4)
					++k;
				if (k == 4)
					++j;
				else
					not_completed = true;
			}
			if (not_completed)
				cout << "Game has not completed\n";
			else
				cout << "Draw\n";
		}
	}

    return EXIT_SUCCESS;
}
