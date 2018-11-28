#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;


const int MAXN = 3000;

int n, m;
int f[MAXN];
long long h[MAXN];


bool dfs(int st, int fn, long long a, long long b, long long c)
{
	if (st >= fn) return true;

	vector <int> s;
	int m = 0;
	long long x = st;
	while (x < fn)
	{
		s.push_back(x);
		m++;
		x = f[x];
	}

	if (x != fn)
		return false;
//	cout << endl;
//	printf("%d %d %d\n", st, fn, m);
//	fflush(stdout);
//	cout << a << " " << b << " " << c << endl;

    x = s[m - 1];
	h[x] = (-c - a * x) / b + 1;

	a = h[fn] - h[x];
	b = x - fn;
	c = -(a * x + b * h[x]);
//	cout << x << " " << h[x] << endl;
	if (!dfs(x + 1, fn, a, b, c))
		return false;

	while (m > 1)
	{
		m--;
		long long x = s[m - 1];
		long long y = s[m];
		long long z = f[s[m]];

		a = h[z] - h[y];
		b = y - z;
		c = -(a * y + b * h[y]);

		h[x] = (-c - a * x) / b + (int)((-c - a * x) % b != 0);

		a = h[x] - h[y];
		b = y - x;
		c = -(a * y + b * h[y]);

		if (!dfs(x + 1, y, a, b, c))
			return false;
	}
	return true;
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
    	memset(h, 0, sizeof(h));
    	memset(f, 0, sizeof(f));

    	scanf("%d", &n);
    	for (int i = 1; i < n; i++)
    		scanf("%d", &f[i]);
/*
    	printf("%d\n", n);
    		for (int i = 1; i < n; i++)
    		printf(" %d", f[i]);
    	printf("\n");
//*/
    	f[n] = n + 1;
    	if (!dfs(1, n + 1, 0, -1, -1))
    		printf(" Impossible");
    	else
    		for (int i = 1; i <= n; i++)
    			printf(" %d", (int)1e+9 - (int)h[i]);
    	printf("\n");
    	fflush(stdout);
    }

    fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
