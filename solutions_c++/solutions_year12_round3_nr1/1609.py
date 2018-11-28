#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

#define MAXN 1006
#define MAXM 900000

const int INF = (1 << 29) - 1;

typedef struct tNode
{
	int v, f;
	tNode *nxt, *rev;
}Edge;
Edge *E[MAXN], *Cur[MAXN], mem[MAXM];
int n, N, S, T, eCnt;
int gap[MAXN], d[MAXN];
int flow, aug;
bool done;

void init()
{
	for (int i = 0; i < N; i++)
		E[i] = NULL;
	eCnt = 0;
}

void Add_Edge(int u, int v, int f)
{
	Edge *p = &mem[eCnt++], *q = &mem[eCnt++];
	p->v = v, p->f = f, p->rev = q;
	p->nxt = E[u], E[u] = p;
	q->v = u, q->f = 0, q->rev = p;
	q->nxt = E[v], E[v] = q;
}

void SAP(int u)
{
	if (u == T)
	{
		done = true;
		flow += aug;
		return ;
	}
	Edge *p = NULL;
	int augOri = aug;
	for (p = Cur[u]; p != NULL; p = p->nxt)
	{
		if (p->f <= 0) continue;
		if (d[p->v] + 1 == d[u])
		{
			Cur[u] = p;
			aug = min(aug, p->f);
			SAP(p->v);
			if (d[S] >= N) return ;
			if (done) break;
			aug = augOri;
		}
	}
	if (done) p->f -= aug, p->rev->f += aug;
	else
	{
		if (!(--gap[d[u]])) d[S] = N;
		int minD = N + 1;
		Cur[u] = E[u];
		for (p = Cur[u]; p != NULL; p = p->nxt)
			if (p->f > 0) minD = min(minD, d[p->v]);
		d[u] = minD + 1;
		gap[d[u]]++;
	}
}

int MaxFlow()
{
	for (int i = 0; i < N; i++)
		gap[i] = d[i] = 0, Cur[i] = E[i];
	gap[0] = N;
	flow = 0;
	while (d[S] < N)
	{
		aug = INF;
		done = false;
		SAP(S);
	}
	return flow;
}

int G[MAXN][MAXN];
int outDeg[MAXN], inDeg[MAXN];

void BuildNetwork(int s, int t)
{
	init();
	Add_Edge(S, s, 2);
	Add_Edge(t, T, 2);
	for (int i = 1; i <= n; i++)
		for (int j = 0; j < outDeg[i]; j++)
			Add_Edge(i, G[i][j], 1);
}

bool check(int s, int t)
{
	BuildNetwork(s, t);
	MaxFlow();
	return flow >= 2;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-lowesy.out", "w", stdout);
	int _, cases = 1;
	scanf("%d", &_);
	while (_--)
	{
		scanf("%d", &n);
		S = 0, T = n + 1, N = n + 2;
		memset(inDeg, 0, sizeof(inDeg));
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &outDeg[i]);
			for (int j = 0; j < outDeg[i]; j++)
			{
				scanf("%d", &G[i][j]);
				inDeg[G[i][j]]++;
			}
		}
		bool ok = false;
		for (int s = 1; s <= n && !ok; s++)
		{
			if (!outDeg[s]) continue;
			for (int t = 1; t <= n && !ok; t++)
			{
				if (s == t) continue;
				if (!inDeg[t]) continue;
				if (check(s, t)) ok = true;
			}
		}
		printf("Case #%d: %s\n", cases++, ok ? "Yes" : "No");
	}
	return 0;
}