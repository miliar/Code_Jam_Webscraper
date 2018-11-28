#include<stdio.h>

int t, test;
int x, m, n, i;
int v, sum;
int main()
{
	freopen("D:\\C-large.in", "r", stdin);
	freopen("D:\\C-large.out", "w", stdout);
	scanf("%d", &t);
	for(test = 1; test<=t; test++)
	{
		m = 1000000000;
		scanf("%d", &n);
		v=0;
		sum=0;
		for(i=0; i<n; i++)
		{
			scanf("%d", &x);
			v^=x;
			sum+=x;
			if (x<m)
			{
				m = x;
			}
		}
		if (test>1)
		{
			printf("\n");
		}
		if (v!=0)
		{
			printf("Case #%d: NO", test);
		}
		else
		{
			printf("Case #%d: %d", test, sum-m);
		}
	}
	return 0;
}