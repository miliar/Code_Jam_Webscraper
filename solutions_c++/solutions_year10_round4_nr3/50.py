#include <cstdio>
#include <cstring>

const int maxn = 200;
const int m = 150;

int a[maxn][maxn];
int n;

int main()
{
	int testnumber, testcount;
	int x1, y1, x2, y2;
	
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d", &n);
		memset(a, 0, sizeof a);
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int j = x1; j <= x2; j++)
				for (int k = y1; k <= y2; k++)
					a[j][k] = 1;
		}
		bool change = true;
		int res = 0;
		while (change)
		{
			res++;
			change = false;
			for (int i = m - 1; i >= 0; i--)
				for (int j = m - 1; j >= 0; j--)
					if (a[i][j] == 1 &&
						(i == 0 || a[i - 1][j] == 0) &&
						(j == 0 || a[i][j - 1] == 0))
					{
						a[i][j] = 0;
						change = true;
					}
					else
					if (a[i][j] == 0 &&
						(i != 0 && a[i - 1][j] == 1) &&
						(j != 0 && a[i][j - 1] == 1))
					{
						a[i][j] = 1;
						change = true;
					}
		}
		printf("Case #%d: %d\n", testcount + 1, res - 1);
	}
	
	return 0;
}
