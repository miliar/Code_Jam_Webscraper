#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<functional>
#include<utility>
using namespace std;

const int MaxN = 100;
const int MaxK = 25;
const int GraphMax = 2*MaxN + 2;
const int NoPre = 0x80808080;
inline int min(int a,int b){return a<b?a:b;}
struct Edge
{
	int v,c,f;Edge *next,*back;
	Edge(int v,int c,int f,Edge* p):v(v),c(c),f(f),next(p){}
};
struct List
{
	int v;List* next;
	List(int v,List* p):v(v),next(p){}
};
Edge* Graph[GraphMax];
void AddEdge(int a,int b,int c)
{
	Graph[a] = new Edge(b,c,0,Graph[a]);
	Graph[b] = new Edge(a,0,0,Graph[b]);
	Graph[a]->back = Graph[b];
	Graph[b]->back = Graph[a];
}
void DeleteEdge(Edge* e)
{
	if(e == NULL) return;
	else
	{
		DeleteEdge(e->next);
		delete(e);
	}
}
int MaxFlow(int s,int t);
int price[MaxN][MaxK];
int n;
int main()
{
	int cases;
	cin>>cases;
	for(int _=1;_<=cases;_++)
	{
		int k;
		cin>>n>>k;
		for(int i=0;i<n;i++)
			for(int j=0;j<k;j++)
				cin>>price[i][j];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				bool gt = true;
				for(int x=0;x<k && gt;x++)
					if(price[i][x] <= price[j][x])
						gt = false;
				if(gt)
				{
					//directed graph: add graph[i][j]
					//so add edges in the bipartite graph
					AddEdge(1+i,1+n+j,1);
				}
			}
		for(int i=0;i<n;i++)
		{
			AddEdge(0,1+i,1);
			AddEdge(1+n+i,1+n+n,1);
		}
		int t = n;
		n = 2*n+2;
		cout<<"Case #"<<_<<": "<<(t-MaxFlow(0,n-1))<<endl;
		for(int i=0;i<n;i++)
		{
			DeleteEdge(Graph[i]);
			Graph[i] = NULL;
		}
	}
	return 0;
}
int MaxFlow(int s,int t)
{
	Edge *x,*y;
	Edge *cur[GraphMax],*path[GraphMax];
	int i,j,k,result=0;
	int pathlen,d[GraphMax];
	for(;;)
	{
		//BFS
		int q[GraphMax],start,end;
		start = end = 0;
		q[end++] = s;
		memset(d,-1,sizeof(d));
		d[s] = 0;
		while(start < end)
		{
			i = q[start++];
			for(x=Graph[i];x;x=x->next)
				if(x->f < x->c && d[j=x->v] < 0)
				{
					d[j] = d[i]+1;
					q[end++] = j;
					if(j == t) goto bfsend;//BFS complete
				}
		}
bfsend:
		if(d[t] < 0) break;
		//DFS
		pathlen = 0;
		memcpy(cur,Graph,sizeof(cur));
		for(;pathlen>=0;)
		{
			i = pathlen==0 ? s : path[pathlen-1]->v;
			if(i == t)//augment
			{
				int minj = 0;
				for(j=0,k=0x7fffffff;j<pathlen;j++)
					if(path[j]->c - path[j]->f < k)
					{
						k = path[j]->c - path[j]->f;
						minj = j;
					}
				result += k;
				for(j=0;j<pathlen;j++)
				{
					path[j]->f += k;
					path[j]->back->f -= k;
				}
				pathlen = minj;
				continue;
			}
			for(x=cur[i];x;x=x->next)
				if(x->f < x->c && d[x->v] == d[i]+1)
					break;
			cur[i] = x;
			if(x)
			{
				path[pathlen++] = x;
				//cur[i] = cur[i]->next;//mundai aru
			}
			else
				d[i] = -1, pathlen--;
		}
	}
	return result; 
}

