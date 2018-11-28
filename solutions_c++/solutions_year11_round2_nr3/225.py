#include <stdio.h>
#include <memory.h>
#include <vector>
#define debug(x) 
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
int Adj[10][10];
int N,M;
int U[10],V[10],C[10];

VVI Groups;


void pick(int x,int y)
{
	debug(printf("trying %d %d\n",x,y));
	VI tmp; 
	int u=x,v=y; 
	tmp.push_back(u); 
	while (v!=x)
	{
		Adj[u][v] = 0; tmp.push_back(v);
		for (int k=1;k<N;++k) if (Adj[v][(u+N-k)%N])
		{
			int w = (u+N-k)%N;
			u = v;
			v = w;
			break;
		}
	}
	Adj[u][v]=0;
	debug(printf("G:");for (int q=0;q<tmp.size();++q) printf("%d ",tmp[q]); printf("\n");)
	Groups.push_back(tmp);
}

int findAny(int u,int k)
{
	if (u>=N)
	{
		int ret = 1;
		for (int q=0;q<Groups.size();++q) 
		{
			int fill = 0;
			for (int w=0;w<Groups[q].size();++w) fill |= 1<<C[Groups[q][w]];
			if (fill!=(1<<k)-1) { ret=0; break; }
		}
		if (ret)
		{
			printf("%d\n",k);
			for (int q=0;q<N;++q) printf("%d ",C[q]+1);printf("\n");
		}
		return ret;
	}
	for (int i=0;i<k;++i)
	{
		C[u] = i;
		if (findAny(u+1,k)) return 1;
	}
	return 0;
}
int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		scanf("%d %d",&N,&M);
		for (int q=0;q<M;++q) scanf("%d",U+q);
		for (int q=0;q<M;++q) scanf("%d",V+q);
		memset(Adj,0,sizeof(Adj));
		for (int q=0;q<N;++q) Adj[q][(q+N-1)%N] = Adj[q][(q+1)%N] = 1;
		for (int q=0;q<M;++q) Adj[--U[q]][--V[q]]=Adj[V[q]][U[q]]=1;
		
		Groups.clear();
		for (int q=0;q<N;++q) 
			if (Adj[q][(q+1)%N]) pick(q,(q+1)%N);
		for (int q=0;q<M;++q)
		{
			if (Adj[U[q]][V[q]]) pick(U[q],V[q]);
			if (Adj[V[q]][U[q]]) pick(V[q],U[q]);
		}
		
		printf("Case #%d: ",kase);
		for (int k=N;k>=1;--k)
		{
			if (findAny(0,k)) break;
		}
	}
	return 0;
}
