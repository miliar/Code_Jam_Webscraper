#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <cassert>
using namespace std;

const int N = 7200;
const int INF = 1 << 28;

class Edge {
public:
	int u, v, cuv, cvu, flow;
	Edge() {}
	Edge(int cu, int cv, int ccu, int ccv) : u(cu), v(cv), cuv(ccu), cvu(ccv), flow(0) {}
	int other(int p) const { return p == u ? v : u; }
	int cap(int p) const { return p == u ? cuv-flow : cvu+flow; }
	void addFlow(int p, int f) { flow += (p == u ? f : -f); }
};

class Graph {
private:
	vector<Edge> eg;
	vector<Edge*> net[N];
	Edge* prev[N];
	int v, s, t;
	int h[N], hn[2*N], cur[N];
	void initNet();
	void initFlow();
	void initHeight();
	void gapHeuristic(int);
public:
	void clear() { eg.clear(); v = 0; }
	void setMaxNode(int cv) { v = cv; }
	void insert(int cu, int cv, int ccu, int ccv = 0)
		{ eg.push_back(Edge(cu, cv, ccu, ccv)); }
	int maxFlow(int, int);
};
void Graph::initHeight() {
	memset(h, 0, sizeof(h)); memset(hn, 0, sizeof(hn));
	for(int i = 0; i < v; i++) h[i] = v;
	queue<int> Q; Q.push(t); h[t] = 0;
	while(!Q.empty()) {
		int p = Q.front(); Q.pop();
		for(int i = net[p].size()-1; i >= 0; i--) {
			int u = net[p][i]->other(p), ec = net[p][i]->cap(u);
			if(ec != 0 && h[u] == v) { h[u] = h[p]+1; Q.push(u); }
		}
	}
	for(int i = 0; i < v; i++) hn[h[i]]++;
}
void Graph::gapHeuristic(int k) {
	if(hn[k] != 0) return;
	for(int i = 0; i < v; i++)
		if(h[i] > k) h[i] = v;
	for(int i = k; i < v; i++)
		{ hn[v] += hn[i]; hn[i] = 0; }
}
void Graph::initNet() {
	for(int i = 0; i < v; i++) net[i].clear();
	for(int i = eg.size()-1; i >= 0; i--) {
		net[eg[i].u].push_back(&eg[i]);
		net[eg[i].v].push_back(&eg[i]);
	}
}
void Graph::initFlow() {
	initNet(); initHeight();
	for(int i = 0; i < v; i++) cur[i] = net[i].size()-1;
}
int Graph::maxFlow(int ss, int tt) {
	s = ss; t = tt; initFlow();
	int c = s, pre[N], flow = 0;
	pre[s] = -1;
	while(h[s] < v) {
		for(; cur[c] >= 0; cur[c]--)
			if(net[c][cur[c]]->cap(c) != 0 && h[c] == h[net[c][cur[c]]->other(c)]+1) break;
		if(cur[c] < 0) {
			int mh = INF, oh = h[c];
			for(int i = net[c].size()-1; i >= 0; i--)
				if(net[c][i]->cap(c) != 0) mh <?= h[net[c][i]->other(c)];
			if(mh == INF) h[c] = v;
			else { h[c] = mh+1; cur[c] = net[c].size()-1; }
			hn[oh]--; hn[h[c]]++; gapHeuristic(oh);
			if(c != s) c = pre[c];
		} else {
			int p = net[c][cur[c]]->other(c);
			prev[p] = net[c][cur[c]];
			pre[p] = c; c = p;
			if(c == t) {
				int ex = INF;
				for(; c != s; c = pre[c]) ex <?= prev[c]->cap(pre[c]);
				for(c = t; c != s; c = pre[c]) prev[c]->addFlow(pre[c], ex);
				flow += ex; c = s;
			}
		}
	}
	return flow;
}

const int M = 128;

char mp[M][M];
int lb1[M][M], lb2[M][M];

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)
#define CLEAR(a, b) memset((a), (b), sizeof(a))

int main()
{
	int T;
	scanf("%d", &T);
	Graph g;
	FOR(t, 0, T) {
		int n, m; scanf("%d %d", &n, &m);
		FOR(i, 0, n) scanf("%s", mp[i]);
		g.clear();
		int n1 = 0, m1 = 0;
		CLEAR(lb1, -1); CLEAR(lb2, -1);
		FOR(i, 0, n) FOR(j, 0, m) if(mp[i][j] == '.') {
			if(j%2 == 0) lb1[i][j] = n1++;
			else lb2[i][j] = m1++;
		}
		FOR(i, 0, n) FOR(j, 0, m) if(mp[i][j] == '.') {
			int dir[][2] = { { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 } };
			FOR(d, 0, 4) {
				int cx = i+dir[d][0], cy = j+dir[d][1];
				if(cx < 0 || cx >= n || cy < 0 || cy >= m) continue;
				if(mp[cx][cy] != '.') continue;
				if(j%2 == 0) g.insert(lb1[i][j]+2, lb2[cx][cy]+n1+2, 1);
				else g.insert(lb1[cx][cy]+2, lb2[i][j]+n1+2, 1);
			}
		}
		FOR(i, 0, n) FOR(j, 0, m) if(mp[i][j] == '.') {
			if(j%2 == 0) g.insert(0, lb1[i][j]+2, 1);
			else g.insert(lb2[i][j]+n1+2, 1, 1);
		}
		g.setMaxNode(n1+m1+2);
		printf("Case #%d: %d\n", t+1, n1+m1-g.maxFlow(0, 1));
	}
	return 0;
}

