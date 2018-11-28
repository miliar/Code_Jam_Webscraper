#include <stdio.h>
#include <string.h>

int u[2000];
int start[2000];
int cost[2000];
int a[2000];

__int64 ans,cycle;

int T,t,i,j,r,k,n,s,p,pp;

int main()
{
	freopen("c.in","r",stdin);	freopen("c.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		memset(u,-1,sizeof(u));
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		s=0;
		for(i=0;i<2000;i++)
		{
			if(u[s]!=-1)
				break;
			u[s]=i;
			start[i]=s;
			cost[i]=0;
			for(j=s;j<s+n;j++)
			{
				cost[i]+=a[j%n];
				if(cost[i]>k)
				{
					cost[i]-=a[j%n];
					break;
				}
			}
			s=j%n;
		}
		p=i-u[s];
		pp=u[s];
		ans=cycle=0;
		for(i=0;i<pp && i<r;i++)
			ans+=cost[i];
		if(r>pp)
		{
			r-=pp;
			for(i=pp;i<pp+p;i++)
				cycle+=cost[i];
			ans+=cycle*(r/p);
			if(r%p)
				for(i=pp;i<r%p+pp;i++)
					ans+=cost[i];
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}