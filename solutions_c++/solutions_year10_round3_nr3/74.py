#include <algorithm>
#include <stdio.h>

using namespace std;

int n, m;
int sol[564];
int a[564][564];

inline int verif(int x, int y, int l)
{
	for (int i = x; i <= x + l - 1; i++)
		for (int j = y; j <= y + l - 1; j++)
			if ((a[i][j] ^ ((i - x + j - y) & 1)) != a[x][y])
				return 0;

	return 1;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int testCases, t = 1;
	for (scanf("%d", &testCases); testCases; t++, testCases--)
	{
		scanf("%d %d\n", &n, &m);
		memset(sol, 0, sizeof(sol));

		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j += 4)
			{
				char ch;
				scanf("%c", &ch);

				int nr;
				if ('0' <= ch && ch <= '9')
					nr = ch - '0';
				else nr = 10 + ch - 'A';

				a[i][j] = (nr & 8) / 8;
				a[i][j + 1] = (nr & 4) / 4;
				a[i][j + 2] = (nr & 2) / 2;
				a[i][j + 3] = (nr & 1);
			}
			scanf("\n");
		}

		for (int l = min(n, m); l; l--)
			for (int i = 1; i <= n - l + 1; i++)
			{
				for (int j = 1; j <= m - l + 1; j++)
					if (a[i][j] != -1 && verif(i, j, l))
					{
						sol[l]++;

						for (int x = i; x <= i + l - 1; x++)
							for (int y = j; y <= j + l - 1; y++)
								a[x][y] = -1;
					}
			}

		int rez = 0;
		for (int i = 1; i <= min(n, m); i++)
			rez += (sol[i] != 0);

		printf("Case #%d: %d\n", t, rez);

		for (int l = min(n, m); l; l--)
			if (sol[l])
				printf("%d %d\n", l, sol[l]);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
