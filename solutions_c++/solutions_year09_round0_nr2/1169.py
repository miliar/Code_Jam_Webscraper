#include <stdio.h>
#define MAX 128
#define INF 123123123

int n, m, color;
int a[MAX][MAX];
char b[MAX][MAX];

const int DX[] = {-1, 0, 0, 1};
const int DY[] = { 0,-1, 1, 0};

char Rec(int x, int y)
{
	if (b[x][y])
		return b[x][y];
	int minv = INF;
	int minx, miny;
	for (int i=0; i<4; i++)
	{
		int xx = x + DX[i];
		int yy = y + DY[i];
		if (xx >= 0 && xx < n && yy >= 0 && yy < m)
		{
			if (minv > a[xx][yy])
			{
				minv = a[xx][yy];
				minx = xx;
				miny = yy;
			}
		}
	}
	if (minv < a[x][y])
	{
		char c = Rec(minx, miny);
		b[x][y] = c;
		return c;
	}
	b[x][y] = color++;
	return b[x][y];
}

void Solve()
{
	scanf("%d %d", &n, &m);
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
		{
			scanf("%d", &a[i][j]);
			b[i][j] = 0;
		}
	}
	color = 'a';
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
			Rec(i, j);
	}
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
			printf("%c ", b[i][j]);
		printf("\n");
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++)
	{
		printf("Case #%d:\n", i);
		Solve();
	}
	return 0;
}
