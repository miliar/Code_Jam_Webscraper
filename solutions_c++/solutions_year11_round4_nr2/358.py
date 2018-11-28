#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

const double eps = 1e-8;

bool Equal(double a, double b)
{
	return fabs(a-b) < eps;
}

bool Less(double a, double b)
{
	return a < b && (!Equal(a, b));
}

bool Great(double a, double b)
{
	return a > b && (!Equal(a, b));
}

const int SZ = 600;
int h, w, d;
long long f[SZ][SZ];
char str[SZ][SZ];


void Scan()
{	
	scanf("%d%d%d", &h, &w, &d);
	for (int i = 0; i < h; i++)
		scanf("%s", str[i]);
	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++)
			f[i][j] = d + (str[i-1][j-1] - '0');
}

long long sx[SZ][SZ];
long long sy[SZ][SZ];
long long sc[SZ][SZ];

void Solve()
{
	for (int i = 1; i <= h; i++)
	{
		for (int j = 1; j <= w; j++)
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
	for (int k = 3; k <= h && k <= w; k++)
	{
		for (int i = 1; i+k-1<=h; i++)
			for (int j = 1; j+k-1<=w; j++)
			{
				long long x = sx[i+k-1][j+k-1] - sx[i-1][j+k-1] - sx[i+k-1][j-1] + sx[i-1][j-1] - f[i][j]*i - f[i+k-1][j]*(i+k-1) - f[i][j+k-1]*i - f[i+k-1][j+k-1]*(i+k-1);
				long long y = sy[i+k-1][j+k-1] - sy[i-1][j+k-1] - sy[i+k-1][j-1] + sy[i-1][j-1] - f[i][j]*j - f[i+k-1][j]*j - f[i][j+k-1]*(j+k-1) - f[i+k-1][j+k-1]*(j+k-1);
				long long c = sc[i+k-1][j+k-1] - sc[i-1][j+k-1] - sc[i+k-1][j-1] + sc[i-1][j-1] - f[i][j] - f[i+k-1][j] - f[i][j+k-1] - f[i+k-1][j+k-1];
				if ((2*x == c*k-c+2*i*c) &&
					(2*y == c*k-c+2*j*c))
				{
					ans = k;
				}
			}
	}
	if (ans == -1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		fprintf(stderr, "test %d\n", i+1);
		printf("Case #%d: ", i+1);
		Solve();
	}
	return 0;
}