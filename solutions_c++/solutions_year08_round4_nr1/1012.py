#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<map>
#include<vector>
#include<string>
using namespace std;	

#define sq(a) ((a)*(a))
#define pb(a) push_back(a)
#define Min(a,b) (((a)<(b))?(a):(b))
#define Max(a,b) (((a)>(b))?(a):(b))
#define eps 1e-9
#define inf 1<<29
#define pye 2.*acos(0.)
#define SZ(v) ((int)(v).size())
#define For(i,a,b) for(i=(a);i<(b);++i)
#define Fore(i,a,b) for(i=(a);i<=(b);++i)
#define Forc(i,v) For(i,0,SZ(v))
#define Foro(i,a) For(i,0,a)

vector<int> adj[35];
int gate[35],chan[35],logic[35],n,m,v,chang[35],temp[35];

int visit(int root)
{
	if(!SZ(adj[root]))
		return logic[root];
	if(temp[root])
		return visit(adj[root][0]) & visit(adj[root][1]);
	else
		return visit(adj[root][0]) | visit(adj[root][1]);
}

int calc(int state)
{
	int i,j;
	for(i=0;i<(m-1)/2;i++)
		temp[i]=gate[i];
	j=0;
	for(i=0;i<n;i++)
		if(state & (1<<i))
		{
			j++;
			temp[chang[i]]=!temp[chang[i]];
		}
	i=visit(0);
	if(i==v)
		return j;
	else
		return inf;
}

int main()
{
	int t,cs,k,i,j,mn;
	freopen("a.txt","w",stdout);
	scanf("%d",&t);
	Foro(cs,t)
	{
		scanf("%d%d",&m,&v);
		Foro(i,m)
			adj[i].clear();
		k=1;
		n=0;
		Foro(i,(m-1)/2)
		{
			scanf("%d%d",&gate[i],&chan[i]);
			if(chan[i]==1)
				chang[n]=i,n++;
			adj[i].pb(k),adj[i].pb(k+1);
			k+=2;
		}
		For(i,(m-1)/2,m)
			scanf("%d",&logic[i]);
		mn=inf;
		for(i=0;i<(1<<n);i++)
			j=calc(i),mn=Min(mn,j);
		if(mn==inf)
			printf("Case #%d: IMPOSSIBLE\n",cs+1);
		else
			printf("Case #%d: %d\n",cs+1,mn);
	}
	return 0;
}

