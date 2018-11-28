#include<stdio.h>

int main(void)
{
	int t;
	int count=0;
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	while(scanf("%d",&t)==1)
	{
		while(t--)
		{
			int m,n,k;
			scanf("%d%d",&n,&k);
			count++;
			m=(1<<n);
			k%=m;
			if(k+1==m)
			{
				printf("Case #%d: ON\n",count);
			}
			else
			{
				printf("Case #%d: OFF\n",count);
			}
		}
	}
	return 0;
}