#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define pb push_back
#define sz(a) (int)((a).size())
#define ll long long
#define sqr(a) ((a) * (a))

#define Nmax 128
#define MOD 10007

int n, m, r;
int mat[Nmax][Nmax];
int D[Nmax][Nmax];

void citire()
{
	int i, x0, y0;

	memset(mat, 0, sizeof(mat));

	scanf("%d %d %d\n", &n, &m, &r);
    for (i = 1; i <= r; ++i)
	{
		scanf("%d %d\n", &x0, &y0);
		mat[x0][y0] = 1;
	}
}

void solve()
{
	int i, j;

	memset(D, 0, sizeof(D));
	D[1][1] = 1;
	for (i = 1; i <= n; ++i)
		for (j = 1; j <= m; ++j)
			if (!mat[i][j])
			{
				if (i >= 2 && j >= 3) D[i][j] += D[i - 1][j - 2];
				if (i >= 3 && j >= 2) D[i][j] += D[i - 2][j - 1];
				D[i][j] %= MOD;
			}

	printf("%d\n", D[n][m]);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
