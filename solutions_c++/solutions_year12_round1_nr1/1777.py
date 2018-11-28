#include<cstdio>
#include<cstring>

const int MAXB = 100000 + 1;
int a, b;
double p[MAXB];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%d%d", &a, &b);
		double ans = b + 2;
		double ps = 1;
		//printf("%.6lf\n", ans);
		for (int i = 1; i <= a; ++i)
		{
			double tmp;
			scanf("%lf", &p[i]);
			ps *= p[i];
			int delk = a - i;
			tmp = ps * (b - a + 1 + (delk) * 2) 
				+ ((double)1.0 - ps) * (b - a + 1 + delk * 2 + b + 1);
			if (tmp < ans)
				ans = tmp;
			//printf("%d %.6lf\n", i, tmp);
		}
		double tmp = ps * (b - a + 1) + ((double)1.0 - ps) * (b - a + 1 + b + 1);
		if (tmp < ans)
			ans = tmp;
		//printf("%.6lf\n", tmp);
		printf("Case #%d: %.6lf\n", tt, ans);
	}
	return 0;
}
