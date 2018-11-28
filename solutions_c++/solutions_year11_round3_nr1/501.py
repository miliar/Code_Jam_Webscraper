#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

char grid[50][50];

int main()
{
	int ncases, r, c;

	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++)
	{
		int count = 0;

		cin >> r >> c;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				cin >> grid[i][j];

		for (int i = 1; i < r; i++)
			for (int j = 1; j < c; j++)
				if (grid[i - 1][j - 1] == '#' && grid[i][j - 1] == '#' && grid[i - 1][j] == '#' && grid[i][j] == '#')
				{
					grid[i - 1][j - 1] = '/';
					grid[i - 1][j] = '\\';
					grid[i][j - 1] = '\\';
					grid[i][j] = '/';
				}

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if (grid[i][j] == '#')
					count++;

		printf("Case #%i:\n", caseno);
		if (count > 0)
		{
			printf("Impossible\n");
		}
		else
		{
			for (int i = 0; i < r; i++)
			{
				for (int j = 0; j < c; j++)
					cout << grid[i][j];
				cout << endl;
			}
		}
	}
}
