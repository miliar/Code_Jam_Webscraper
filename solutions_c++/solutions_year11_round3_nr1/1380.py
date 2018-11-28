#include <stdio.h>

#define N 51

int T;
int R, C;
char map[N][N];
bool ispossible;

int main()
{
	int i, r, c;
	char ch;
	scanf("%d", &T);
	for(i = 0; i < T; i++)
	{
		scanf("%d%d", &R, &C);
		for(r = 1; r <= R; r++)
		{
			scanf("%c", &ch);
			for(c = 1; c <= C; c++)
				scanf("%c", &map[r][c]);
		}
		ispossible = true;
		for(r = 1; r <= R; r++)
			for(c = 1; c <= C; c++)
			{
				if(map[r][c] == '#')
				{
					if(c + 1 <= C && map[r][c + 1] == '#' 
						&& r + 1 <= R && map[r + 1][c] == '#'
						&& map[r + 1][c + 1] == '#')
					{
						map[r][c] = '/';
						map[r][c + 1] = '\\';
						map[r + 1][c] = '\\';
						map[r + 1][c + 1] = '/';
					}
					else
					{
						r = R + 1;
						ispossible = false;
						break;
					}
				}
			}
		printf("Case #%d:\n", i + 1);
		if(!ispossible)
		{
			printf("Impossible\n");
			continue;
		}
		for(r = 1; r <= R; r++)
		{
			for(c = 1; c <= C; c++)
				printf("%c", map[r][c]);
			printf("\n");
		}
	}

	return 0;
}