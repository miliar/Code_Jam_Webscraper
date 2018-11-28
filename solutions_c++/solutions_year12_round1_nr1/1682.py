#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

double p[100005];

double func1(int a, int b)
{
	int i, j;
	double tmp1, tmp2, ans;
	for(i = 0, tmp1 = 1.0; i < a; i++)
		tmp1 *= p[i];
	ans = (b - a + 1) * tmp1;
	tmp2 = 1 - tmp1;
	ans += tmp2 * (2 * b + 2 - a);
	return ans;
}

double func2(int a, int b)
{
	int i, j, k;
	double tmp1, tmp2, mmin, ans;
	mmin = 100000000;
	for(i = 0, tmp1 = 1.0; i < a; i++)
		tmp1 *= p[i];
	for(i = 1; i <= a; i++)
	{
		ans = tmp1 * (2 * i + b - a + 1);
		for(j = 0; j < a; j++)
		{
			tmp2 = 1;
			for(k = 0; k < j; k++)
				tmp2 *= p[k];
			tmp2 *= (1 - p[j]);
			if(a - i <= j)
				ans += tmp2 * (b - a + 2 * i + 1);
			else
				ans += tmp2 * (2 * b - a + 2 * i + 2);
		}
		if(ans < mmin)
			mmin = ans;
	}
	return mmin;
}

double func3(int a, int b)
{
	double ans;
	ans = b + 2;
	return ans;
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, i, a, b, cas = 1;
	double ans, tmp;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d %d", &a, &b);
		for(i = 0; i < a; i++)
			scanf("%lf", &p[i]);
		ans = func1(a, b);
		tmp = func2(a, b);
		if(tmp < ans)
			ans = tmp;
		tmp = func3(a, b);
		if(tmp < ans)
			ans = tmp;
		printf("Case #%d: %.06lf\n", cas++, ans);
	}
	return 0;
}
