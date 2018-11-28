#include<cstdio>
using namespace std;

int T, R, C;
char mat[51][51];

int checkandfill(int x, int y)
{
	if((mat[x][y+1] == '#') && (mat[x+1][y+1] == '#') && (mat[x+1][y] == '#'))
	{
		mat[x][y] = '/';
		mat[x][y+1] = '\\';
		mat[x+1][y+1] = '/';
		mat[x+1][y] = '\\';
		return 1;
	}
	else
	{
		return 0;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		int OK = 1;
		scanf("%d %d", &R, &C);

		int blues = 0;
		for(int i = 0; i < R; i++)
		{
			scanf("%s", mat[i]);
		}

		for(int i = 0; i < R-1; i++)
		{
			for(int j = 0; j < C-1; j++)
			{
				if(mat[i][j] == '#')
				{
					int temp = checkandfill(i,j);
					if(!temp)
						OK = 0;
				}
			}
		}

		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				if(mat[i][j] == '#')
					OK = 0;
			}
		}

		printf("Case #%d:\n", cases);
		if(OK)
		{
			for(int i = 0; i < R; i++)
			{
				printf("%s\n", mat[i]);
			}
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}