#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;


const int MAXN = 20;

int n, l, w;
int r[MAXN];
int x[MAXN], y[MAXN];

template <typename T> T abs(T x) { return x < 0? -x : x; }

bool check(int i, int j)
{
	return !(max(abs(x[i] - x[j]), abs(y[i] - y[j])) >= r[i] + r[j]);
}

bool dfs(int m)
{
	if (m)
	{
		if (x[m - 1] < 0) x[m - 1] = 0;
		if (x[m - 1] > w) x[m - 1] = w;
		if (y[m - 1] < 0) y[m - 1] = 0;
		if (y[m - 1] > l) y[m - 1] = l;
	}

	for (int i = 0; i < m - 1; i++)
		if (check(i, m - 1)) return false;

	if (m == n)
		return true;
	x[m] = 0;
	y[m] = 0;
	if (dfs(m + 1)) return true;
	x[m] = w;
	y[m] = 0;
	if (dfs(m + 1)) return true;
	x[m] = 0;
	y[m] = l;
	if (dfs(m + 1)) return true;
	x[m] = w;
	y[m] = l;
	if (dfs(m + 1)) return true;

	for (int i = 0; i < m - 1; i++)
	{
		x[m] = x[i] - r[i] - r[m];
		y[m] = y[i] - r[i] + r[m];
		if (dfs(m + 1)) return true;
		x[m] = x[i] - r[i] - r[m];
		y[m] = y[i] + r[i] - r[m];
		if (dfs(m + 1)) return true;
		x[m] = x[i] + r[i] + r[m];
		y[m] = y[i] - r[i] + r[m];
		if (dfs(m + 1)) return true;
		x[m] = x[i] + r[i] + r[m];
		y[m] = y[i] + r[i] - r[m];
		if (dfs(m + 1)) return true;

		y[m] = y[i] - r[i] - r[m];
		x[m] = x[i] - r[i] + r[m];
		if (dfs(m + 1)) return true;
		y[m] = y[i] - r[i] - r[m];
		x[m] = x[i] + r[i] - r[m];
		if (dfs(m + 1)) return true;
		y[m] = y[i] + r[i] + r[m];
		x[m] = x[i] - r[i] + r[m];
		if (dfs(m + 1)) return true;
		y[m] = y[i] + r[i] + r[m];
		x[m] = x[i] + r[i] - r[m];
		if (dfs(m + 1)) return true;
	}
	return false;
}

int main()
{
    freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);

    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
    	printf("Case #%d:", t);
    	scanf("%d %d %d", &n, &w, &l);
    	for (int i = 0; i < n; i++)
    		scanf("%d", &r[i]);

    	if (dfs(0))
    	{
    		for (int i = 0; i < n; i++)
    			printf(" %.2lf %.2lf", (double)x[i], (double)y[i]);
    		printf("\n");
    	}
    }

    fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
