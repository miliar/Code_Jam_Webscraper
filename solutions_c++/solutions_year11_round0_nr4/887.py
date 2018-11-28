#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

int n, a[1100];
double d[1100], p[1100], f[1100];
bool used[1100];

void precalc()
{
	d[1] = 0.0;
	f[0] = 1;
	for (int i = 1; i <= 1000; i ++)
		f[i] = f[i - 1] * (double)(i);
	p[0] = 1, p[1] = 0;
	for (int i = 2; i <= 1000; i ++)
		p[i] = (i - 1) * (p[i - 1] + p[i - 2]);

	for (int i = 2; i <= 1000; i ++)
	{
		double A = 1.0, B = 0.0;
		for (int j = 1; j < i; j ++)
			A += p[j] * d[j] / f[j] / f[i - j];
		B = p[i] / f[i];
		d[i] = A / (1.0 - B);
	}
}

void solve(int test)
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i ++)
		scanf("%d", &a[i]);
	for (int i = 1; i <= n; i ++)
		used[i] = false;

	double res = 0.0;
	for (int i = 1; i <= n; i ++)
		if (!used[i])
		{
			int t = i, k = 0;
			while (!used[t]) used[t] = true, t = a[t], k ++;
			if (k == 1) k = 0;
			res += k;
		}
	printf("Case #%d: %.10lf\n", test, res);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//precalc();
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++)
		solve(i);
	return 0;
}