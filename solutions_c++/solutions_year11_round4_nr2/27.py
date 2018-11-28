#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

ll sum[512][512];
ll x[512][512], y[512][512];
ll ar[512][512];

char temp[512];


ll get(ll ar[512][512], int x, int y)
{
	if (x < 0 || y < 0)
		return 0;
	return ar[x][y];
}

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int w, h;
	scanf("%d%d%*d", &w, &h);
	clr(sum);
	clr(x); clr(y);
	for(int i = 0; i < w; i++)
	{
		scanf("%s", temp);
		for(int j = 0; j < h; j++)
		{
			ar[i][j] = sum[i][j] = temp[j] - '0';
			x[i][j] = sum[i][j] * i;
			y[i][j] = sum[i][j] * j;
		}
	}
	for(int i = 0; i < w; i++)
		for(int j = 0; j < h; j++)
		{
			sum[i][j] += get(sum, i-1, j) + get(sum, i, j-1) - get(sum, i-1, j-1);
			x[i][j] += get(x, i-1, j) + get(x, i, j-1) - get(x, i-1, j-1);
			y[i][j] += get(y, i-1, j) + get(y, i, j-1) - get(y, i-1, j-1);
		}
	int ans = 0;
	for(int k = 3; k < 1000; k++)
		for(int i = 0; i + k <= w; i++)
			for(int j = 0; j + k <= h; j++)
			{
				ll sumx = get(x, i + k - 1, j + k - 1) 
					- get(x, i - 1, j + k - 1) 
					- get(x, i + k - 1, j - 1) 
					+ get(x, i - 1, j - 1);
				ll sumy = get(y, i + k - 1, j + k - 1) 
					- get(y, i - 1, j + k - 1) 
					- get(y, i + k - 1, j - 1) 
					+ get(y, i - 1, j - 1);
				ll sums = get(sum, i + k - 1, j + k - 1) 
					- get(sum, i - 1, j + k - 1) 
					- get(sum, i + k - 1, j - 1) 
					+ get(sum, i - 1, j - 1);
				sumx -= (ar[i][j] * i + ar[i][j+k-1] * i + ar[i+k-1][j] * (i+k-1) + ar[i+k-1][j+k-1] * (i+k-1));
				sumy -= (ar[i][j] * j + ar[i][j+k-1] * (j+k-1) + ar[i+k-1][j] * j + ar[i+k-1][j+k-1] * (j+k-1));
				sums -= (ar[i][j] + ar[i][j+k-1] + ar[i+k-1][j] + ar[i+k-1][j+k-1]);
				if (sumx * 2 == sums * (2*i + k-1) && sumy * 2 == sums * (2*j + k - 1))
					ans = k;
			}
	if (ans)
		printf("%d\n", ans);
	else
		printf("IMPOSSIBLE\n");


}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
