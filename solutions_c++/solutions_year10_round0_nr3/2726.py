#include<stdio.h>
#include<string.h>

long long r,k,n,to,g[1001],gt[500500];
int v[1001][1001];

int main()
{
	int i,j,p,q,t;
	long long ans=0;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	
	scanf("%d", &t);
	for(i=0; i<t; i++)
	{
		scanf("%lld%lld%lld", &r,&k,&n);
		memset(v,0,sizeof(v));
		int gtc=0,start,end,first=1;
		ans=0;
		for(j=0; j<n; j++)
		{
			long long tmp=0;
			scanf("%lld", &tmp);
			if(tmp>k)
				j--,n--;
			else
				g[j]=tmp;
		}
		p=0;
		for(j=0; ; j=(j+1)%n)
		{
			long long gn=0;
			q=0;
			for(p=j; gn+g[p]<=k && q<n; p=(p+1)%n)
			{
				q++;
				gn+=g[p];
			}
			if(v[j][q]==1 && first)
				start=gtc,first=0;
			if(v[j][q]==2)
			{
				end=gtc;
				break;
			}
			gt[gtc++]=gn;
			v[j][q]++;
			j=p-1;
		}
		int temp=end-start;
		start-=temp;
		end-=temp;
		if(r<end+temp)
			for(j=0; j<r; j++)
				ans+=gt[j];
		else
		{
			for(j=0; j<end; j++)
				ans+=gt[j];
			r-=end;
			int div=r/temp;
			int mod=r%temp;
			long long t1=0,t2=0;
			for(j=start; j<end; j++)
				t1+=gt[j];
			for(j=start; j<start+mod; j++)
				t2+=gt[j];
			ans+=t1*div+t2;
		}
		printf("Case #%d: %lld\n", i+1,ans);
	}
}