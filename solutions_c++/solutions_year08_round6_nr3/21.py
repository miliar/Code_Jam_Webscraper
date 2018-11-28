
	#include <cstdio>
	#include <cstdlib>
	#include <algorithm>

	int m, x;
	double p, f[50][10];

	void work()
	{
		scanf("%d%lf%d", &m, &p, &x);
		int a = 1000000;
		for (int i = 1; i <= 5; i ++)
			a /= 2;
		int b = x / a + 1;
		for (int i = 1; i <= 16; i ++)
			f[i][1] = 0;
		for (int i = 17; i <= 32; i ++)
			f[i][1] = p;
		f[33][1] = 1;
		//printf("\n");
		for (int i = 2; i <= 5; i ++)
		{
			for (int j = 1; j <= 33; j ++)
			{
				f[j][i] = 0;
				for (int k = 0; j - k >= 1 && j + k <= 33; k ++)
				{
					if (f[j][i] < f[j - k][i - 1] * (1 - p) + f[j + k][i - 1] * p)
						f[j][i] = f[j - k][i - 1] * (1 - p) + f[j + k][i - 1] * p;
				}
		//		printf("%.6lf ", f[j][i]);
			}
		//	printf("\n");
		}
		printf("%.8lf\n", f[b][m]);
	}

	int main(int argc, char *argv[])
	{
		freopen("c.in", "r", stdin);
		freopen("c.out", "w", stdout);
		int c;
		scanf("%d", &c);
		for (int testnum = 1; testnum <= c; testnum ++)
		{
			printf("Case #%d: ", testnum);
			work();
		}
		return 0;
	}
