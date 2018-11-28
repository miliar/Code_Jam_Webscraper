#include<iostream>
#include<sstream>
using namespace std;

int n, c;
double M[1000];

int bp(int x)
{
	int ret = 0;
	while (x)
	{
		ret++;
		x -= (x&-x);
	}
	return ret;
}

double comb(int n, int m)
{
	return m ? 1.0 * comb(n - 1,m - 1) * n / m : 1;
}

void dfs(int now)
{
	if (now == c)
	{
		M[now] = 0.0;
		return;
	}
	double p[50] = {0.0};
	for (int i = now; i <= c; i++)
	{
		if (c >= now && n-i+now>=0 && n-i+now<=now)
			p[i] = comb(c - now, i - now) * comb(now, n-i+now) / comb(c, n);
		if (i != now && M[i] < 0)
			dfs(i);
	}

	double num = 0.0;
	for (int i = 0; i <= c; i++)
	{
		if (i != now)
		{
			num += p[i] * M[i];
		}
	}
	M[now] = (1.0 + num) / (1 - p[now]);
}
	
int main()
{
	int tc;
	scanf("%d", &tc);
	for (int T = 1; T <= tc; T++)
	{
		for (int i = 0; i < 1000; i++)
			M[i] = -1.0;
		scanf("%d %d", &c, &n);
		dfs(0);
		printf("Case #%d: %.10lf\n", T, M[0]);
	}
	return 0;
}
