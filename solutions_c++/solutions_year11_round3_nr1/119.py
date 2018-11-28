#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int row, col;
char map[1000][1000];

bool solve()
{
	for(int i = 1; i <= row; ++i)
			for(int j = 1; j <= col; ++j)
				if(map[i][j] == '#')
				{
					if(map[i + 1][j] == '#' && map[i][j + 1] == '#' && map[i + 1][j + 1] == '#')
					{
						map[i][j] = '/';
						map[i][j + 1] = '\\';
						map[i + 1][j] = '\\';
						map[i + 1][j + 1] = '/';
					}
					else return false;
				}
	return true;
}

int main()
{
	int T; scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%i %i", &row, &col);
		for(int i = 0; i <= row + 1; ++i)
			for(int j = 0; j <= col + 1; ++j)
				map[i][j] = '.';
				
		for(int i = 1; i <= row; ++i)
			for(int j = 1; j <= col; ++j)
				scanf("%1s", &map[i][j]);
		
		printf("Case #%i:\n", t);
		if(solve())
		{
			for(int i = 1; i <= row; ++i)
			{
				for(int j = 1; j <= col; ++j)
					printf("%c", map[i][j]);
				printf("\n");
			}
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}
