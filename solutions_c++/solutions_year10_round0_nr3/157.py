#include <iostream>

using namespace std;

#define LL __int64

#define N 1010

int next[N],cost[N],g[N];
bool vst[N];
int cir_bg,cir_ct;
LL cir_tl;
int R,K,n;

void init()
{
	int i,j;
	for(i=0;i<n;i++)
	{
		int sm=0;
		for(j=i;;j=(j+1)%n)
		{
			if(sm+g[j]>K) break;
			if(j==i&&sm) break;
			sm+=g[j];
		}
		next[i]=j;
		cost[i]=sm;
	}
	memset(vst,0,sizeof(vst));
	i=0;
	while(1)
	{
		vst[i]=true;
		if(vst[next[i]])
		{
			cir_bg=next[i];
			cir_ct=1;
			i=next[cir_bg];
			cir_tl=cost[cir_bg];
			while(i!=cir_bg)
			{
				cir_ct++;
				cir_tl+=cost[i];
				i=next[i];
			}
			break;
		}
		else
		{
			i=next[i];
		}
	}
}

LL solve()
{
	LL sm=0;
	int i=0;
	while(R&&i!=cir_bg)
	{
		sm+=cost[i];
		i=next[i];
		R--;
	}
	if(R)
	{
		sm+=(LL)cir_tl*(R/cir_ct);
		R=R%cir_ct;
	}
	while(R)
	{
		sm+=cost[i];
		i=next[i];
		R--;
	}
	return sm;
}

int main()
{
	int t;
//	freopen("C-large.in.txt","r",stdin);
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		scanf("%d%d%d",&R,&K,&n);
		int i;
		for(i=0;i<n;i++) scanf("%d",g+i);
		init();
		LL ret=solve();
		printf("Case #%d: %I64d\n",cse,ret);
	}
	return 0;
}
