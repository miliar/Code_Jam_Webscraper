#include<stdio.h>
#include<queue>
#include<algorithm>
using namespace std;

#define INF 1e200

typedef struct Node {
	int r, c;
	double t;
	Node() {}
	Node(int x, int y, double z):r(x), c(y), t(z) {}
	bool operator<(const struct Node &a) const {
		if(t != a.t) return t > a.t;
		if(r != a.r) return r < a.r;
		return c < a.c;
	}
}Node;

int nCase;
int H, N, M;
int C[128][128], F[128][128];
int dr[4] = {1, 0, -1, 0}, dc[4] = {0, 1, 0, -1};
double T[128][128];

priority_queue<Node> PQ;

inline double getTime(int c1, int f1, int c2, int f2, double t0) {
	double w = H - 10.0*t0;
	if(c2-f1 < 50 || c2-f2 < 50 || c1-f2 < 50) return INF;
	if(c2-w >= 50) {	// go directly
		if(t0 == 0) return 0;
		else return t0 + ((w-f1>=20)?1:10);
	} else {	// must wait for tide out
		double t = 5 - (c2-H)/10.0;
		if(t0 < t) t0 = t;
		w = H - 10.0*t0;
		return t0 + ((w-f1>=20)?1:10);
	}
}

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d %d %d", &H, &N, &M);
		for(int i = 0; i < N; ++i) for(int j = 0; j < M; ++j)
			scanf("%d", &C[i][j]);
		for(int i = 0; i < N; ++i) for(int j = 0; j < M; ++j)
			scanf("%d", &F[i][j]);
		for(int i = 0; i < N; ++i) for(int j = 0; j < M; ++j) T[i][j] = INF;
		T[0][0] = 0;
		while(!PQ.empty()) PQ.pop();
		PQ.push(Node(0, 0, 0));
		Node now;
		while(!PQ.empty()) {
			now = PQ.top();
			PQ.pop();
			if(now.r == N-1 && now.c == M-1) break;
			if(now.t > T[now.r][now.c]) continue;
			for(int i = 0; i < 4; ++i) {
				int nr = now.r + dr[i], nc = now.c + dc[i];
				if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
				double nt = getTime(C[now.r][now.c], F[now.r][now.c], C[nr][nc], F[nr][nc], now.t);
				if(nt < T[nr][nc]) {
					PQ.push(Node(nr, nc, nt));
					T[nr][nc] = nt;
				}
			}
		}

		printf("Case #%d: %.9lf\n", cs, now.t);
	}
}


