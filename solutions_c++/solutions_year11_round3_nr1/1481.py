#if 1

#include <cstdio>
#include <cstring>

const int SZ = 55;

int R, C;
char tile[SZ][SZ];

bool change()
{
	int i, j;
	for (i = 0; i < R; i++)
	{
		for (j = 0; j < C; j++)
		{
			if (tile[i][j] != '#') continue;
			else if ( (i-1 < 0 || tile[i-1][j] != '#')
				&& (j-1 <0 || tile[i][j-1] != '#')
				&& (i-1 < 0 || j-1 < 0 || tile[i-1][j-1] != '#') )
			{
				if (tile[i][j] == '#' 
					&& (j+1 < C && tile[i][j+1] == '#')
					&& (i+1 < R && tile[i+1][j] == '#')
					&& tile[i+1][j+1] == '#')
				{
					tile[i][j] = '/';
					tile[i][j+1] = '\\';
					tile[i+1][j] = '\\';
					tile[i+1][j+1] = '/';
				}
				else return 0;
			}
		}
	}
	return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int t;
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		scanf("%d%d", &R, &C);
		int i;
		for (i = 0; i < R; i++)
			scanf("%s", tile[i]);
		if (change())
		{
			for (i = 0; i < R; i++)
				printf("%s\n", tile[i]);
		}
		else printf("Impossible\n");
	}

	return 0;
}

#endif