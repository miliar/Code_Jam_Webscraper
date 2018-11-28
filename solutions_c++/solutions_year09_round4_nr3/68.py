#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

template<class CapType> class FlowNetwork_s{
	public:
		int N,M;
	    vector<VI> adj;
	    vector<vector<CapType> > cap;
	    void init(int _N) { N=_N; M=0; adj.clear(); cap.clear(); adj.resize(N); cap.resize(N); Repi(N) cap[i].resize(N); }
	    void add(int u,int v,CapType _cap=1)
	     {
			if (!cap[u][v] && !cap[v][u]) { adj[u].PB(v); adj[v].PB(u); }
			cap[u][v]+=_cap; M++;
	//		cout<<"              "<<u<<" -> "<<v<<"\n";
	     }
      };

template<class CapType> CapType MaxFlow(FlowNetwork_s<CapType> &G,int source,int sink,bool residual=0)
{
	VI dist(G.N),path(G.N),prev(G.N),q(G.N),next(G.N);
	vector<bool> used(G.N);
	vector<vector<CapType> > res=G.cap;
	int u,v,pc;
	CapType mincap,Flow=0;

	q[0]=sink; used[sink]=1; dist[sink]=0;
	for (int s=0,e=1;s<e;s++)
	 {
			u=q[s];
			Repi(G.adj[u].SZ)
			 {
					v=G.adj[u][i];
					if (G.cap[v][u]>0 && !used[v])
					 {
							dist[v]=dist[u]+1;
							used[v]=1;
							q[e++]=v;
					 }
			 }
	 }

	u=source; prev[source]=-1;
	while (dist[source]<G.N)
	 {
			for(;next[u]<G.adj[u].SZ;next[u]++)
			 { v=G.adj[u][next[u]];
			   if (res[u][v]>0 && dist[u]==dist[v]+1) break;
			 }
			if (next[u]==G.adj[u].SZ)
			 {
			   dist[u]=INF;
			   Repi(G.adj[u].SZ)
			    if (res[u][G.adj[u][i]]>0)
			     dist[u]=min(dist[u],dist[G.adj[u][i]]+1);
			   next[u]=0;
			   if (u!=source) u=prev[u];
			   continue;
			 }
			prev[v]=u;
			u=v;
			if (u==sink)
			 {
			   pc=0;
			   while (u!=-1) { path[pc++]=u; u=prev[u]; }
			   reverse(path.begin(),path.begin()+pc);
			   mincap=res[path[0]][path[1]];
			   for (int i=1;i<pc-1;i++)
			    mincap=min(mincap,res[path[i]][path[i+1]]);
			   Flow+=mincap;
			   Repi(pc-1)
			    {
					res[path[i]][path[i+1]]-=mincap;
					res[path[i+1]][path[i]]+=mincap;
				}
			   u=source;
			 }
	 }
	if (residual) G.cap=res;
	return Flow;
}




int N,K;

int p[128][27];

int T;
int main()
{
    
    scanf("%d",&T);
    F(xx,T)
     {
            scanf("%d%d",&N,&K);
            Repi(N)
             Repj(K)
              scanf("%d",&p[i][j]);
            //cout<<"\n\n\n";

            FlowNetwork_s<int> F;
            F.init(2*N+4);
            Repi(N)
             F.add(0,i+1) , F.add(i+N+1,2*N+2);
            Repi(N)
             {
               Repj(N)
                {
                    bool yes=1;
                    Repk(K)
                      if (p[i][k] <= p[j][k] ) { yes=0; break; }
                   if (yes)
                    F.add(i+1,j+N+1);
                }
             }
             
            printf("Case #%d: %d\n",xx+1,N-MaxFlow<int>(F,0,2*N+2));
        }
    
    return 0;
}
