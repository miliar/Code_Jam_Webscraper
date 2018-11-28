#include <cstdio>
using namespace std;

int t;
int n;
char a[110][110];
double b;
double mowp[110];

double WP(int i, int k)
{
	double g;
	int h;
	int j;

	g = h = 0;
	for (j = 0; j < n; ++j)
		if (j != k && a[i][j] != '.')
		{
			++h;
			g += a[i][j] - '0';
		}
	return g / h;
}
double OWP(int i)
{
	double g;
	int h;
	int j;

	if (mowp[i] >= 0)
		return mowp[i];
	g = h = 0;
	for (j = 0; j < n; ++j)
		if (a[i][j] != '.')
		{
			++h;
			g += WP(j, i);
		}
	mowp[i] = g / h;
	return mowp[i];
}
double OOWP(int i)
{
	double g;
	int h;
	int j;

	g = h = 0;
	for (j = 0; j < n; ++j)
		if (a[i][j] != '.')
		{
			++h;
			g += OWP(j);
		}
	return g / h;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int i, j, k;
		
	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d", &n);
		for (j = 0; j < n; ++j)
		{
			scanf("%s", a + j);
			mowp[j] = -1;
		}
		printf("Case #%d:\n", i);
		for (j = 0; j < n; ++j)
			printf("%.6lf\n", 0.25 * WP(j, -1) + 0.5 * OWP(j) + 0.25 * OOWP(j));
	}
	return 0;
}