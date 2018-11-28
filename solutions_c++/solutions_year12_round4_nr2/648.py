#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define N 10
#define T 100
#define MAX 1000000000

double randDouble()
{
	double ans = 0, tmp;
	for (int i=0;i<T;++i)
		ans+=rand()/32767.;
	ans = ans/T*MAX;
	return ans;
}

double mod(double value, int div)
{
	return value-int(value/div)*div;
}

double dis(double x1, double y1, double x2, double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
	srand(time(NULL));
	int t;
	int n, w, l;
	int ans;
	int r[N];
	double ansX[N], ansY[N];
	scanf("%d", &t);
	for (int i=1;i<=t;++i)
	{
		ans = 0;
		scanf("%d%d%d", &n, &w, &l);
		for (int j=0;j<n;++j)
			scanf("%d", &r[j]);
		while (!ans)
		{
			ans = 1;
			for (int j=0;j<n;++j)
			{
				ansX[j] = mod(randDouble(), w);
				ansY[j] = mod(randDouble(), l);
				for (int k=0;k<j;++k)
					if (dis(ansX[j], ansY[j], ansX[k], ansY[k])<r[j]+r[k])
					{
						ans = 0;
						break;
					}
				if (!ans)
					break;
			}
		}
		printf("Case #%d:", i);
		for (int j=0;j<n;++j)
			printf(" %lf %lf", ansX[j], ansY[j]);
		printf("\n");
	}
	return 0;
}
