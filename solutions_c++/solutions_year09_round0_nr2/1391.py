#include<queue>

const int MAXL = 1e9, MAXN = 102;
int m[MAXN][MAXN];
int col[MAXN][MAXN];
int num;

int di[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int dfs(int x, int y)
{
	if(col[x][y] == 0)
	{
		int nx, ny;
		int mn = m[x][y];
		for(int i = 0; i < 4; i++)
			if(m[x + di[i][0]][y + di[i][1]] < mn)
			{
				mn = m[x + di[i][0]][y + di[i][1]];
				nx = x + di[i][0];
				ny = y + di[i][1];
			}
		//sink
		if(m[x][y] == mn)
			col[x][y] = num++;		
		else
			col[x][y] = dfs(nx, ny);
	}
	return col[x][y];
}

int main()
{	
	freopen("B-large.in", "r", stdin);
	//freopen("B-small1.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int ncase;
	scanf("%d", &ncase);	
	for(int c = 0; c < ncase; c++)
	{
		printf("Case #%d:\n", c + 1);
		int n1, n2;
		scanf("%d%d\n", &n1, &n2);
		for(int i = 0; i < MAXN; i++)
			for(int j = 0; j < MAXN; j++)
			{
				m[i][j] = MAXL;
			}
		memset(col, 0, sizeof(col));
		for(int i = 1; i <= n1; i++)
			for(int j = 1; j <= n2; j++)
				scanf("%d", &m[i][j]);
		num = 1;
		for(int i = 1; i <= n1; i++)
			for(int j = 1; j <= n2; j++)
			{
				printf("%c", 'a' - 1 + dfs(i, j));
				if(j != n2)
					printf(" ");
				else
					printf("\n");
			}
	}
	return 0;
}