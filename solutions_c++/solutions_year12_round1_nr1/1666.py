#include <cstdio>

const int oo = 1 << 30;
int main ()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;	scanf("%d", &tc);
	for (int T = 1; T <= tc; T++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		double p[100], f[100];
		for (int i = 0; i < a; i++)		scanf("%lf", p + i);
		for (int i = 0; i < a; i++)		f[i] = 1 - p[i];
		int tot = b + 1;
		double tem, pro = 1, ans = tot + 1;
		for (int i = 0; i < a; i++)
		{
			int cnt = a  - 1 - i + 1;
			tem = pro * (cnt + b - i + 1) + (1 - pro) * (cnt + b - i + 1 + tot);
			if (tem < ans)	ans = tem;
			pro *= p[i];
		}
		tem = pro * (b - a + 1) + (1 - pro) * (b - a + 1 + tot + 1);
		if (tem < ans)	ans = tem;
		printf("Case #%d: %.6lf\n", T, ans);
	}
}