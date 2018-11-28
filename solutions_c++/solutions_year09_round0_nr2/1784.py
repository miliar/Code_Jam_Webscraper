#include<iostream>

#define N 110
using namespace std;

const int INF = 1000000;
int n, m;
int alt[N][N];
char lab[N][N], letter;
int dir[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void DFS(int r, int c)
{
	if (lab[r][c] != 0)
	{
		letter--;
		return; 
	}
	bool flag = 1;
	int minV = INF;
	int i;
	for (i = 0; i < 4; i++)
	{
		if (minV > alt[r + dir[i][0]][c + dir[i][1]]) minV = alt[r + dir[i][0]][c + dir[i][1]];
		if (alt[r][c] > alt[r + dir[i][0]][c + dir[i][1]]) flag = 0;
	}
	if (flag)
	{
		lab[r][c] = letter;
		return;
	}
	for (i = 0; i < 4; i++)
	{
		if (alt[r + dir[i][0]][c + dir[i][1]] == minV)
		{
			DFS(r + dir[i][0], c + dir[i][1]);
			lab[r][c] = lab[r + dir[i][0]][c + dir[i][1]];
			break;
		}
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		scanf("%d %d", &n, &m);
		int i, j;
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				scanf("%d", &alt[i][j]);
		for (i = 0; i <= n + 1; i++)
			alt[i][0] = alt[i][m + 1] = INF;
		for (i = 0; i <= m + 1; i++)
			alt[0][i] = alt[n + 1][i] = INF;
		memset(lab, 0, sizeof(lab));
		letter = 'a';
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
			{
				if (lab[i][j] == 0)
				{
					DFS(i, j);
					letter++;
				}
			}
		printf("Case #%d:\n", caseID++);
		for (i = 1; i <= n; i++)
		{
			printf("%c", lab[i][1]);
			for (j = 2; j <= m; j++)
				printf(" %c", lab[i][j]);
			printf("\n");
		}
	}
	return 0;
}