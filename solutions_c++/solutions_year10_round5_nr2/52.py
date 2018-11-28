#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))
#define pi 3.141592653589
#define VI vector <int>

#define maxN 100005
#define maxn 105

struct node
{
	int d;
	long long sum;
}dist[maxN];
int Link[maxN],heap[maxN],hz;
int a[maxn],n;

inline node operator +(const node &a,const int &b)
{
	node c;
	c.d=a.d+b;
	c.sum=a.sum+1;
	return c;
}

inline bool operator <(const node &a,const node &b)
{
	return a.sum-a.d<b.sum-b.d || a.sum-a.d==b.sum-b.d && a.d<b.d;
}

inline void up(int x)
{
	for (int y=x/2;y;y=x/2)
	{
		if (dist[heap[x]]<dist[heap[y]])
		{
			swap(heap[x],heap[y]);
			swap(Link[heap[x]],Link[heap[y]]);
		}else break;
		x=y;
	}
}

inline void sink(int x)
{
	for (int y=x*2;y<=hz;y=x*2)
	{
		if (y<hz && dist[heap[y+1]]<dist[heap[y]]) ++y;
		if (dist[heap[y]]<dist[heap[x]])
		{
			swap(heap[x],heap[y]);
			swap(Link[heap[x]],Link[heap[y]]);
		}else break;
		x=y;
	}
}

int main()
{
	freopen("B_large.in","r",stdin);
	freopen("B_large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		long long L;
		int n;
		scanf("%I64d %d",&L,&n);
		int N=0;
		for (int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			N=max(N,a[i]);
		}
		int yu=L%N;
		long long Limit=(L-yu)/N;
		
		for (int i=0;i<N;++i)
		{
			dist[i].d=-1;
			Link[i]=-1;
		}
		
		dist[0].d=0;
		dist[0].sum=0;
		Link[0]=1;
		heap[hz=1]=0;
		while (hz)
		{
			int u=heap[1];
			heap[1]=heap[hz--];
			Link[u]=-1;
			if (hz)
			{
				sink(1);
				Link[heap[1]]=1;
			}
			if (dist[u].d<Limit)
			for (int i=0;i<n;++i)
			{
				int delta=0,v=a[i]+u;
				if (v>=N) v-=N,delta=1;
				
				if (dist[v].d==-1 || dist[u]+delta<dist[v])
				{
					dist[v]=dist[u]+delta;
					if (Link[v]==-1)
					{
						heap[++hz]=v;
						Link[v]=hz;
					}
					up(Link[v]);
				}
			}
		}
		
		
		printf("Case #%d: ",test);
		if (dist[yu].d!=-1)
		{
			printf("%I64d\n",dist[yu].sum+(L-yu-(long long)dist[yu].d*N)/N);
		}else puts("IMPOSSIBLE");
	}
	
	return 0;
}
