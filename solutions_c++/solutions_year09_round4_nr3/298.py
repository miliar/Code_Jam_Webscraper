#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 209;

bool vst[MAXN], forbid[MAXN];
int cy[MAXN], que[MAXN], qN;  // cy[y]<-->y
int N, K;

struct Edge {
	int to;
	Edge *next;
};

Edge edges[MAXN * MAXN], *g[MAXN];
int nEdge;

void init() {
	memset(g, 0, sizeof(g));
	nEdge = 0;
}

void link(int x, int y) {
	Edge *p = &edges[nEdge++];
	p->to = y;
	p->next = g[x];
	g[x] = p;
}


bool dfs(int x)
{
    int k, v;
    Edge* p;
    for (p = g[x]; p; p = p->next)
        if (!vst[v = p->to] && !forbid[v])
        {
            que[qN++] = v;
            vst[v] = true;
            k = cy[v];
            cy[v] = x;
            if (k == -1 || dfs(k))
                return true;
            cy[v] = k;
        }
    return false;
}

int bpMatch(int nv1, int nv2)
{
    int i, j, ans = 0;
    memset(cy, -1, nv2 * sizeof(int));
    memset(forbid, false, nv2);
    for (i = 0; i < nv1; i++)
    {
        memset(vst, false, nv2); qN = 0;
        if (dfs(i))
        {
            ans++; continue;
        }
        for (j = 0; j < qN; j++)
            forbid[que[j]] = true;
    }
    return ans;
}

int mat[MAXN][MAXN];

int main() {
	freopen("D:\\C-large.in", "r", stdin);
	freopen("D:\\C-large.out", "w", stdout);
	int i, j, k,  T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &N, &K);
		for (i = 0; i < N; ++i)
			for (j = 0; j < K; ++j)
				scanf("%d", &mat[i][j]);
		init();
		for (i = 0; i < N; ++i)
			for (j = 0; j < N; ++j) {
				for (k = 0; k < K; ++k)
					if (mat[i][k] >= mat[j][k]) break;
					if (k >= K) {
						link(i, j);
				//		printf("i = %d j = %d\n", i, j);
					}
			}
		printf("Case #%d: %d\n", ++cas, N - bpMatch(N, N));

	}
	return 0;
}