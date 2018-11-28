#include <cstdio>
#include <cstring>

const int maxn = 50;

int a[maxn * 2][maxn * 2];
int n;

int area(int x, int y)
{
	int max = 0;
	int a1 = (x - y) + n;
	int a2 = n - (x - y);
	int a3 = (x + y) - (n - 2);
	int a4 = (3 * n - 2) - (x + y);
	if (a1 > max) max = a1;
	if (a2 > max) max = a2;
	if (a3 > max) max = a3;
	if (a4 > max) max = a4;
	return (max * max - n * n);
}

bool inrang(int x, int y)
{
	if (x < 0 || x >= 2 * n - 1) return false;
	if (x < n) return y >= n - 1 - x && y <= n - 1 + x;
	else return y >= n - 1 - (2 * n - 2 - x) && y <= n - 1 + (2 * n - 2 - x);
}

bool test(int x, int y)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < i + 1; j++)
		{
			int xo = i;
			int yo = n - i - 1 + j * 2;
			int xp = x * 2 - xo;
			int yp = yo;
			if (inrang(xp, yp) && a[xo][yo] != a[xp][yp]) return false;
			xp = xo;
			yp = y * 2 - yo;
			if (inrang(xp, yp) && a[xo][yo] != a[xp][yp]) return false;
		}
	for (int i = n - 2; i >= 0; i--)
		for (int j = 0; j < i + 1; j++)
		{
			int xo = n * 2 - i - 2;
			int yo = n - i - 1 + j * 2;
			int xp = x * 2 - xo;
			int yp = yo;
			if (inrang(xp, yp) && a[xo][yo] != a[xp][yp]) return false;
			xp = xo;
			yp = y * 2 - yo;
			if (inrang(xp, yp) && a[xo][yo] != a[xp][yp]) return false;
		}
	return true;
}

int main()
{
	int testnumber;
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (int testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d", &n);
		memset(a, 0xff, sizeof a);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < i + 1; j++)
				scanf("%d", &a[i][n - i - 1 + j * 2]);
		for (int i = n - 2; i >= 0; i--)
			for (int j = 0; j < i + 1; j++)
				scanf("%d", &a[n * 2 - i - 2][n - i - 1 + j * 2]);
		
		int min = 0x7fffffff;
		for (int i = 0; i < n * 2 - 1; i++)
			for (int j = 0; j < n * 2 - 1; j++)
				if (area(i, j) < min && test(i, j))
					min = area(i, j);
		printf("Case #%d: %d\n", testcount + 1, min);
	}
	
	return 0;
}
