#include<iostream>
#include<fstream>
using namespace std;

char grid[51][51];

bool checkblue(int R, int C)
{
	int x, y;

	for(y = 0; y < R; y++)
	{
		for(x = 0; x < C; x++)
		{
			if(grid[x][y] == '#')
			{
				if(grid[x + 1][y] == '#' &&
				   grid[x][y + 1] == '#' &&
				   grid[x + 1][y + 1] == '#')
				{
					grid[x][y] = '/';
					grid[x + 1][y] = '\\';
					grid[x][y + 1] = '\\';
					grid[x + 1][y + 1] = '/';					   	
				}
				else
				{
					return false;
				}
			}
		}
	}

	return true;
}

int main()
{
	ifstream fin("qa.in");
	ofstream fout("qa.out");
	
	int T, R, C;
	int n, x, y;
	
	fin >> T;
	
	for(n = 1; n <= T; n++)
	{
		fin >> R >> C;
		
		for(y = 0; y < R; y++)
		{
			for(x = 0; x < C; x++)
			{
				fin >> grid[x][y]; 
			}
		}
		
		fout << "Case #" << n << ": " << endl;
		
		if(checkblue(R, C))
		{
			for(y = 0; y < R; y++)
			{
				for(x = 0; x < C; x++)
				{
					fout << grid[x][y]; 
				}
				fout <<endl;
			}
		}
		else
		{
			fout << "Impossible" << endl;
		}
	}
}