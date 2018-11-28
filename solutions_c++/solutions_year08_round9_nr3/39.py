#include <cstdio>
#include <cstring>

int test;
int v[10][10], mine[10][10];
void work()
{
	int r, c;
	int ans = 0;
	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			scanf("%d", &v[i][j]);
	memset(mine, 0, sizeof(mine));
	for (int s = 0; s < 1 << (r + c - 1); ++s)
	{
		for (int i = 0; i < c; ++i)
			if (s & (1 << i))
				mine[0][i] = 1;
			else
				mine[0][i] = 0;
		for (int i = 1; i < r; ++i)
			if (s & (1 << i + c - 1))
				mine[i][0] = 1;
			else
				mine[i][0] = 0;
		int ok = 1;
		for (int i = 1; i <= r && ok; ++i)
			for (int j = 1; j <= c && ok; ++j)
			{
				mine[i][j] = 0;
				int nv = v[i - 1][j - 1];
				for (int dx = -2; dx <= 0; ++dx)
					for (int dy = -2; dy <= 0; ++dy)
					{
						if (i + dx >= 0 && j + dy >= 0)
							nv -= mine[i + dx][j + dy];
					}
				if (nv > 1 || nv < 0)
					ok = 0;
				if (nv == 1 && (i == r || j == c))
					ok = 0;
				mine[i][j] = nv;
			}
		if (ok)
		{
			int cnt = 0;
			for (int i = 0; i < c; ++i)
				cnt += mine[(r - 1) / 2][i];
			if (cnt > ans)
				ans = cnt;
		}
	}
	printf("Case #%d: %d\n", ++test, ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
