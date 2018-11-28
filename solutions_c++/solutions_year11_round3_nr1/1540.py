#include <iostream>

using namespace std;


int main()
{
	int T;
	cin >> T;

	for(int t = 0; t < T; t++)
	{
		int R;
		int C;
		cin >> R;
		cin >> C;
		int bCount = 0;

		char* grid = new char[R*C];

		for(int r = 0; r < R; r++)
		{
			for(int c = 0; c < C; c++)
			{
				char in;
				cin >> in;
				if(in == '#')
					bCount ++;

				grid[r*C + c] = in;
			}
		}

		if((bCount % 4) != 0)
		{
			cout << "Case #" << t+1 << ":\nImpossible" << endl;
			continue;
		}

		bool success = false;
		for(int g = 0; g < R*C; g++)
		{
			if(grid[g] == '#')
			{
				if(g+C+1 >= R*C) break;
				if(grid[g+1] != '#' || (g+1) % C == 0) break;
				if(grid[g+C] != '#' || (g / C - 1) >= R-1) break;
				if(grid[g+C+1] != '#') break;

				grid[g] = '/';
				grid[g+1] = '\\';
				grid[g+C] = '\\';
				grid[g+C+1] = '/';
			}
			if(g == R*C-1)
				success = true;
		}
		if(bCount == 0)
			success = true;

		if(!success)
			cout << "Case #" << t+1 << ":\nImpossible" << endl;
		else
		{
			cout << "Case #" << t+1 << ":" << endl;
			for(int r = 0; r < R; r++)
			{
				for(int c = 0; c < C; c++)
				{
					cout << grid[r*C + c];
				}
				cout << endl;
			}
		}


		delete[] grid;
	}
	return 0;
}