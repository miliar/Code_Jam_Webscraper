#include <stdio.h>
#include <algorithm>
#include <assert.h>
using namespace std;
#define N 10000
int table[N];
bool used[N];
int mygate[N];
bool leaf[N];
int can[N];
bool value[N];
bool eval(int v)
{
	if(leaf[v])return value[v]=(mygate[v]==1);
	int ll=(v<<1)+1;
	int rr=ll+1;
	eval(ll);
	eval(rr);
	if(mygate[v]==1)return (value[v]=(value[ll]&&value[rr]));
	else return (value[v]=(value[ll]||value[rr]));
}
int DP(int v)
{
	if(leaf[v])return 10*N;
	if(used[v])return table[v];
	used[v]=true;
	int ll=(v<<1)+1;
	int rr=ll+1;
	int re=10*N;
	if(mygate[v])
	{
		assert((value[ll]&&value[rr])==value[v]);
		if(value[v])
		{
			re=min(re,DP(ll));
			re=min(re,DP(rr));
		}
		else
		{
			int t=0;
			if(!value[ll])t+=DP(ll);
			if(!value[rr])t+=DP(rr);
			re=min(re,t);
		}
	}
	else
	{
		assert((value[ll]||value[rr])==value[v]);
		if(value[v])
		{
			int t=0;
			if(value[ll])t+=DP(ll);
			if(value[rr])t+=DP(rr);
			re=min(re,t);
		}
		else
		{
			re=min(re,DP(ll));
			re=min(re,DP(rr));
		}
	}
	if(can[v])
	{
		mygate[v]^=1;
		if(mygate[v])
		{
			if(value[v]!=(value[ll]&&value[rr]))
				re=min(re,1);
			else
			{
				if(value[v])
				{
					re=min(re,DP(ll)+1);
					re=min(re,DP(rr)+1);
				}
				else
				{
					int t=1;
					if(!value[ll])t+=DP(ll);
					if(!value[rr])t+=DP(rr);
					re=min(re,t);
				}
			}
		}
		else
		{
			if(value[v]!=(value[ll]||value[rr]))
				re=min(re,1);
			else
			{
				if(value[v])
				{
					int t=1;
					if(value[ll])t+=DP(ll);
					if(value[rr])t+=DP(rr);
					re=min(re,t);
				}
				else
				{
					re=min(re,DP(ll)+1);
					re=min(re,DP(rr)+1);
				}
			}
		}
	}
	table[v]=re;
	return re;
}
int main()
{
	int t,n,v,ca=1;
	for(scanf("%d",&t);t--;)
	{
		scanf("%d %d",&n,&v);
		assert(n<=N);
		assert(n&1);
		memset(used,false,sizeof(bool)*n);
		for(int i=0;i<n;i++)
		{
			leaf[i]=!(i<(n-1)/2);
			if(leaf[i])scanf("%d",mygate+i);
			else scanf("%d %d",mygate+i,can+i);
		}
		int ans;
		bool f=eval(0);
		if(f==(v==1))ans=0;
		else ans=DP(0);
		printf("Case #%d: ",ca++);
		if(ans>n)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
