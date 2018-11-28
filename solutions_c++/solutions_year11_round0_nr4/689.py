#include <stdio.h>

int main()
{
	int s[1002];
	int used[1002];
	double a[1002];
	double tmp,total;
	int i,j,n,cas,asd,count;
	a[0] = 0;
	a[1] = 0;
	for(i=2;i<=1000;i++)
	{
		tmp = 0;
		for(j=1;j<i;j++)
		{
			tmp += (a[j] + a[i-j]);
		}
		tmp = tmp / (double) (i-1);
		tmp += 1;
		a[i] = tmp;
	}
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d",&n);
		total = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&s[i]);
			used[i] = 0;
		}
		for(i=0;i<n;i++)
		{
			if(!used[i])
			{
				j = i;
				count = 0;
				do
				{
					used[j] = 1;
					j = s[j] - 1;
					count ++;
				}while(used[j] == 0);
				if(count!=1)
					total += a[count]+1;
			}
		}
		printf("Case #%d: ",asd+1);
		printf("%.6lf\n",total);
	}
	return 0;
}