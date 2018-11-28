#include <cstdio>

using namespace std;

int R, C;
char table[50][51];

void solve()
{
	for (int r = 0; r < R; ++r)
		for (int c = 0; c < C; ++c)
			if (table[r][c] == '#')
			{
				if (r+1 == R || c+1 == C) { printf("Impossible\n"); return; }
				if (table[r][c+1] != '#' || table[r+1][c] != '#' || table[r+1][c+1] != '#') { printf("Impossible\n"); return; }

				table[r][c] = '/';
				table[r][c+1] = '\\';
				table[r+1][c] = '\\';
				table[r+1][c+1] = '/';
			}

	for (int r = 0; r < R; ++r)
		printf("%s\n", &table[r][0]);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		scanf("%d%d", &R, &C);

		for (int r = 0; r < R; ++r)
			scanf("%s", &table[r][0]);

		printf("Case #%d:\n", t);
		solve();
	}

	return 0;
}
