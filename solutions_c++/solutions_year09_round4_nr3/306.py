#include <cstdio>
#include <vector>
#include <memory.h>

using namespace std;

int sgn(int a, int b)
{
	if (a < b)
		return -1;
	if (a > b)
		return 1;
	return 0;
}

struct stock_s
{
	vector<int> li;

	bool cross(const stock_s &other)
	{
		int N = li.size();
		int i;
		for (i = 0;i < N - 1;i++)
		{
			int sign_1 = sgn(li[i], other.li[i]);
			int sign_2 = sgn(li[i + 1], other.li[i + 1]);
			if (!sign_1 || !sign_2)
				return true;
			if (sign_1 != sign_2)
				return true;
		}
		if (sgn(li[N - 1], other.li[N - 1]) == 0)
			return true;
		return false;
	}
} stock[16];

int adj[16][16];

int main()
{
	int t;
	scanf("%d", &t);
	int ti;
	for (ti = 1;ti <= t;ti++)
	{
		memset(adj, 0, sizeof(adj));
		int R, C;
		scanf("%d %d", &R, &C);
		int i, j;
		for (i = 0;i < R;i++)
		{
			stock[i].li.clear();
			for (j = 0;j < C;j++)
			{
				int v;
				scanf("%d", &v);
				stock[i].li.push_back(v);
			}
		}

		for (i = 0;i < R;i++)
		{
			for (j = 0;j < R;j++)
			{
				if (i == j)
					continue;

				if (stock[i].cross(stock[j]))
				{
					adj[i][j] = true;
					//fprintf(stderr, "%d/%d\n", i, j);
				}
			}
		}

		int ans = 0;
		for (i = 0;i < (1 << R);i++)
		{
			int cnt = 0;
			for (j = 0;j < R;j++)
				cnt += (i >> j) & 1;
			if (cnt <= ans)
				continue;

			int k;
			for (j = 0;j < R;j++)
			{
				if (!((i >> j) & 1))
					continue;
				for (k = j + 1;k < R;k++)
				{
					if (!((i >> k) & 1))
						continue;
					if (!adj[j][k])
						break;
				}
				if (k != R)
					break;
			}
			if (j != R)
				continue;

			ans = cnt;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
}
