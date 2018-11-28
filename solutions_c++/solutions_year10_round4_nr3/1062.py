#include <cstdio>
#include <cstring>

int a[110][110];
int b[110][110];

bool dead()
{
	for (int i = 1; i <= 100; ++i)
		for (int j = 1; j <= 100; ++j)
			if (a[i][j] == 1)
				return false;
	return true;
}

int solve()
{
	int T = 0;
	while (!dead())
	{
		++T;
		memset(b, 0, sizeof b);
		for (int i = 2; i <= 100; ++i)
			for (int j = 2; j <= 100; ++j)
				if (a[i][j] == 1 && (a[i - 1][j] == 1 || a[i][j - 1] == 1) || a[i - 1][j] == 1 && a[i][j - 1] == 1)
					b[i][j] = 1;
		for (int i = 1; i <= 100; ++i)
			for (int j = 1; j <= 100; ++j)
				a[i][j] = b[i][j];
	}
	return T;
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int ntc;
	scanf("%u", &ntc);
	for (int tc = 0; tc < ntc; ++tc)
	{
		memset(a, 0, sizeof a);
		int R;
		scanf("%d", &R);
		for (int i = 0; i < R; ++i)
		{
			int X1, X2, Y1, Y2;
			scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
			for (int x = X1; x <= X2; ++x)
				for (int y = Y1; y <= Y2; ++y)
					a[x][y] = 1;
		}

		printf("Case #%u: %d\n", tc + 1, solve());
	}

	return 0;
}
