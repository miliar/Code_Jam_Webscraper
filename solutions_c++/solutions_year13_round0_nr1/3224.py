#include <iostream>
#include <fstream>
using namespace std;

char board[4][4];

void main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");

	int T;
	in >> T;

for (int k = 0; k < T; k++)
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			in >> board[i][j];

	bool containsT = false;
	char winner = 'N';
	int countX, countO;
	bool hasDots = false;

	for (int i = 0; i < 4; i++)
	{
		countX = countO = 0;
		containsT = false;
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] == '.')
				hasDots = true;
			if (board[i][j] == 'T')
				containsT = true;
			else if (board[i][j] == 'X') 
				countX++;
			else if (board[i][j] == 'O')
				countO++;
		}

		if (containsT)
			if (countX == 3)
				winner = 'X';
			else 
			{
				if (countO == 3)
					winner = 'O';
			}
		else
		{
			if (countX == 4)
				winner = 'X';
			else if (countO == 4)
				winner = 'O';
		}

		if (winner != 'N')
			break;
	}

	if (winner == 'N')
		for (int j = 0; j < 4; j++)
		{
			countX = countO = 0;
			containsT = false;
			for (int i = 0; i < 4; i++)
			{
				if (board[i][j] == 'T')
					containsT = true;
				else if (board[i][j] == 'X') 
					countX++;
				else if (board[i][j] == 'O')
					countO++;
			}

			if (containsT)
				if (countX == 3)
					winner = 'X';
				else 
				{
					if (countO == 3)
						winner = 'O';
				}
			else
			{
				if (countX == 4)
					winner = 'X';
				else if (countO == 4)
					winner = 'O';
			}

			if (winner != 'N')
				break;
		}

	if (winner == 'N')
	{
		countX = countO = 0;
		containsT = false;

		for (int i = 0; i < 4; i++)
		{
			if (board[i][i] == 'T')
				containsT = true;
			if (board[i][i] == 'X')
				countX++;
			else if (board[i][i] == 'O')
				countO++;
		}

		if (containsT)
			if (countX == 3)
				winner = 'X';
			else 
			{
				if (countO == 3)
					winner = 'O';
			}
		else
		{
			if (countX == 4)
				winner = 'X';
			else if (countO == 4)
				winner = 'O';
		}
	}

	if (winner == 'N')
	{
		countX = countO = 0;
		containsT = false;

		for (int i = 0; i < 4; i++)
		{
			if (board[i][3 - i] == 'T')
				containsT = true;
			if (board[i][3 - i] == 'X')
				countX++;
			else if (board[i][3 - i] == 'O')
				countO++;
		}

		if (containsT)
			if (countX == 3)
				winner = 'X';
			else 
			{
				if (countO == 3)
					winner = 'O';
			}
		else
		{
			if (countX == 4)
				winner = 'X';
			else if (countO == 4)
				winner = 'O';
		}
	}

	if (winner == 'X')
		out << "Case #" << k + 1 << ": X won" << endl;
	else if (winner == 'O')
		out << "Case #" << k + 1 << ": O won" << endl;
	else if (hasDots)
		out << "Case #" << k + 1 << ": Game has not completed" << endl;
	else 
		out << "Case #" << k + 1 << ": Draw" << endl;
}
}
