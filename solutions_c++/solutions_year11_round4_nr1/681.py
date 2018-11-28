#include<stdio.h>
#include<algorithm>
using namespace std;

struct C
{
	double len, sp;
};

bool cmp(C c1, C c2)
{
	return c1.sp < c2.sp;
}

C c[1111];
double x, s, r, t, st, ed;
int n;

double solve()
{
	scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
	c[n].len = x;
	for (int i = 0; i < n; i++)
	{
		scanf("%lf %lf %lf", &st, &ed, &c[i].sp);
		c[i].len = ed - st;
		c[n].len -= c[i].len;
	}
	c[n].sp = 0;
	sort(c, c + n + 1, cmp);

	double ans = 0.0;
	for (int i = 0; i <= n; i++)
	{
		if (c[i].len / (c[i].sp + r) < t)
		{
			t -= c[i].len / (c[i].sp + r);
			ans += c[i].len / (c[i].sp + r);
		} else
		{
			ans += t + (c[i].len - t * (c[i].sp + r)) / (c[i].sp + s);
			t = 0;
		}
	}
	return ans;
	
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: %.10f\n", i, solve());
	}
	return 0;
	
}
