#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
using namespace std;

const long long STEP = 10;

int n, m, a;

void Load()
{
	scanf("%d%d%d", &n, &m, &a);
}

int x[3], y[3];

long long GCD(long long a, long long b, long long &x, long long &y)
{
	if (a < b) return GCD(b, a, y, x);
	else if (b == 0)
	{
		x = 1;
		y = 0;
		return a;
	}
	else
	{
		long long d, xx, yy;
		d = GCD(b, a % b, xx, yy);
		x = yy;
		y = xx - (a / b) * yy;
		return d;
	}
}

int Check()
{
	int i;
	for (i = 0; i < 3; i++)
	{
		if (! ((x[i] >= 0) && (x[i] <= n) && (y[i] >= 0) && (y[i] <= m)) ) return 0;
	}
	long long s = abs(x[1] * y[2] - y[1] * x[2]);
	if (s == a) 
	{
		printf("%d %d %d %d %d %d", x[0], y[0], x[1], y[1], x[2], y[2]);
		return 1;
	}
	return 0;
}

void Solve()
{
	// bottom
	int i;
	vector<int> p;
	for (i = 1; i * i <= a; i++)
	{
		if (a % i == 0)
		{
			p.push_back(i);
			p.push_back(a / i);
		}
	}
	x[0] = y[0] = 0;
	for (i = 0; i < p.size(); i++)
	{
		x[1] = p[i];
		y[1] = 0;
		x[2] = 0;
		y[2] = a / p[i];
		if (Check()) return;
	}
	for (i = 1; i <= m; i++)
	{
		x[1] = n;
		y[1] = i;
		long long x0, y0;
		long long d = GCD(i, n, x0, y0);
		vector<long long> cts;
		cts.clear();
		cts.push_back(-x0 * a / n);
		cts.push_back(-x0 * a / n + n * d / n);
		cts.push_back(y0 * a / i);
		cts.push_back(y0 * a / i - m * d / i);
		int j;
		for (j = 0; j < cts.size(); j++)
		{
			long long ct;
			for (ct = cts[j] - STEP; ct <= cts[j] + STEP; ct++)
			{
				x[2] = x0 * a / d + n / d * ct;
				y[2] = y0 * a / d + i / d * ct;
				if (Check()) return;
			}
		}
		x0 = -x0;
		y0 = -y0;
		cts.clear();
		cts.push_back(-x0 * a / n);
		cts.push_back(-x0 * a / n + n * d / n);
		cts.push_back(y0 * a / i);
		cts.push_back(y0 * a / i - m * d / i);
		for (j = 0; j < cts.size(); j++)
		{
			long long ct;
			for (ct = cts[j] - STEP; ct <= cts[j] + STEP; ct++)
			{
				x[2] = x0 * a / d + n / d * ct;
				y[2] = y0 * a / d + i / d * ct;
				if (Check()) return;
			}
		}
	}
	printf("IMPOSSIBLE");
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}