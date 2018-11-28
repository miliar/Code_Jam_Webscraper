#include <iostream>
#include <string>

int main(int argc, char *argv[])
{
	int nrTestCases;

	std::cin >> nrTestCases;

	for(int i = 0; i < nrTestCases; i++)
	{
		std::string tc[4];

		bool dotFound = false;
		for(int j = 0; j < 	4; j++)
		{
			std::cin >> tc[j];

			if (tc[j].find(".") != std::string::npos)
			{
				dotFound = true;
			}
		}

		// Output case number
		std::cout << "Case #" << (i + 1) << ": ";

		// Vaaka
		bool isWon = false;
		for(int j = 0; j < 4; j++)
		{
			int nrX = 0, nrO = 0;
			for(int k = 0; k < 4; k++)
			{
				switch(tc[j][k])
				{
				case 'X':
					nrX++;
					break;
				case 'O':
					nrO++;
					break;
				case 'T':
					nrX++;
					nrO++;
					break;
				}
			}

			if (nrX == 4)
			{
				std::cout << "X won\n";
				isWon = true;
				break;
			}
			if (nrO == 4)
			{
				std::cout << "O won\n";
				isWon = true;
				break;
			}
		}

		if (isWon)
		{
			continue;
		}

		// Pysty
		for(int j = 0; j < 4; j++)
		{
			int nrX = 0, nrO = 0;
			for(int k = 0; k < 4; k++)
			{
				switch(tc[k][j])
				{
				case 'X':
					nrX++;
					break;
				case 'O':
					nrO++;
					break;
				case 'T':
					nrX++;
					nrO++;
					break;
				}
			}

			if (nrX == 4)
			{
				std::cout << "X won\n";
				isWon = true;
				break;
			}
			if (nrO == 4)
			{
				std::cout << "O won\n";
				isWon = true;
				break;
			}
		}

		if (isWon)
		{
			continue;
		}

		// Diagonaali 1
		{
			int nrX = 0, nrO = 0;
			for(int k = 0; k < 4; k++)
			{
				switch(tc[k][k])
				{
				case 'X':
					nrX++;
					break;
				case 'O':
					nrO++;
					break;
				case 'T':
					nrX++;
					nrO++;
					break;
				}
			}

			if (nrX == 4)
			{
				std::cout << "X won\n";
				isWon = true;
				continue;
			}
			if (nrO == 4)
			{
				std::cout << "O won\n";
				isWon = true;
				continue;
			}
		}

		// Diagonaali 2
		{
			int nrX = 0, nrO = 0;
			for(int k = 0; k < 4; k++)
			{
				switch(tc[3 - k][k])
				{
				case 'X':
					nrX++;
					break;
				case 'O':
					nrO++;
					break;
				case 'T':
					nrX++;
					nrO++;
					break;
				}
			}

			if (nrX == 4)
			{
				std::cout << "X won\n";
				isWon = true;
				continue;
			}
			if (nrO == 4)
			{
				std::cout << "O won\n";
				isWon = true;
				continue;
			}
		}

		// Draw / not completed
		if (!dotFound)
		{
			std::cout << "Draw\n";
		} else 
		{
			std::cout << "Game has not completed\n";
		}
	}

	return 0;
}