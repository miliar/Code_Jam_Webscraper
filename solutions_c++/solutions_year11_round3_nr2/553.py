#include<cstdio>
#include<vector>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
using namespace std;
#define N 1111

int a[N], b[N], l, n, c, T, s, ans, m, k, f, d, F[N];
LL t;

LL _max(LL a, LL b)
{
	return a > b ? a : b;
}

int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	cin>> T;
	for (int tt = 1; tt <= T; tt++)
	{
		cin>> l>> t>> n>> c;
		for (int i = 1; i <= c; i++) cin>> b[i];
		m = 0, k = 1;
		memset(F, 0, sizeof(F));
		while (m < n)
		{
			a[++m] = b[k++];
			if (k > c) k = 1;
			F[m] = F[m - 1] + a[m];
		}
		printf("Case #%d: ", tt);
		if (l == 0) cout<< F[m] * 2<< endl;
		if (l == 1)
		{
			ans = 2000000000;
			for (int i = 1; i <= m; i++)
			{
				s = f = 0;
				for (int j = 1; j <= m; j++)
				{
					if (s + a[j] * 2 >= t) f = 1;
					if (i == j && f)
					{
						d = a[j] - _max(0, t - s) / 2;
						s += (a[j] - d) * 2 + d;
					}else s += a[j] * 2;
				}
				if (s < ans) ans = s;
			}
			cout<< ans<< endl;
		}
		if (l == 2)
		{
			ans = 2000000000;
			for (int i = 1; i <= m; i++) for (int w = i + 1; w <= m; w++)
			{
				s = f = 0;
				for (int j = 1; j <= m; j++)
				{
					if (s + a[j] * 2 >= t) f = 1;
					if ((i == j || w == j) && f)
					{
						d = a[j] - _max(0, t - s) / 2;
						s += (a[j] - d) * 2 + d;
					}else s += a[j] * 2;
				}
				if (s < ans) ans = s;
			}
			cout<< ans<< endl;
		}
	}
	return 0;
}
