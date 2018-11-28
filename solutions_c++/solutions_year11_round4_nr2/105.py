#include <cstdio>
#include <cmath>

using namespace std;

int n, m;
char mat[501][501];
double sumx[501][501], sumy[501][501];
double sumcx[501][501], sumcy[501][501];

const double eps = 1e-8;

void init()
{
	int d;
	scanf("%d%d%d", &n, &m, &d);
	for (int i = 0; i < n; i++) {
		scanf("%s", mat[i]);
	}
}

double getSumx(int x, int y) 
{
	if (x < 0 || y < 0) return 0;
	return sumx[x][y];
}

double getSumy(int x, int y) 
{
	if (x < 0 || y < 0) return 0;
	return sumy[x][y];
}

double getSumcx(int x, int y) 
{
	if (x < 0 || y < 0) return 0;
	return sumcx[x][y];
}

double getSumcy(int x, int y) 
{
	if (x < 0 || y < 0) return 0;
	return sumcy[x][y];
}

double calcx(int x, int  y)
{
	return (double)(mat[x][y] - '0') * ((double)x + 0.5);
}

double calcy(int x, int  y)
{
	return (double)(mat[x][y] - '0') * ((double)y + 0.5);
}

double calccx(int x, int y)
{
	return mat[x][y] - '0';
}

double calccy(int x, int y)
{
	return mat[x][y] - '0';
}

bool check(int ans)
{
	for (int i = 0; i <= n - ans; i++) {
		for (int j = 0; j <= m - ans; j++) {
			double left = getSumx(i + ans - 1, j + ans - 1) - getSumx(i + ans - 1, j - 1) - getSumx(i - 1, j + ans - 1) + getSumx(i - 1, j - 1) - calcx(i, j) - calcx(i + ans - 1, j) - calcx(i, j + ans - 1) - calcx(i + ans - 1, j + ans - 1);
			double right = (getSumcx(i + ans - 1, j + ans - 1) - getSumcx(i + ans - 1, j - 1) - getSumcx(i - 1, j + ans - 1) + getSumcx(i - 1, j - 1) - calccx(i, j) - calccx(i + ans - 1, j) - calccx(i, j + ans - 1) - calccx(i + ans - 1, j + ans - 1)) * ((double)i + (double)ans / 2.0);
			if (fabs(left - right) > eps) continue;
			left = getSumy(i + ans - 1, j + ans - 1) - getSumy(i + ans - 1, j - 1) - getSumy(i - 1, j + ans - 1) + getSumy(i - 1, j - 1) - calcy(i, j) - calcy(i + ans - 1, j) - calcy(i, j + ans - 1) - calcy(i + ans - 1, j + ans - 1);
			right = (getSumcy(i + ans - 1, j + ans - 1) - getSumcy(i + ans - 1, j - 1) - getSumcy(i - 1, j + ans - 1) + getSumcy(i - 1, j - 1) - calccy(i, j) - calccy(i + ans - 1, j) - calccy(i, j + ans - 1) - calccy(i + ans - 1, j + ans - 1)) * ((double)j + (double)ans / 2.0);
			if (fabs(left - right) > eps) continue;
			return true;
		}
	}
	return false;
}

void work()
{
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			sumx[i][j] = getSumx(i - 1, j) + getSumx(i, j - 1) - getSumx(i - 1, j - 1) + ((double)i + 0.5) * (double)(mat[i][j] - '0');
			sumy[i][j] = getSumy(i - 1, j) + getSumy(i, j - 1) - getSumy(i - 1, j - 1) + ((double)j + 0.5) * (double)(mat[i][j] - '0');
			sumcx[i][j] = getSumcx(i - 1, j) + getSumcx(i, j - 1) - getSumcx(i - 1, j - 1) + (double)(mat[i][j] - '0');
			sumcy[i][j] = getSumcy(i - 1, j) + getSumcy(i, j - 1) - getSumcy(i - 1, j - 1) + (double)(mat[i][j] - '0');
		}
	}
	for (int ans = n; ans >= 3; ans--) {
		if (check(ans)) {
			printf("%d\n", ans);
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%d: ", tt);
		init();
		work();
	}
}