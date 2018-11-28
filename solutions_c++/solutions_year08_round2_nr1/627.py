#include <stdio.h>

bool find(__int64 cx, __int64 cy, __int64 x[], __int64 y[], int t)
{
	for (int i=0; i<t; i++)
	{
		if (cx==x[i] && cy==y[i])
			return true;
	}
	return false;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int n;
	scanf("%d", &n);
	int now = 1;
	while (now <= n)
	{
		int t;
		__int64 a, b, c, d, x0, y0, m;
		__int64 x[200], y[200];
		scanf("%d", &t);
		scanf("%I64d", &a);
		scanf("%I64d", &b);
		scanf("%I64d", &c);
		scanf("%I64d", &d);
		scanf("%I64d", &x0);
		scanf("%I64d", &y0);
		scanf("%I64d", &m);
		x[0] = x0; y[0] = y0;
		int i,j,k;
		for (i=1; i<= t-1; i++)
		{
			x[i]=(a*x[i-1]+b)%m;
			y[i]=(c*y[i-1]+d)%m;
		}
		int count = 0;
		for (i=0; i<t-2; i++)
			for (j=i+1; j<t-1; j++)
				for(k=j+1; k<t; k++)
				{
					_int64 cx = (x[i]+x[j]+x[k]);
					_int64 cy = (y[i]+y[j]+y[k]);
					if (cx%3==0 && cy%3==0)
					{
						count++;
					}
				}
		printf("Case #%d: %d\n", now ,count);
		now++;
	}
	return 0;
}