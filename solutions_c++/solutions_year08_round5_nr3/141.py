#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
using namespace std;

struct Network
{
	static const int MAX_NODE_NUM = 100 * 100 * 2;

	typedef int Capa;
	static const Capa INF = 10000000;

	struct Edge
	{
		int start;
		int target;
		Capa flow;
		Capa capa;
		Edge* prev;
		Edge* opposite;
		
		Edge(int start, int target, Capa capa, Capa flow)
		{
			this->start = start;
			this->target = target;
			this->capa = capa;
			this->flow = flow;
		}
	};

	int source;
	int sink;
	int nodeNum;
	int edgeNum;
	Edge* last[MAX_NODE_NUM];
	Edge* lastAugment[MAX_NODE_NUM];
	Capa lastUsed[MAX_NODE_NUM];
	Capa curFlow;
	Capa curDelta;
	bool reachable[MAX_NODE_NUM];

	void initialize(int source, int sink, int nodeNum)
	{
		this->source = source;
		this->sink = sink;
		this->nodeNum = nodeNum;
		this->edgeNum = 0;
		memset(last, 0, sizeof(Edge*) * nodeNum);
	}
	void addEdge(int start, int target, Capa capa, Capa flow = 0)
	{
		Edge* positive = new Edge(start, target, capa, flow);
		Edge* negative = new Edge(target, start, 0, -flow);

		positive->opposite = negative;
		negative->opposite = positive;

		positive->prev = last[start];
		last[start] = positive;
		negative->prev = last[target];
		last[target] = negative;
		
		edgeNum += 2;
	}
	bool findPath(int start, Capa delta)
	{
		lastUsed[start] = curFlow;
		if (start == sink)
		{
			curDelta = delta;
			return true;
		}
		if (last[start] == NULL)
			return false;
		Edge* curEdge = lastAugment[start];
		do
		{
			if (lastUsed[curEdge->target] < curFlow && curEdge->flow < curEdge->capa)
				if (findPath(curEdge->target, min(delta, curEdge->capa - curEdge->flow)))
				{
					curEdge->flow += curDelta;
					curEdge->opposite->flow -= curDelta;
					lastAugment[start] = curEdge;
					return true;
				}
			curEdge = curEdge->prev;
			if (curEdge == NULL)
				curEdge = last[start];
		}
		while (curEdge != lastAugment[start]);
		return false;
	}
	Capa getMaxFlow()
	{
		memset(lastUsed, -1, sizeof(Capa) * nodeNum);
		memcpy(lastAugment, last, sizeof(Edge*) * nodeNum);
		curFlow = 0;
		while (findPath(source, INF))
			curFlow += curDelta;
		return curFlow;
	}
	void clearGraph()
	{
		for (int i = 0; i < nodeNum; i++)
			for (Edge* curEdge = last[i]; curEdge != NULL; )
			{
				Edge* tmpEdge = curEdge->prev;
				delete curEdge;
				curEdge = tmpEdge;
			}
	}
	void clearFlow()
	{
		for (int i = 0; i < nodeNum; i++)
			for (Edge* curEdge = last[i]; curEdge != NULL; curEdge = curEdge->prev)
				curEdge->flow = 0;
	}
	void dfsCut(int start)
	{
		reachable[start] = true;
		for (Edge* curEdge = last[start]; curEdge != NULL; curEdge = curEdge->prev)
			if (!reachable[curEdge->target] && curEdge->flow < curEdge->capa)
				dfsCut(curEdge->target);
	}
	void findCut()
	{
		memset(reachable, 0, sizeof(reachable));
		dfsCut(source);
	}
};

int n, m;
char buffer[100];
Network net;

void link(int i, int j, int x, int y)
{
	if (x < 0 || y < 0 || y >= n)
		return;
	int s = i * n + j;
	int t = x * n + y;
	if (j & 1)
		net.addEdge(s, t, Network::INF);
	else
		net.addEdge(t, s, Network::INF);
}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d", &m, &n);
		net.initialize(m * n, m * n + 1, m * n + 2);
		int cnt = n * m;
		for (int i = 0; i < m; i++)
		{
			scanf("%s", buffer);
			for (int j = 0; j < n; j++)
				if (buffer[j] == '.')
				{
					if (j & 1)
						net.addEdge(n * m, i * n + j, 1);
					else
						net.addEdge(i * n + j, n * m + 1, 1);
				}
				else
					cnt--;
		}
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
			{
				link(i, j, i, j - 1);
				link(i, j, i, j + 1);
				link(i, j, i - 1, j - 1);
				link(i, j, i - 1, j + 1);
			}
		printf("Case #%d: %d\n", testInd + 1, cnt - net.getMaxFlow());
	}
	return 0;
}
