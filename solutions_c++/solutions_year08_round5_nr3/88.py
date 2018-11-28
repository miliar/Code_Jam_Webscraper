//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}
class Graph {
private:
	struct edge {
		int to, cap, back;
	};
	vector<vector<edge> > adj;
	int n;
public:
	Graph(int n) : n(n) {
		adj.resize(n);
		for (int i=0; i<n; i++)
			adj[i].clear();
	}
	~Graph() {
		for (int i=0; i<n; i++)
			adj[i].clear();
		adj.clear();
	}
	void Insert(int i, int j, int c) {
		adj[i].push_back((edge){j, c, adj[j].size()});
		adj[j].push_back((edge){i, 0, adj[i].size()-1});
	}
	int Dinic(int s, int t) {
		int q[n], prev[n];
		int allflow=0;
		while (true) {
			memset(prev, -1, sizeof(prev));
			int qf=0, qb=0;
			prev[q[qb++]=s] = -2;
			while (qb>qf && prev[t]==-1)
				for (int u=q[qf++], i=0, v; i<adj[u].size(); i++)
					if (prev[v=adj[u][i].to]==-1 && adj[u][i].cap>0)
						prev[q[qb++]=v] = adj[u][i].back;
			if (prev[t] == -1)
				break;
			for (int i=0, z; i<adj[t].size(); i++)
				if(adj[z=adj[t][i].to][adj[t][i].back].cap>0 && prev[z]!=-1) {
					int flow = adj[z][adj[t][i].back].cap;
					for (int v=z, u=prev[v]; u>=0; v=adj[v][u].to, u=prev[v])
						flow <?= adj[adj[v][u].to][adj[v][u].back].cap;
					if (!flow)
						continue;
					adj[z][adj[t][i].back].cap -= flow;
					adj[t][i].cap += flow;
					for (int v=z, u=prev[v]; u>=0; v=adj[v][u].to, u=prev[v]) {
						adj[adj[v][u].to][adj[v][u].back].cap -= flow;
						adj[v][u].cap += flow;
					}
					allflow += flow;
				}
		}
		return allflow;
	}
};
char buf[99][99];
int main(){
	int tests;
	scanf("%d",&tests);
	for(int T=1;T<=tests;T++){
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%s",buf[i]);
		Graph flow(n*m+2);
		int s=n*m,t=n*m+1,cnt=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				if(buf[i][j]!='.')
					continue;
				cnt++;
				if(j&1)
					flow.Insert(s,i*m+j,1);
				else
					flow.Insert(i*m+j,t,1);
			}
		for(int j=1;j<m;j++)
			for(int i=0;i<n;i++)
				for(int k=-1;k<=1;k++){
					if(i+k<0||i+k>=n)
						continue;
					if(j&1)
						flow.Insert(i*m+j,(i+k)*m+j-1,1);
					else
						flow.Insert((i+k)*m+j-1,i*m+j,1);
				}
		printf("Case #%d: %d\n",T,cnt-flow.Dinic(s,t));
	}
scanf("%*s");
	return 0;
}
