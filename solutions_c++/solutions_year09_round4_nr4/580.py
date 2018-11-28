#include <stdio.h>
#include <math.h>

int x[5], y[5], r[5];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, t, n, i, j, k;
	double R, S;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%d%d%d", x+i, y+i, r+i);
		printf("Case #%d: ", t);
		if (n == 1)
		{
			printf("%d\n", r[0]);
			continue;
		}
		if (n == 2)
		{
			if (r[0] < r[1])
				printf("%d\n", r[1]);
			else
				printf("%d\n", r[0]);
			continue;
		}
		R = 1000000000.0;
		for (i = 0; i < n; i++)
			for (j = i+1; j < n; j++)
			{
				k = 3-i-j;
				S = (r[i]+r[j]+sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+0.0))/2.0;
				if (S < r[k])
					S = r[k];
				if (S < R)
					R = S;
			}
		printf("%.9lf\n", R);
	}
	return 0;
}
