#include <stdio.h>
#include <queue>
#include <vector>
#include <memory.h>
#include <sstream>
#include <string>
using namespace std;
const int _NMAX = 500;
int N,M;
int DistFrom0[_NMAX];
int Adj[_NMAX][_NMAX];
int Dp[_NMAX][_NMAX];
int Vs[_NMAX][_NMAX];

int Near3[_NMAX][_NMAX][_NMAX];
vector<int> FR[_NMAX];
//i loop = 0;

int CountNear(int a)
{
	return FR[a].size();
}

int CountNear(int a,int b,int c)
{
	if (Near3[a][b][c]>=0) return Near3[a][b][c];
	int ret = 0;
	/*
	for (int q=0;q<N;++q)
	{
		if (q==a || q==b || q==c) continue;
		if (!Adj[a][q] && !Adj[b][q] && Adj[c][q]) ret++;
	}*/
	for (int q=0;q<FR[c].size();++q)
	{
		int d = FR[c][q];
		if (d!=a && d!=b && !Adj[a][d] && !Adj[b][d]) ret++;
	}
	return Near3[a][b][c] = ret;
}



int solve(int u,int v)
{
	if (DistFrom0[v]>=DistFrom0[1]) return -987654321;
	if (Adj[v][1]) return 0;

	if (Vs[u][v]) return Dp[u][v];
	else Vs[u][v] = 1;

	int &ret = Dp[u][v];
	ret = -987654321;
	for (int t=0;t<N;++t)
	{
		if (Adj[v][t] && DistFrom0[t] == DistFrom0[v]+1)
		{
			int tmp = 0;
			tmp += CountNear(u,v,t);
			tmp += solve(v,t);
			tmp --;
			//printf("%d->%d->%d / %d + %d -1 = %d\n", u,v,t,CountNear(u,v,t),solve(v,t),tmp);
			if (tmp>ret) ret = tmp;
		}
	}

	return ret;
}

int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		fprintf(stderr,"Doing %d\n",kase);
		memset(Adj,0,sizeof(Adj));
		memset(DistFrom0,0,sizeof(DistFrom0));
		memset(Vs,0,sizeof(Vs));
		scanf("%d %d",&N,&M);	
		for (int q=0;q<N;++q) FR[q].clear();
		for (int q=0;q<M;++q)
		{
			char str[256];
			scanf("%s",str);
			int u,v;
			sscanf(str,"%d,%d",&u,&v);
			if (u>=N || v>=N) fprintf(stderr,"fuck!\n");
			Adj[u][v]=Adj[v][u]=1;
			FR[u].push_back(v);
			FR[v].push_back(u);
		}
		//set DistFrom 0
		for (int q=0;q<N;++q) DistFrom0[q] = -1;
		DistFrom0[0] = 0;
		queue<int> Q;
		Q.push(0);
		while (!Q.empty())
		{
			int u = Q.front(); Q.pop();
			for (int v=0;v<N;++v) if (Adj[u][v] && DistFrom0[v]<0)
			{
				DistFrom0[v] = DistFrom0[u] + 1;
				Q.push(v);
			}
		}
		for (int q=0;q<=N;++q) for (int w=0;w<=N;++w) for (int e=0;e<=N;++e)
			Near3[q][w][e]=-1;
		//if already near
		//loop=0;
		int ret = CountNear(0) + solve(N,0);
		printf("Case #%d: %d %d\n",kase,DistFrom0[1]-1,ret);
		//fprintf(stderr,"LoopCount : %d With N = %d , M =%d\n",loop,N,M);
	}
	return 0;
}
