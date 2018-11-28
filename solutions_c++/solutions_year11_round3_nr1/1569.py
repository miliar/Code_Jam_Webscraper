#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>
#include <set>
#include <iostream>
#include <sstream>
#include <ctime>
#include <numeric>

using namespace std;

char grid[64][64];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int R, C;
		scanf("%d %d", &R, &C);
		for(int i = 0; i < R; i++)
			scanf("%s", grid[i]);
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
				if(i+1 < R && j+1 < C && grid[i][j] == '#' && grid[i][j] == grid[i+1][j+1] && grid[i+1][j+1] == grid[i+1][j] && grid[i][j+1] == grid[i][j])
				{
					grid[i][j] = grid[i+1][j+1] = '/';
					grid[i+1][j] = grid[i][j+1] = '\\';
				}
		}
		bool imp = false;
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				if(grid[i][j] == '#')
				{
					imp = true;
					break;
				}
				printf("Case #%d:\n", t);
				if(imp)	{	printf("Impossible\n");	continue;}
				for(int i = 0; i < R; i++)
					printf("%s\n", grid[i]);

	}
	return 0;
}