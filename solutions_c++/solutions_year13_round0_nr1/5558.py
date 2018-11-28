#include <iostream>

using namespace std;

int detect(char grid[4][4])
{
	// Detect vertical or draw
	bool draw = true;
	for(int x = 0; x < 4; ++x)
	{
		int whoseline = -1;
		for(int y = 0; y < 4; ++y)
		{
			if(grid[x][y] == '.')
			{
				// nobody wins here
				whoseline = -1;
				draw = false;
				break;
			}

			if(grid[x][y] == 'X')
			{
				if(whoseline == 2)
				{
					//nobody wins here
					whoseline = -1;
					break;
				}

				whoseline = 1;
			}
			else if(grid[x][y] == 'O')
			{
				if(whoseline == 1)
				{
					//nobody wins here
					whoseline = -1;
					break;
				}

				whoseline = 2;
			}
		}
		if(whoseline == 1)
		{
			return 0;
		}
		else if(whoseline == 2)
		{
			return 1;
		}
	}
	// Detect horizontal
	for(int y = 0; y < 4; ++y)
	{
		int whoseline = -1;
		for(int x = 0; x < 4; ++x)
		{
			if(grid[x][y] == '.')
			{
				// nobody wins here
				whoseline = -1;
				break;
			}

			if(grid[x][y] == 'X')
			{
				if(whoseline == 2)
				{
					//nobody wins here
					whoseline = -1;
					break;
				}

				whoseline = 1;
			}
			else if(grid[x][y] == 'O')
			{
				if(whoseline == 1)
				{
					//nobody wins here
					whoseline = -1;
					break;
				}

				whoseline = 2;
			}
		}
		if(whoseline == 1)
		{
			return 0;
		}
		else if(whoseline == 2)
		{
			return 1;
		}
	}

	// Detect diagonal 1
	int whoseline = -1;
	for(int z = 0; z < 4; ++z)
	{
		if(grid[z][z] == '.')
		{
			// nobody wins here
			whoseline = -1;
			break;
		}

		if(grid[z][z] == 'X')
		{
			if(whoseline == 2)
			{
				//nobody wins here
				whoseline = -1;
				break;
			}

			whoseline = 1;
		}
		else if(grid[z][z] == 'O')
		{
			if(whoseline == 1)
			{
				//nobody wins here
				whoseline = -1;
				break;
			}

			whoseline = 2;
		}
	}

	if(whoseline == 1)
	{
		return 0;
	}
	else if(whoseline == 2)
	{
		return 1;
	}

	// Detect diagonal 2
	whoseline = -1;
	for(int z = 0; z < 4; ++z)
	{
		if(grid[z][3-z] == '.')
		{
			// nobody wins here
			whoseline = -1;
			break;
		}

		if(grid[z][3-z] == 'X')
		{
			if(whoseline == 2)
			{
				//nobody wins here
				whoseline = -1;
				break;
			}

			whoseline = 1;
		}
		else if(grid[z][3-z] == 'O')
		{
			if(whoseline == 1)
			{
				//nobody wins here
				whoseline = -1;
				break;
			}

			whoseline = 2;
		}
	}

	if(whoseline == 1)
	{
		return 0;
	}
	else if(whoseline == 2)
	{
		return 1;
	}

	// decide between draw or incomplete
	if(draw)
	{
		return 2;
	}

	return 3;
}

void main()
{
	int T;
	char grid[4][4];

	cin >> T;

	for(int t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";

		// Get game board
		for(int x = 0; x < 4; ++x)
		{
			for(int y = 0; y < 4; ++y)
			{
				cin >> grid[x][y];
			}
		}
		
		// Detect if X or O won
		int result = detect(grid);

		switch(result)
		{
		case(0):
			cout << "X won" << endl;
			break;
		case(1):
			cout << "O won" << endl;
			break;
		case(2):
			cout << "Draw" << endl;
			break;
		case(3):
			cout << "Game has not completed" << endl;
			break;
		}
	}
}