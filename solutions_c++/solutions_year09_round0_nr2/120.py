#include <iostream>
using namespace std;

const int N = 100;
const int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };
int a[N][N];
int f[N * N];
int flag[N * N];
char ret[N * N];

int find(int x)
{
	if (f[x] != f[f[x]]) f[x] = find(f[x]);
	return f[x];
}

int main()
{
	int num, cas;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &cas);
	for (num = 1; num <= cas; ++num)
	{
		int n, m;
		int i, j, k;
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j)
				scanf("%d", &a[i][j]);
		for (i = 0; i < n * m; ++i) f[i] = i;
		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j)
			{
				int min_v, min_x, min_y;
				min_v = INT_MAX;
				for (k = 0; k < 4; ++k)
				{
					int x, y;
					x = i + dir[k][0];
					y = j + dir[k][1];
					if (!(x >= 0 && x < n && y >= 0 && y < m)) continue;
					if (a[x][y] < a[i][j] && a[x][y] < min_v)
					{
						min_v = a[x][y];
						min_x = x;
						min_y = y;
					}
				}
				if (min_v != INT_MAX) f[i * m + j] = min_x * m + min_y;
			}
		memset(flag, 255, sizeof(flag));
		j = 0;
		for (i = 0; i < n * m; ++i)
		{
			f[i] = find(i);
			if (flag[f[i]] < 0)
			{
				flag[f[i]] = j++;
			}
			ret[i] = 'a' + flag[f[i]];
		}
		printf("Case #%d:\n", num);
		for (i = 0; i < n; ++i)
		{
			printf("%c", ret[f[i * m]]);
			for (j = 1; j < m; ++j)
				printf(" %c", ret[f[i * m + j]]);
			puts("");
		}
	}
	return 0;
}
