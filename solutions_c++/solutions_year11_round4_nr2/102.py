#include <cstdio>
#include <cstring>

const int MAXN = 510;

int n, m, D;
int a[MAXN][MAXN];
char s[MAXN];
long long b[MAXN][MAXN];
long long c[MAXN][MAXN], d[MAXN][MAXN];

inline int min(int a, int b) { return (a<b) ? a : b;}

void init()
{
	scanf("%d %d %d", &n, &m, &D);
	int i, j;
	for (i=1; i<=n; ++i)
	{
		scanf("%s", s+1);
		for (j=1; j<=m; ++j)
			a[i][j] = s[j] - '0';
	}
}

long long getx(int x1, int y1, int x2, int y2)
{
	long long t = c[x2][y2] - c[x1-1][y2] - c[x2][y1-1] + c[x1-1][y1-1];
	t -= x1 * (a[x1][y1] + a[x1][y2]) + x2 * (a[x2][y1] + a[x2][y2]);
	return t;
}
long long gety(int x1, int y1, int x2, int y2)
{
	long long t = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1];
	t -= y1 * (a[x1][y1] + a[x2][y1]) + y2 * (a[x1][y2] + a[x2][y2]);
	return t;
}

long long getsum(int x1, int y1, int x2, int y2)
{
	long long t = b[x2][y2] - b[x1-1][y2] - b[x2][y1-1] + b[x1-1][y1-1];
	t -= a[x1][y1] + a[x2][y1] + a[x1][y2] + a[x2][y2];
	return t;
}

bool check(int x1, int y1, int x2, int y2)
{
	long long tx = getx(x1, y1, x2, y2) * 2;
	long long ty = gety(x1, y1, x2, y2) * 2;
	long long kx = getsum(x1, y1, x2, y2) * (x2 + x1);
	long long ky = getsum(x1, y1, x2, y2) * (y2 + y1);
	return (tx == kx) && (ty == ky);
}

void solve()
{
	memset(b, 0, sizeof(b));
	memset(c, 0, sizeof(c));
	memset(d, 0, sizeof(d));
	int i, j, k;
	for (i=1; i<=n; ++i)
	for (j=1; j<=m; ++j)
		b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1] + a[i][j];
	for (i=1; i<=n; ++i)
	for (j=1; j<=m; ++j)
		c[i][j] = c[i-1][j] + c[i][j-1] - c[i-1][j-1] + i * a[i][j];
	for (i=1; i<=n; ++i)
	for (j=1; j<=m; ++j)
		d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + j * a[i][j];
	for (k=min(n, m); k>=3; --k)
	{
		for (i=1; i<=n-k+1; ++i)
		for (j=1; j<=m-k+1; ++j)
			if (check(i, j, i+k-1, j+k-1))
			{
				printf("%d\n", k);
				return;
			}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int CASE, TT;
	scanf("%d", &TT);
	for (CASE=1; CASE<=TT; ++CASE)
	{
		init();
		printf("Case #%d: ", CASE);
		solve();
	}
	return 0;
}

