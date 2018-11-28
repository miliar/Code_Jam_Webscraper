#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int R, q;
bool cur[100][100], prev[100][100];

void solve()
{
	int res = 0;
	while (q != 0)
	{
		++res;
		memcpy(cur, prev, sizeof(prev));

		for (int x = 0; x < 100; ++x)
			for (int y = 0; y < 100; ++y)
			{
				if (x > 0 && y > 0 && prev[x-1][y] && prev[x][y-1]) cur[x][y] = true;
				if (x > 0 && y > 0 && !prev[x-1][y] && !prev[x][y-1]) cur[x][y] = false;
				if (x == 0 && y > 0 && !prev[x][y-1]) cur[x][y] = false;
				if (y == 0 && x > 0 && !prev[x-1][y]) cur[x][y] = false;
				if (x == 0 && y == 0) cur[x][y] = false;
			}

		memcpy(prev, cur, sizeof(cur));
		q = 0;
		for (int x = 0; x < 100; ++x) for (int y = 0; y < 100; ++y) if (prev[x][y]) ++q;
	}

	printf("%d\n", res);
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int C;
	scanf("%d", &C);

	for (int t = 1; t <= C; ++t)
	{
		memset(prev, 0, sizeof(prev));
		scanf("%d", &R);

		for (int i = 0; i < R; ++i)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);

			for (int x = x1-1; x < x2; ++x) for (int y = y1-1; y < y2; ++y)
			{
				if (!prev[x][y]) ++q;
				prev[x][y] = true;
			}
		}

		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
