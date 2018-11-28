#include<stdio.h>
int g[1001];
int time[1001];
long long money[1001];
int to[1001];
long long add[1001];
int main()
{
	freopen("c-large.in","r",stdin);
	freopen("c-large.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		int r,k,n;
		scanf("%d %d %d",&r,&k,&n);
		for(int i=0;i<n;i++) scanf("%d",&g[i]);
		
		int j=0;
		int sum=0;
		for(int i=0;i<n;i++)
		{
			while(sum+g[j]<=k)
			{
				sum+=g[j];
				j=(j+1)%n;
				if(j==i) break;
			}
			to[i]=j;
			add[i]=sum;
			sum-=g[i];
		}
		
		for(int i=0;i<n;i++)
		{
			time[i]=-1;
			money[i]=-1;
		}
		time[0]=0;
		money[0]=0;
		
		long long ans=0;
		int now=0;
		int cnt=0;
		bool on=0;
		while(r>0)
		{
			int next=to[now];
			r--;
			ans+=add[now];
			if(on==0 && time[to[now]]!=-1)
			{
				on=1;
				int T=(time[now]+1-time[to[now]]);
				ans+=(r/T)*(ans-money[to[now]]);
				r%=T;
			}
			time[to[now]]=time[now]+1;
			money[to[now]]=ans;
			now=to[now];
		}
		
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}
