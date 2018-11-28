#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int f[400][400], g[400][400];
int n;

bool ok(int f[400][400], int a)
{
	if (a == 1 || a == n + n - 1) return true;
	bool ok = true;
	for (int delta = 1; ok && a - delta >= 1 && a + delta <= n + n - 1; ++delta)
		for (int j = 1; j <= n + n - 1 && ok; ++j)
			if (f[a - delta][j] != f[a + delta][j] && f[a - delta][j] != -1 && f[a + delta][j] != -1) ok = false;
	return ok;
}

int cal(int n)
{
	return n * n;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	scanf("%d" , &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		memset( g , -1 ,sizeof(g));
		scanf("%d" , &n);
		for (int i = 1; i <= n + n - 1; ++i)
			if (i <= n)
				for (int j = 1; j <= i; ++j) scanf("%d" , &g[i][n - i + 2 * j - 1]);
			else
				for (int j = 1; j <= n + n - i; ++j) scanf("%d" , &g[i][i - n + 2 * j - 1]);
		int a,b;
		a = b = n + n;
		for (int i = 1; i <= n + n - 1; ++i)
			for (int j = 1; j <= n + n - 1; ++j)
				f[i][j] = g[j][i];
		for (int i = 1; i <= n + n - 1; ++i)
			if (ok(g, i) && abs(n - i) < a) a = abs(n - i);
		for (int i = 1; i <= n + n - 1; ++i)
			if (ok(f, i) && abs(n - i) < b) b = abs(n - i);
		printf("Case #%d: %d\n", ca, cal(n + a + b) - cal(n));
	}
	fclose(stdin); fclose(stdout);
}
