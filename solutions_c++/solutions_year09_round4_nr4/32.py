#include <cstdio>
#include <cstring>
#include <cmath>


int nt;


int n, x[100], y[100], r[100];

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d", &n);

		for(int i = 0; i < n; i++) scanf("%d %d %d", &x[i], &y[i], &r[i]);

/*		double L = 0, R = 1e8;

		while(R - L > 1e-8)
		{
			double x = (L + R) / 2;

			bool good = false;

			for(int i1 = 0; i1 < n; i1++)
			for(int i2 = 0; i2 < n; i2++)
			for(int i3 = 0; i3 < n


			if (good) R = x; else L = x;
		}*/

		double res = 0;

		for(int i = 0; i < n; i++) if (res < r[i]) res = r[i];

		if (n > 2)
		{
			double res2 = 1e8;

			for(int i = 0; i < n; i++)
			for(int j = i + 1; j < n; j++)
			{
				double cur = sqrt((double)(x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) + r[i] + r[j];

				if (cur < res2) res2 = cur;
			}

			res2 /= 2;

			if (res2 > res) res = res2;
		}

		printf("%.8lf\n", res);


	}

	return 0;	
}