#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 100;

int h[maxn][maxn];
int l[maxn][maxn];
int d[2][4] = {{-1, 0, 0, 1},{0, -1, 1, 0}};
int n, m, label;

void init()
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &h[i][j]);
}

int qx[maxn * maxn], qy[maxn * maxn];

void visit(int x, int y)
{
	int r = 0;
	qx[r] = x; qy[r] = y;
	while (true)
	{
		x = qx[r]; y = qy[r];
		int min = h[x][y];
		int cho = -1;
		for (int i = 0; i < 4; i++)
		{
			int nowx = x + d[0][i];
			int nowy = y + d[1][i];
			if (nowx < 0 || nowx >= n || nowy < 0 || nowy >= m) continue;
			if (h[nowx][nowy] < min)
			{
				min = h[nowx][nowy];
				cho = i;
			}
		}
		if (cho == -1) break;
		x += d[0][cho];
		y += d[1][cho];
		r++;
		qx[r] = x;
		qy[r] = y;
		if (l[x][y] != -1) break;
	}	
	int lnow = l[qx[r]][qy[r]];
	if (lnow == -1) lnow = label++;
	for (int i = 0; i <= r; i++)
		l[qx[i]][qy[i]] = lnow;
}

void work()
{
	label = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			l[i][j] = -1;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (l[i][j] == -1)
				visit(i, j);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			printf("%c ", 'a' + l[i][j]);
		printf("\n");
	}
}

int main()
{
	int caseno;
	scanf("%d", &caseno);
	for (int i = 0; i < caseno; i++)
	{
		init();
		printf("Case #%d:\n", i+1);
		work();
	}
}
