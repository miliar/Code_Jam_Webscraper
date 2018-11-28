#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;


long long f[646][646];
char s[646][646];
long long sx[646][646];
long long sy[646][646];
long long sc[646][646];



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		int n, m, d;
		fprintf(stderr, "%d\n", _);
		scanf("%d%d%d", &n, &m, &d);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				f[i][j] = d + (s[i-1][j-1] - '0');
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				sx[i][j] = sx[i][j-1];
				sy[i][j] = sy[i][j-1];
				sc[i][j] = sc[i][j-1];
				for (int k = 1; k <= i; k++)
				{
					sx[i][j] += f[k][j] * k;
					sy[i][j] += f[k][j] * j;
					sc[i][j] += f[k][j];
				}
			}
		}
		int ans = -1;
		long long x, y, c;
		for (int k = 3; k <= n && k <= m; k++)
		{
			for (int i = 1; i + k - 1 <= n; i++)
				for (int j = 1; j + k - 1 <= m; j++)
				{
					x = sx[i+k-1][j+k-1] - sx[i-1][j+k-1] - sx[i+k-1][j-1] + sx[i-1][j-1] - f[i][j]*i - f[i+k-1][j]*(i+k-1) - f[i][j+k-1]*i - f[i+k-1][j+k-1]*(i+k-1);
					y = sy[i+k-1][j+k-1] - sy[i-1][j+k-1] - sy[i+k-1][j-1] + sy[i-1][j-1] - f[i][j]*j - f[i+k-1][j]*j - f[i][j+k-1]*(j+k-1) - f[i+k-1][j+k-1]*(j+k-1);
					c = sc[i+k-1][j+k-1] - sc[i-1][j+k-1] - sc[i+k-1][j-1] + sc[i-1][j-1] - f[i][j] - f[i+k-1][j] - f[i][j+k-1] - f[i+k-1][j+k-1];
					if (2 * x == c * k - c + 2 * i * c && 2 * y == c * k - c + 2 * j * c)
					{
						ans = k;
					}
				}
		}
		printf("Case #%d: ", _ + 1);
		if(ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}