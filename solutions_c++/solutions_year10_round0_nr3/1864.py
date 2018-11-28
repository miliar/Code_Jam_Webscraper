#include<stdio.h>

int r,k,n,g[2001],go[1001],cost[1001];

void process()
{
	int i,t=0;
	__int64 sum=0;
	for(i=n;i<n+n;i++) g[i]=g[i-n];
	for(i=0;i<n;i++)
	{
		while(t-i<n)
		{
			sum+=g[t];
			if(sum>k)
			{
				sum-=g[t];
				break;
			}
			t++;
		}
		go[i]=t%n;
		cost[i]=sum;
		sum-=g[i];
	}
	int x=0;
	sum=0;
	for(i=0;i<r;i++)
	{
		sum+=__int64(cost[x]);
		x=go[x];
	}
	printf("%I64d\n",sum);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,t;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(j=0;j<n;j++)
		{
			scanf("%d",&g[j]);
		}
		printf("Case #%d: ",i+1);
		process();
	}
	return 0;
}