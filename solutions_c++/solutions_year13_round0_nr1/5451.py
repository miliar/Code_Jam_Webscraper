#include <fstream>
#include <string>
using namespace std;

int main (void)
{
	fstream input("A-small-attempt2.in");
	ofstream output("A-small-attempt2.out");

	int T;
	input >> T;

	for (int t = 1; t <= T; t++)
	{
		char grid[4][4];

		//read the board
		for (int y = 0; y < 4; y++)
			for (int x = 0; x < 4; x++)
				input >> grid[x][y];

		//check for wins
		bool win = false;
		bool draw = true;
		char winner;

		//rows
		for (int y = 0; y < 4; y++)
		{
			winner = 'T';
			for (int x = 0; x < 4; x++)
			{
				if (grid[x][y] == '.')
					draw = false;

				if (winner == 'T')
				{
					winner = grid[x][y];
					continue;
				}

				if (grid[x][y] != winner && grid[x][y] != 'T')
				{
					winner = '.';
					break;
				}
			}

			if (winner != '.')
			{
				win = true;
				break;
			}
		}

		//columns
		if (!win)
		{
			for (int x = 0; x < 4; x++)
			{
				winner = 'T';
				for (int y = 0; y < 4; y++)
				{
					if (winner == 'T')
					{
						winner = grid[x][y];
						continue;
					}

					if (grid[x][y] != winner && grid[x][y] != 'T')
					{
						winner = '.';
						break;
					}
				}

				if (winner != '.')
				{
					win = true;
					break;
				}
			}
		}

		//diag1
		if (!win)
		{
			winner = 'T';
			int x = 0;
			for (int y = 0; y < 4; y++, x++)
			{
				if (winner == 'T')
				{
					winner = grid[x][y];
					continue;
				}

				if (grid[x][y] != winner && grid[x][y] != 'T')
				{
					winner = '.';
					break;
				}
			}

			if (winner != '.')
			{
				win = true;
			}
		}

		//diag2
		if (!win)
		{
			winner = 'T';
			int x = 3;
			for (int y = 0; y < 4; y++, x--)
			{
				if (winner == 'T')
				{
					winner = grid[x][y];
					continue;
				}

				if (grid[x][y] != winner && grid[x][y] != 'T')
				{
					winner = '.';
					break;
				}
			}

			if (winner != '.')
			{
				win = true;
			}
		}

		//output the result
		output << "Case #" << t << ": ";
		
		if (win)
			output << winner << " won";
		else if (draw)
			output << "Draw";
		else
			output << "Game has not completed";

		if (t != T)
			output << endl;

	}

	input.close();
	output.close();
}