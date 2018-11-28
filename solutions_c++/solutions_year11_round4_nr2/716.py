#include<cstdio>
using namespace std;

#define INPUT "B-small.in"
#define OUTPUT "B-small.out"
#define NMAX 16
#define EPS 1e-6
char A[NMAX][NMAX];
int n, m, d;

double abs(double a)
{
	return a < 0 ? -a : a;
}

int ok(int x, int y, int k)
{
	double xc = x + (double)(k - 1) / 2, yc = y + (double)(k - 1) / 2;
	double tx = 0, ty = 0;

	for(int i = 0; i < k; ++i)
		for(int j = 0; j < k; ++j)
		{
			if((i == 0 && j == 0) || (i == 0 && j == k - 1) || (i == k - 1 && j == 0) || (i == k - 1 && j == k - 1))
				continue;
			int m = d + A[x + i][y + j] - '0';
			tx += (x + i - xc) * m;
			ty += (y + j - yc) * m;
		}

	return abs(tx) < EPS && abs(ty) < EPS;
}

void solve()
{
	scanf("%d%d%d", &n, &m, &d);
	for(int i = 0; i < n; ++i)
		scanf("%s", A[i]);

	int ans = 0;
	for(int k = 3; k <= n && k <= m; ++k)
		for(int i = 0; i + k <= n; ++i)
			for(int j = 0; j + k <= m; ++j)
				if(ok(i, j, k))
					ans = k;

	if(ans)
		printf("%d\n", ans);
	else
		printf("IMPOSSIBLE\n");
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);
	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
