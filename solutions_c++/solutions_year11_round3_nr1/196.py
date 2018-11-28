#include <iostream>
#include <xutility>
#include <vector>

using namespace std;

bool SolveTest();

void main()
{
	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		cout << "Case #" << i+1 << ":" << endl;;
		bool result = SolveTest();
		if(!result)
			cout << "Impossible" << endl;
	}
}

bool SolveTest()
{
	char grid[50][50];
	char ch;

	int rows, cols;
	cin >> rows;
	cin >> cols;

	//read in all
	for(int i = 0; i < rows; ++i)
	{
		for(int j = 0; j < cols; ++j)
		{
			cin >> ch;
			grid[i][j] = ch;
		}
	}

	//scan and convert
	for(int i = 0; i < rows; ++i)
	{
		for(int j = 0; j < cols; ++j)
		{
			if(grid[i][j] == '#')
			{
				//convert all, or fail
				if(i + 1 >= rows)
					return false;

				if(j + 1 >= cols)
					return false;
				
				if(grid[i+1][j] != '#' || grid[i+1][j+1] != '#' || grid[i][j+1] != '#')
					return false;

				grid[i][j] = '/';
				grid[i+1][j] = '\\';
				grid[i][j+1] = '\\';
				grid[i+1][j+1] = '/';
			}
		}
	}

	for(int i = 0; i < rows; ++i)
	{
		for(int j = 0; j < cols; ++j)
		{
			cout << grid[i][j];
		}
		cout << endl;
	}


}