#include <iostream>
#include <vector>
using namespace std;
typedef __int64 llong;
#define maxn 1020

int r,n,k;
llong ans=0;
vector<int> gp;
int cnt[maxn];
llong w[maxn];
llong len;
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int cas,casid=0;
	scanf("%d",&cas);
	while(cas--)
	{
		ans=0;
		scanf("%d%d%d",&r,&k,&n);
		gp.resize(n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&gp[i]);
		}
		int pre=0,mod;
		len=0;
		memset(cnt,-1,sizeof(cnt));
		memset(w,0,sizeof(0));
		for(int i=0;i<n+1;i++)
		{
			int tmp=0,j=pre;
			for(int t=0;t<n;t++)
			{
				if(j>=n)j=0;
				tmp+=gp[j];
				if(tmp>k)
					break;
				j=(j+1)%n;
			}
			if(tmp>k)
			{
				if(i)w[i]=w[i-1]+tmp-gp[j];
				else w[i]=tmp-gp[j];
			}
			else 
			{
				if(i)w[i]=w[i-1]+tmp;
				else w[i]=tmp;
			}
			if(cnt[pre]!=-1)
			{
				mod=i-cnt[pre];
				len=w[i]-w[cnt[pre]];
				break;
			}
			cnt[pre]=i;
			pre=j;
		}
		int pp=0;
		for(int i=0;i<min(cnt[pre],r);i++)
		{
			int tmp=0,j=pp;
			for(int t=0;t<n;t++)
			{
				tmp+=gp[j];
				if(tmp>k)break;
				j=(j+1)%n;
			}
			pp=j;
			if(tmp>k)tmp-=gp[j];
			ans+=tmp;
		}
		r-=(cnt[pre]);
		if(r>0)
		{
			int tmp=r/mod;
			ans+=tmp*len;
			pp=cnt[pre];
			for(int i=0;i<r%mod;i++)
			{
				int tmp=0,j=pp;
				for(int t=0;t<n;t++)
				{
					tmp+=gp[j];	
					if(tmp>k)break;
					j=(j+1)%n;
				}
				pp=j;
				if(tmp>k)tmp-=gp[j];
				ans+=tmp;
			}
		}
		printf("Case #%d: %I64d\n",++casid,ans);
	}
}