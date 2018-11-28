#include<iostream>
#include<queue>
using namespace std;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};
const int maxl = 100;
int h, w, a[maxl][maxl], T;
bool g[maxl][maxl][4];
char ans[maxl][maxl];

void floodfill(int sx, int sy, int sym)
{
	queue< pair<int, int> > q;
	q.push(make_pair(sx, sy));
	ans[sx][sy] = sym;
	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();
		for (int i = 0; i < 4; i++)
			if (g[cur.first][cur.second][i] && ans[cur.first + dx[i]][cur.second + dy[i]] == 0)
			{
				ans[cur.first + dx[i]][cur.second + dy[i]] = sym;
				q.push(make_pair(cur.first + dx[i], cur.second + dy[i]));
			}
	}
}

int main()
{
	freopen("p2.in", "r", stdin);
	freopen("p2.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		scanf("%d %d", &h, &w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				scanf("%d", &a[i][j]);
		memset(g, 0, sizeof(g));
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
			{
				int minv = a[i][j];
				int p = -1;
				for (int k = 0; k < 4; k++)
				{
					int cx = i + dx[k], cy = j + dy[k];
					if (cx < 0 || cy < 0 || cx >= h || cy >= w) continue;
					if (a[cx][cy] < minv) minv = a[cx][cy], p = k;
				}
				if (p >= 0) g[i][j][p] = g[i + dx[p]][j + dy[p]][3 - p] = true;
			}
		
		memset(ans, 0, sizeof(ans));
		char cv = 'a';
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (ans[i][j] == 0) floodfill(i, j, cv++);
				if (j > 0) printf(" ");
				printf("%c", ans[i][j]);
			}
			printf("\n");
		}
	}
}
