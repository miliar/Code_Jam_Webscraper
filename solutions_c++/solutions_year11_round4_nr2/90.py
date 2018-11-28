#include <cstdio>
#include <memory.h>
#include <algorithm>

using namespace std;

long long sum_r[512][512], sum_c[512][512], sum_mass[512][512];
int R, C, D;

char data[512][512];

long long it;

inline long long get_v(long long (&v)[512][512], int r, int c)
{
	return (r >= 0 && c >= 0) ? v[r][c] : 0LL;
}

inline long long get_r(int sr, int sc, int sz)
{
	return get_v(sum_r, sr + sz - 1, sc + sz - 1)
		- get_v(sum_r, sr + sz - 1, sc - 1)
		- get_v(sum_r, sr - 1, sc + sz - 1)
		+ get_v(sum_r, sr - 1, sc - 1)
		- data[sr][sc] * sr
		- data[sr + sz - 1][sc] * (sr + sz - 1)
		- data[sr][sc + sz - 1] * sr
		- data[sr + sz - 1][sc + sz - 1] * (sr + sz - 1);
}

inline long long get_c(int sr, int sc, int sz)
{
	return get_v(sum_c, sr + sz - 1, sc + sz - 1)
		- get_v(sum_c, sr + sz - 1, sc - 1)
		- get_v(sum_c, sr - 1, sc + sz - 1)
		+ get_v(sum_c, sr - 1, sc - 1)
		- data[sr][sc] * sc
		- data[sr + sz - 1][sc] * sc
		- data[sr][sc + sz - 1] * (sc + sz - 1)
		- data[sr + sz - 1][sc + sz - 1] * (sc + sz - 1);
}

inline long long get_mass(int sr, int sc, int sz)
{
	return get_v(sum_mass, sr + sz - 1, sc + sz - 1)
		- get_v(sum_mass, sr + sz - 1, sc - 1)
		- get_v(sum_mass, sr - 1, sc + sz - 1)
		+ get_v(sum_mass, sr - 1, sc - 1)
		- data[sr][sc]
		- data[sr + sz - 1][sc]
		- data[sr][sc + sz - 1]
		- data[sr + sz - 1][sc + sz - 1];
}

int go()
{
	for (int sz = min(R, C);sz >= 3;sz--)
	{
		for (int i = 0;i < R - sz + 1;i++)
		{
			for (int j = 0;j < C - sz + 1;j++)
			{
				long long sr = get_r(i, j, sz);
				long long sc = get_c(i, j, sz);

				long long midr = 2 * i + sz - 1;
				long long midc = 2 * j + sz - 1;
				long long sm = get_mass(i, j, sz);

				it++;

				if (sr * 2 == midr * sm && sc * 2 == midc * sm)
					return sz;
			}
		}
	}
	return -1;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int ti = 1;ti <= t;ti++)
	{
		fprintf(stderr, "Case %d\n", ti);
		scanf("%d %d %d", &R, &C, &D);
		for (int i = 0;i < R;i++)
			scanf("%s", data[i]);

		for (int i = 0;i < R;i++)
		{
			for (int j = 0;j < C;j++)
			{
				data[i][j] -= '0';
				data[i][j] += D;
			}
		}

		memset(sum_r, 0, sizeof(sum_r));
		memset(sum_c, 0, sizeof(sum_c));
		memset(sum_mass, 0, sizeof(sum_mass));

		for (int i = 0;i < R;i++)
		{
			for (int j = 0;j < C;j++)
			{
				sum_r[i][j] = get_v(sum_r, i - 1, j)
							+ get_v(sum_r, i, j - 1)
							- get_v(sum_r, i - 1, j - 1)
							+ data[i][j] * i;
				sum_c[i][j] = get_v(sum_c, i - 1, j)
							+ get_v(sum_c, i, j - 1)
							- get_v(sum_c, i - 1, j - 1)
							+ data[i][j] * j;
				sum_mass[i][j] = get_v(sum_mass, i - 1, j)
							+ get_v(sum_mass, i, j - 1)
							- get_v(sum_mass, i - 1, j - 1)
							+ data[i][j];
			}
		}

		int ans = go();
		printf("Case #%d: ", ti);
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
		fprintf(stderr, "# %lld\n", it);
	}
	return 0;
}
