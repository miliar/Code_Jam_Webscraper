#include <iostream>
#define RMAX 52
#define CMAX 52

using namespace std;

int main()
{
	freopen("sqr.in", "r", stdin);
	freopen("sqr.out", "w", stdout);
	
	int T, R, C;
	char map[RMAX][CMAX] = {{'0'}};
	char trash;
	
	scanf("%d", &T);
	
	for (int tc = 0; tc < T; tc++)
	{	
		scanf("%d %d", &R, &C);
		for (int i = 1; i <= R; i++)
		{
			scanf("%c", &trash);
			for (int j = 1; j <= C; j++)
			{
				scanf("%c", &map[i][j]);
			}
		}
		
		bool possible = true;
		for (int i = 1; i <= R; i++)
		{
			for (int j = 1; j <= C; j++)
			{
				if (map[i][j] == '#')
				{
					map[i][j] = '/';
					if (map[i+1][j] == '#') 
						map[i+1][j] = '\\';
					else
						possible = false;
					if (map[i][j+1] == '#') 
						map[i][j+1] = '\\';
					else
						possible = false;
					if (map[i+1][j+1] == '#')
						map[i+1][j+1] = '/';
					else
						possible = false;
					
					if (!possible)
						break;
				}
			}
		}
		
		printf("Case #%d:\n", tc + 1);
		if (!possible) printf ("Impossible\n");
		else
		{
			for (int i = 1; i <= R; i++)
			{
				for (int j = 1; j <= C; j++)
				{
					printf("%c", map[i][j]);
				}
				printf("\n");
			}
		}
		
		// cleanup
		for (int i = 0; i <= R + 1; i++)
		{
			for (int j = 0; j <= C + 1; j++)
			{
				map[i][j] = '0';
			}
		}
	}
}