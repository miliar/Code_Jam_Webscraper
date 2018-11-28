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

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int PMAX = 400;

const int INF = 1000000000;

const int MOD = 1000003;

const int NMAX = 100*100;

int R, C, N;

bool vis[NMAX];
VI Gout[NMAX], Gin[NMAX];

inline int to_ver(int r, int c) {
	return r*C + c;
}

inline void add_edge(int r, int c, int nr, int nc) {
	nr %= R;
	if (nr < 0) nr += R;
	nc %= C;
	if (nc < 0) nc += C;
	Gout[to_ver(r, c)].PB(to_ver(nr, nc));
	Gin[to_ver(nr, nc)].PB(to_ver(r, c));
}

int clean(int res) {
	REP(i, N) {
		Gin[i].clear();
		Gout[i].clear();
	}
	printf("%d\n", res);
	return -1;
}

void DFS(int x) {
	vis[x] = true;
	REP(i, 2) {
		int y = Gout[x][i];
		int z = Gin[y][Gin[y][0] == x ? 1 : 0];
		if (!vis[z]) DFS(z);
	}
}

int testcase() {
	scanf("%d%d", &R, &C);
	N = R*C;
	REP(r, R) REP(c, C) {
		static char buf[10];
		scanf("%1s", buf);
//putchar(buf[0]);
		switch (buf[0]) {
			case '-':
				add_edge(r, c, r, c-1);
				add_edge(r, c, r, c+1);
			break;
			case '|':
				add_edge(r, c, r-1, c);
				add_edge(r, c, r+1, c);
			break;
			case '/':
				add_edge(r, c, r-1, c+1);
				add_edge(r, c, r+1, c-1);
			break;
			case '\\':
				add_edge(r, c, r-1, c-1);
				add_edge(r, c, r+1, c+1);
			break;
		}
	}
	
	REP(u, N) if (Gin[u].size() == 0)
		return clean(0);
	
	queue<int> Q;
	REP(u, N) if (Gin[u].size() == 1)
		Q.push(u);
	while (!Q.empty()) {
		int y = Q.front();
		Q.pop();
		
		int x = Gin[y][0];
		Gin[y].clear();
		
		int z = Gout[x][Gout[x][0] == y ? 1 : 0];
		Gout[x].clear();
		
		if (Gin[z].size() == 1) return clean(0);
		VI::iterator it = find(ALL(Gin[z]), x);
		swap(*it, Gin[z].back());
		Gin[z].pop_back();
		if (Gin[z].size() == 1) Q.push(z);
	}
	
	int res = 1;
	fill_n(vis, N, false);
	REP(u, N) if (!vis[u] && Gout[u].size() == 2) {
		res += res;
		if (res >= MOD) res -= MOD;
		DFS(u);
	}
	return clean(res);
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d: ", i);
		testcase();
	}
}
