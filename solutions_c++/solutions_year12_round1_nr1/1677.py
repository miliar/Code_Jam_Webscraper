#include <cstdio>
#include <cstring>
#include <cstdlib>

int a, b;
double p[100010];

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		double ans;
		scanf("%d%d", &a, &b);
		for (int i = 0; i < a; i++)
			scanf("%lf", &p[i]);
		ans = b + 2;
//		printf("temp = %lf\n", ans);
		for (int k = 0; k < 3; k++)
		{
			int proc = a - k;
			double pp = 1;
			if (proc < 0)
				proc = 0;
			for (int j = 0; j < proc; j++)
				pp *= p[j];
//			printf("temp = %lf\n", pp * (a + b - 2 * proc + 1) + (1 - pp) * (a + b - 2 * proc + 1 + b + 1));
			if ((pp * (a + b - 2 * proc + 1) + (1 - pp) * (a + b - 2 * proc + 1 + b + 1)) < ans)
				ans = pp * (a + b - 2 * proc + 1) + (1 - pp) * (a + b - 2 * proc + 1 + b + 1);
		}
		printf("Case #%d: %lf\n", cases, ans);
	}

	return 0;
}
