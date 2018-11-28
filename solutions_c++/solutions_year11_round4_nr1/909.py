#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <map>
#include <set>
#include <vector>
#include <functional>
#include <algorithm>
using namespace std;

#define N 1010

struct ooo
{
	int b, e, w, flag;
	bool operator < (const ooo &o) const
	{
		return b < o.b;
	}
}a[N];

bool cmp(const ooo &o1, const ooo &o2)
{
	return o1.w < o2.w;
}

int main()
{
	int X, S, R, n, t;

	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].w);
			a[i].w += S;
			a[i].flag = 1;
		}
		sort(a, a+n);
		int flag = 0;
		for (int i = 0; i < n; ++i)
			if (a[i].b<=X && a[i].e>=X)
			{
				a[i].e = X;
				n = i + 1;
				flag = 1;
				break;
			}
		int pos = 0;
		int m = n;
		if (a[0].b)
		{
			a[m].b = 0; a[m].e = a[0].b; a[m].w = S; a[m].flag = 0;
			m++;
		}
		if (!flag)
		{
			a[m].b = a[n-1].e; a[m].e = X; a[m].w = S; a[m].flag = 0;
			m++;
		}
		for (int i = 1; i < n; ++i) if (a[i].b > a[i-1].e)
		{
			a[m].b = a[i-1].e;
			a[m].e = a[i].b;
			a[m].w = S;
			a[m].flag = 0;
			++m;
		}
		sort(a, a+m, cmp);
		double sum = 0;
		double left = t;
		for (int i = 0; i < m; ++i)
		{
			if (left > 0) {
				int speed = a[i].w - S + R;
				double u = 1.*(a[i].e-a[i].b)/speed;
				if (u > left) u = left;
				left -= u;
				sum += u;
				sum += (a[i].e-a[i].b-speed*u)/a[i].w;
			} else
				sum += 1.*(a[i].e-a[i].b)/a[i].w;
		}
// 		int len1 = a[i].b;
// 		for (int i = 1; i < n; ++i)
// 			len1 += a[i].b - a[i-1].e;
		printf("Case #%d: %.9lf\n", T, sum);
	}

	return 0;
}
