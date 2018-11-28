
#include <cstdio>

using namespace std;

int a[101];
int best[101][256]; // pos, val
int D, I, M, N;
const int INF = (1 << 30);

inline int abs(int x) {
	return x > 0 ? x : -x;
}

int solve() {
	if(N == 1)
		return 0;

	for(int v = 0; v < 256; v++) {
		best[0][v] = 0;
	}

	for(int i = 1; i <= N; i++) {
		// delete
		for(int v = 0; v < 256; v++)
			best[i][v] = best[i-1][v] + D;

		// change/extend
		for(int ch = 0; ch < 256; ch++) {
			int b = a[i] - ch;
			if(b >= 0) {
				for(int dv = -M; dv <= M; dv++) {
					if(b + dv < 256 && b + dv >= 0 &&
							best[i][b] > best[i-1][b+dv] + ch)
						best[i][b] = best[i-1][b+dv] + ch;
				}
			}
			b = a[i] + ch;
			if(b < 256) {
				for(int dv = -M; dv <= M; dv++) {
					if(b + dv < 256 && b + dv >= 0 &&
							best[i][b] > best[i-1][b+dv] + ch)
						best[i][b] = best[i-1][b+dv] + ch;
				}
			}
		}

		// insert
		for(int v = 0; v < 256; v++) {
			for(int dv = -M; dv <= M; dv++) {
				if(v + dv < 256 && v + dv >= 0 &&
						best[i][v] > best[i][v+dv] + I)
					best[i][v] = best[i][v+dv] + I;
			}
		}
		for(int v = 256; v >= 0; v--) {
			for(int dv = -M; dv <= M; dv++) {
				if(v + dv < 256 && v + dv >= 0 &&
						best[i][v] > best[i][v+dv] + I)
					best[i][v] = best[i][v+dv] + I;
			}
		}
	}

	int res = INF;
	for(int v = 0; v < 256; v++)
		if(res > best[N][v])
			res = best[N][v];
	return res;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for(int i = 0; i < N; i++) {
			scanf("%d", &a[i+1]);
		}
		printf("Case #%d: %d\n", t, solve());
	}

	return 0;
}
