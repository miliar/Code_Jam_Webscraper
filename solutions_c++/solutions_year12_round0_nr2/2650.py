#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define seta(a, b) memset(a, b, sizeof(a))

const string name = "g";

const int NMAX = 105;
int n, s, p, zn[NMAX], d[NMAX][NMAX];
int supr[30], exist_supr[30], norm[30], exist_norm[30];

int solve()
{
	seta(d, 255);
	d[0][0] = 0;
	forn(i, n)
		forn(j, s + 1)
			if (d[i][j] >= 0)
			{
				if (exist_norm[zn[i]]) d[i + 1][j] = max(d[i + 1][j], d[i][j] + norm[zn[i]]);
				if (exist_supr[zn[i]]) d[i + 1][j + 1] = max(d[i + 1][j], d[i][j] + supr[zn[i]]);
			}
	return d[n][s];
}

int main()
{
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);

	int tst;
	cin >> tst;
	forn(i, tst)
	{
		cin >> n >> s >> p;
		seta(norm, 0);
		seta(supr, 0);
		seta(exist_norm, 0);
		seta(exist_supr, 0);
		forn(x, 11)
			forn(y, 11)
				forn(z, 11)
				{
					if (max(x, max(y, z)) - min(x, min(y, z)) < 2)
					{
						exist_norm[x + y + z] = 1;
						if (max(x, max(y, z)) >= p) norm[x + y + z] = 1;
					}
					if (max(x, max(y, z)) - min(x, min(y, z)) == 2)
					{
						exist_supr[x + y + z] = 1;
						if (max(x, max(y, z)) >= p) supr[x + y + z] = 1;
					}
				}
		forn(j, n)
			scanf("%d", &zn[j]);
		printf("Case #%d: %d\n", i + 1, solve());
	}

	return 0;
}
