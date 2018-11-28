#include<stdio.h>
#include<string.h>
long long dist[1000002],bacha[1000002];
int main()
{
	int T, L,n,c,x;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		long long timeInit, saved=0, sum=0;
		scanf("%d%Ld%d%d\n",&L,&timeInit,&n,&c);
		for(x=0;x<c;x++)
		{
			scanf("%Ld",&dist[x]);
			long long ls=sum;
			sum+=dist[x]*2;
			if(sum<=timeInit)bacha[x]=0;
			else if(ls<timeInit)bacha[x]=(sum-timeInit)>>1;
			else
			{
				bacha[x]=dist[x];
			}
		}
		for(x=c;x<n;x++)
		{
			dist[x]=dist[x-c];
			long long ls=sum;
			sum+=dist[x]*2;
			if(sum<=timeInit)bacha[x]=0;
			else if(ls<timeInit)bacha[x]=(sum-timeInit)>>1;
			else
			{
				bacha[x]=dist[x];
			}
		}
		int cntt[10005];
		memset(cntt,0,sizeof(cntt));
		for(x=0;x<n;x++)
			cntt[bacha[x]]++;
		for(x=10004;x;x--)
		{
			if(L==0)break;
			if(cntt[x]<=L)
			{
				L-=cntt[x];
				saved+=cntt[x]*x;
			}
			else
			{
				saved+=L*x;
				L=0;
			}
		}
		printf("Case #%d: %Ld\n",t,sum-saved);
	}
	return 0;
}
