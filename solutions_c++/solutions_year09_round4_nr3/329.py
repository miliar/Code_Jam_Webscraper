#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define ALL(a) a.begin(),a.end()
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long

const int MAXN=105,MAXK=30;
int T,N,K;

int mem[MAXN][MAXK];
int adj[MAXN<<1][MAXN<<1];

inline bool edge(int x,int y) {
	for(int j=0;j<K;j++) {
		if (mem[x][j]>=mem[y][j]) {return false;}
	}
	return true;
}

int parent[MAXN<<1];
bool vis[MAXN<<1];

inline int flow() {
	int ret=0;
	while (1) {
		CLEAR(vis);
		memset(parent,-1,sizeof(parent));
		queue<int> q;
		q.push(0);
		vis[0]=true;
		while (!q.empty()) {
			int t=q.front();
			q.pop();
			for(int i=0;i<=2*N+1;i++) {
				if (adj[t][i]>0 && !vis[i]) {
					vis[i]=true;
					parent[i]=t;
					q.push(i);
				}
			}
		}
		if (!vis[2*N+1]) {break;}
		int v=2*N+1,f=999999;
		while (parent[v]!=-1) {
			f=min(f,adj[parent[v]][v]);
			v=parent[v];
		}
		v=2*N+1;
		while (parent[v]!=-1) {
			adj[parent[v]][v]-=f;
			adj[v][parent[v]]+=f;
			v=parent[v];
		}
		ret+=f;
	}
	return ret;
}

int main() {
	scanf("%d",&T);
	for(int h=1;h<=T;h++) {
		scanf("%d %d",&N,&K);
		for(int i=1;i<=N;i++) {
			for(int j=0;j<K;j++) {
				scanf("%d ",&mem[i][j]);
			}
		}
		memset(adj,0,sizeof(adj));
		for(int i=1;i<=N;i++) {
			adj[0][i]=1;
			for(int j=1;j<=N;j++) {
				if (edge(i,j)) {
					adj[i][N+j]=1;
				}
			}
			adj[i+N][2*N+1]=1;
		}
		printf("Case #%d: %d\n",h,N-flow());
	}	
	
	return 0;
}








