#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;

const int maxn = 111;

int xi[4] = {-1, 0, 0, 1},
	yi[4] = { 0, -1, 1, 0};

int k, n, m, d, t, x, y;
int a[maxn][maxn];
char c[maxn][maxn];
bool f[maxn][maxn][4];
queue <pair <int, int> > q;

int add(int x, int y)
{
	if (x < 0 || y < 0 || n <= x || m <= y || c[x][y]) return 0;
	c[x][y] = d;
	q.push(make_pair(x, y));
	return 0;
}

int main()
{
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	cin >> k;
	for (int test = 0; test < k; test++)
	{
		cin >> n >> m;
		memset(f, 0, sizeof(f));
		memset(c, 0, sizeof(c));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> a[i][j];

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				d = a[i][j];
				for (int z = 0; z < 4; z++)
				{
					x = i + xi[z];
					y = j + yi[z];
					if (x < 0 || y < 0 || n <= x || m <= y || a[x][y] >= d) continue;
					d = a[x][y];
					t = z;
				}
				if (a[i][j] <= d) continue;
				f[i][j][t] = true;
				f[i + xi[t]][j + yi[t]][3 - t] = true;
			}
		memset(c, sizeof(c), 0);
		d = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (c[i][j] == 0)
				{
					d++;
					while (q.size()) q.pop();
					add(i, j);
					while (q.size())
					{
						x = q.front().first;
						y = q.front().second;
						q.pop();
						for (int z = 0; z < 4; z++)
							if (f[x][y][z]) add(x + xi[z], y + yi[z]);
					}
				}
		printf("Case #%d:\n", test + 1);	
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m - 1; j++)
				printf("%c ", c[i][j] + 'a' - 1);
			printf("%c\n", c[i][m - 1] + 'a' - 1);
		}
	}


	return 0;
}
