#include <cstdio>
#include <cstring>

using namespace std;

#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)

int main()
{
//	freopen("A.in", "rt", stdin);
//	freopen("A.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int nr[3][3];
		memset( nr, 0, sizeof(nr) );

		int N, A, B, C, D, X, Y, MOD;
		scanf("%d %d %d %d %d %d %d %d", &N, &A, &B, &C, &D, &X, &Y, &MOD);
		nr[X % 3][Y % 3]++;
		for (int i = 1; i < N; i++)
		{
			X = (A * (long long)X + B) % MOD;
			Y = (C * (long long)Y + D) % MOD;
			nr[X % 3][Y % 3]++;
		}

		long long rez = 0;
		FOR(a, 0, 3) FOR(b, 0, 3) FOR(c, 0, 3)
		{
			if ((a + b + c) % 3 != 0)
				continue;
			FOR(d, 0, 3) FOR(e, 0, 3) FOR(f, 0, 3)
			{
				if ((d + e + f) % 3 != 0)
					continue;

				long long cur = 1;
				int selected[3][3];
				memset( selected, 0, sizeof(selected) );

				selected[a][d]++;
				selected[b][e]++;
				selected[c][f]++;
				FOR(i, 0, 3) FOR(j, 0, 3)
				{
					if (selected[i][j] >= 1)
						cur *= nr[i][j];
					if (selected[i][j] >= 2)
						cur *= nr[i][j] - 1;
					if (selected[i][j] >= 3)
						cur *= nr[i][j] - 2;
				}

				rez += cur;
			}
		}
		printf("Case #%d: %lld\n", t, rez / 6);
	}

	return 0;
}


