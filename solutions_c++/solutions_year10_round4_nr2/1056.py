#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>

#define MAX 4096

using namespace std;
FILE *in; FILE *out;


// Dinitz Algorithm

#define MAX_NODES 2048
#define MAX_EDGES 131072
#define INF 999666333
#define SOURCE (MAX_NODES - 1)
#define SINK (MAX_NODES - 2)

struct Edge
{
	int next, to, cap;
	Edge(int next_ = 0, int to_ = 0, int cap_ = 0)
		{next = next_; to = to_; cap = cap_;}
};

int source, sink;
Edge edges[MAX_EDGES]; int numEdges;
int vis[MAX_NODES], dist[MAX_NODES], first[MAX_NODES];
int ma3x[MAX_NODES][MAX_NODES];

int recurse(int node, int flow)
{
	if (node == sink) return flow;
	for (int idx = first[node]; idx != -1; idx = edges[idx].next)
	{
		if (!vis[edges[idx].to] && ma3x[node][edges[idx].to] > 0 && dist[node] == dist[edges[idx].to] + 1)
		{
			int ret = recurse(edges[idx].to, min(flow, edges[idx].cap));
			if (ret) {ma3x[node][edges[idx].to] -= ret; ma3x[edges[idx].to][node] += ret; return ret;}
		}
	}
	vis[node] = 1;
	return 0;
}

int dinitz(int source_, int sink_)
{
	source = source_; sink = sink_;
	
	int flow = 0;
	while (1)
	{
		// BFS
		int cur = 0;
		queue <int> q;

		for (int i=0; i<MAX_NODES; i++) dist[i] = MAX_NODES;
		q.push(sink); dist[sink] = 0;
		
		while (!q.empty())
		{
			cur = q.front(); q.pop();
			for (int idx = first[cur]; idx != -1; idx = edges[idx].next)
			{
				if (ma3x[edges[idx].to][cur] > 0 && dist[edges[idx].to] == MAX_NODES)
				{
					dist[edges[idx].to] = dist[cur] + 1;
					q.push(edges[idx].to);
					if (edges[idx].to == source) {cur = source; break;}
				}
			}
			if (cur == source) break;
		}
		if (cur != source) break;
		
		// DFS
		int flag = 0;
		memset(vis, 0, sizeof(vis));
		while(1)
		{
			int add = recurse(source, INF);
			if (add == 0) break;
			flow += add; flag = 1;
		}
		if (!flag) break;
	}
	return flow;
}

inline void addEdge(int from, int to, int cap)
{
	if (!numEdges) memset(first, -1, sizeof(first));
	edges[numEdges].to = to; edges[numEdges].cap = cap;
	edges[numEdges].next = first[from]; first[from] = numEdges++;
	ma3x[from][to] += cap;
	
	edges[numEdges].to = from; edges[numEdges].cap = 0;
	edges[numEdges].next = first[to]; first[to] = numEdges++;
}

// End of Dinitz Algorithm

int origMa3x[MAX_NODES][MAX_NODES];
int matchPrice[MAX];
int svMa3x[MAX_NODES][MAX_NODES];

void doWork(int testNum)
{
	int n, numTeams;
	fscanf(in, "%d", &n);
	numTeams = (1 << n);
	
	int rem[MAX];
	for (int i = 0; i < numTeams; i++)
	{
		fscanf(in, "%d", &rem[i]);
		rem[i] = n - rem[i];
	}
	
	for (int i = 0; i < numTeams - 1; i++)
		fscanf(in, "%d", &matchPrice[i]);

	/*
	numEdges = 0;
	memset(ma3x, 0, sizeof(ma3x));
	for (int i = 0; i < numTeams; i++)
	{
		int cur;
		fscanf(in, "%d", &cur);
		addEdge(SOURCE, i, n - cur);
	}
	
	
	int div = 1;
	int next = 0;
	for (int level = 0; level < n; level++)
	{
		div *= 2;
		int lim = (1 << (n - level - 1));
		for (int i = 0; i < lim; i++)
		{
			fscanf(in, "%d", &matchPrice[next]);
			addEdge(numTeams + next + i, SINK, INF);
		}
		for (int i = 0; i < numTeams; i++)
			addEdge(i, numTeams + next + i / div, 1);
		
		next += lim;
	}

	memcpy(origMa3x, ma3x, sizeof(origMa3x));
	
	int flow = dinitz(SOURCE, SINK);
	memcpy(svMa3x, ma3x, sizeof(svMa3x));
	cout << "FLow is: " << flow << endl;
	int ans = 0;
	
	for (int i = 0; i < numTeams - 1; i++)
	{
		if (svMa3x[numTeams + i][SINK] < INF)
		{
			memcpy(ma3x, origMa3x, sizeof(ma3x));
			ma3x[numTeams + i][SINK] = 0;
			int cflow = dinitz(SOURCE, SINK);
			cout << "Trying edge " << i << " with cflow = " << cflow << endl;
			if (cflow < flow) ans++;
			else origMa3x[numTeams + i][SINK] = 0;
		}
		else origMa3x[numTeams + i][SINK] = 0;
	}
	*/
	
	int ans = 0;
	int size = 1, idx = numTeams - 2;
	int level = 0;
	while (idx >= 0)
	{
		level++;
		int didx = numTeams - 1;
		int cnt = (1 << (n - level + 1));
		for (int i = 0; i < size; i++)
		{
			int flag = 0;
			for (int c = 0; c < cnt; c++)
			{
				if (rem[didx] > 0) {rem[didx]--; flag = 1;}
				didx--;
			}
			idx--;
			ans += flag;
		}
		size *= 2;
	}
	
	fprintf(out, "%d\n", ans);
	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("WorldCup2010.in", "rt");
	out = fopen("WorldCup2010.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
