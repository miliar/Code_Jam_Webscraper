#include<iostream>
using namespace std;

const int MaxN = 500;
const int MaxE = 2000000;
const int INF = 100000000;
struct edge {
	int u, v, nxt, cap;
	inline edge(int u=0, int v=0,int nxt=-1, int cap=0)
		:u(u),v(v),nxt(nxt),cap(cap){};
}e[MaxE];
int head[MaxN], tot;


int que[MaxN], n, lis[MaxN], sz;
int blockn, block[MaxN], size[MaxN], score[MaxN];
int vst[MaxN], mark[MaxN];
int rep[MaxN][2];

int dist[MaxN], cur[MaxN];

struct Graph {
	int st, en, N;
	inline int clear(int S, int T, int _) {
		memset(head, -1, sizeof(head));
		tot = 0;
		st = S; en = T; N = _;
	}
	inline int insert(int u, int v, int cap) {
		e[tot]=edge(u, v, head[u], cap); head[u] = tot++;
		e[tot]=edge(v, u, head[v], 0); head[v] = tot++;
	}
	int bfs() {
		int fron = 0, tail = 0;
		memset(dist, -1, sizeof(dist));
		que[tail++] = st;
		dist[st] = 0;
		while(fron < tail) {
			int u = que[fron ++];
			cur[u] = head[u];
			for(int i=head[u];i!=-1;i=e[i].nxt) 
				if(dist[e[i].v] == -1 && e[i].cap > 0) {
					dist[e[i].v] = dist[u] + 1;
					que[tail++] = e[i].v;
				}
		}
		return dist[en] != -1;
	}
	int dfs(int v, int cap) {
		if (v == en) return cap;
		int flow = 0;
		for(int &i = cur[v]; i!=-1 && cap > 0; i=e[i].nxt)
			if(dist[e[i].v] == dist[v] + 1 && e[i].cap > 0) {
				int det = dfs(e[i].v, min(e[i].cap, cap));
				flow += det;
				e[i].cap -= det; e[i^1].cap += det;
				if(!(cap -= det)) return flow;
			}
		return flow;
	}
	inline int maxflow() {
		int ret = 0;
		while(bfs()) ret += dfs(st, INF);
		return ret;
	}
}G;

int N, K;

int p[500][500];

int run() {
	scanf("%d %d", &N, &K);
	
	int S=0, T=2*N+1;
	G.clear(0, 2*N+1, 2*N+2);
	
	for(int i=1;i<=N;++i) {
		for(int j=1;j<=K;++j)
			scanf("%d", &p[i][j]);
		G.insert(S, i, 1);
		G.insert(N+i, T, 1);
	}
	
	for(int i=1;i<=N;++i) 
		for(int j=1;j<=N;++j) {
			bool flag=true;
			for(int k=1;k<=K && flag;++k)
				if(p[i][k] <= p[j][k]) flag=false;
			if(flag) {
				G.insert(i, N+j, 1);
			}
		}
	int t = G.maxflow();
	cout<<N-t<<endl;
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int test; cin>>test;
	for(int no=1;no<=test;++no) {
		cout<<"Case #"<<no<<": "; run();
	}
}
