#include <iostream>

bool winner(int s)
{
	if (s == 'O' * 4 || s == 'O' * 3 + 'T')
	{
		std::cout << "O won" << std::endl;;
		return true;
	}

	if (s == 'X' * 4 || s == 'X' * 3 + 'T')
	{
		std::cout << "X won" << std::endl;
		return true;
	}

	return false;
}

int main(int argc, char ** argv)
{
	int n = 0;
	std::cin >> n;

	unsigned char board[4][4];

	for (int i = 0; i < n; i++)
	{
		bool empty = false;

		for (int j = 0; j < 4*4; j++)
		{
			std::cin >> board[0][j];
			if (board[0][j] == '.')
				empty |= true;
		}

		std::cout << "Case #" << i + 1 << ": ";

		bool won = false;
		int s = 0;
		for (int a = 0; a < 4; a++)
		{
			s = 0;
			for (int b = 0; b < 4; b++)
				s += board[a][b];
			if (won = winner(s))
				break;

			s = 0;
			for (int b = 0; b < 4; b++)
				s += board[b][a];
			if (won = winner(s))
				break;
		}

		if (won)
			continue;

		s = 0;
		for (int b = 0; b < 4; b++)
			s += board[b][b];
		if (winner(s))
			continue;

		s = 0;
		for (int b = 0; b < 4; b++)
			s += board[3-b][b];
		if (winner(s))
			continue;

		if (empty)
			std::cout << "Game has not completed" << std::endl;
		else
			std::cout << "Draw" << std::endl;
	}

	return 0;
}