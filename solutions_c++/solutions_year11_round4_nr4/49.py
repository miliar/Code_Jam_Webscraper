#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define FOR(i, a, b) for (int i = (a), _n = (b); i <= _n; ++i)
#define FORD(i, a, b) for (int i = (a), _n = (b); i >= _n; --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef pair<int,int> PII;
typedef vector<int> VI;

const int PMAX = 400;

const int INF = 1000000000;

int N, bitN, d[PMAX], ind[PMAX], deg[PMAX], dyn[PMAX][PMAX], shared_neigh[PMAX][PMAX];
bool G[PMAX][PMAX];
unsigned int Gbit[PMAX][20];

void read_data() {
	int M;
	scanf("%d%d", &N, &M);
	REP(i, N) fill_n(G[i], N, false);
	REP(i, M) {
		int a, b;
		scanf("%d,%d", &a, &b);
		G[a][b] = G[b][a] = true;
	}
}

void solve() {
	const int bitN = (N+31)/32;
	
	REP(u, N) fill_n(Gbit[u], bitN, 0);
	REP(u, N) REP(v, N) if (G[u][v])
		Gbit[u][v/32] |= 1UL<<(v%32);
	
	int qbeg = 0, Nind = 0;
	fill_n(d, N, INF);
	d[0] = 0;
	ind[Nind++] = 0;
	while (qbeg != Nind) {
		int u = ind[qbeg++];
		REP(v, N) if (G[u][v] && d[v] == INF) {
			d[v] = d[u]+1;
			ind[Nind++] = v;
		}
	}
	fill_n(deg, N, 0);
	REP(u, N) REP(v, N) if (G[u][v]) ++deg[u];
	
	REP(u, N) FOR(v, 0, u-1) {
		shared_neigh[u][v] = 0;
		REP(i, bitN) shared_neigh[u][v] += __builtin_popcount(Gbit[u][i] & Gbit[v][i]);
	}
	REP(u, N) FOR(v, u+1, N-1) shared_neigh[u][v] = shared_neigh[v][u];
//REP(u, N) {	REP(v, N) printf("%d ", shared_neigh[u][v]); printf("\n"); }
	
//printf("Nind=%d\n", Nind);	
	REP(u, N) REP(v, N) dyn[u][v] = -1;
	REP(i, Nind) {
		int u = ind[i];
		if (u == 0) {
			dyn[u][0] = deg[u];
			continue;
		}
		if (u == 1) {
			int res = 0;
			REP(v, N) REP(w, N) if (G[v][u] && d[v]+1 == d[u] && dyn[v][w] != -1)
				res = max(res, dyn[v][w]);
			printf("%d %d\n", d[u]-1, res);
			return;
		}
		REP(v, N) if (G[v][u] && d[v]+1 == d[u]) {
			dyn[u][v] = 0;
			REP(w, N) if (dyn[v][w] != -1) {
				int tmp = dyn[v][w]-2+deg[u];
				REP(z, N) if (z != u && z != v && z != w && (G[v][z]||G[w][z]) && G[u][z]) --tmp;
				dyn[u][v] = max(dyn[u][v], tmp);
			}
		}
//dyn[u] = max(dyn[u], dyn[v]+deg[u]-2-shared_neigh[u][v]);
//printf("dyn[%d]=%d\n", u, dyn[u]);
	}
}

void testcase() {
	read_data();
	solve();
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d: ", i);
		testcase();
	}
}
