#include <cstdio>
#include <cstring>

const int MAXN = 310;

class MaxMatch {
public:
	int n, m;
	
	bool mat[MAXN][MAXN];

	int maxMatch() {
		int head[MAXN + 1], tail[MAXN], ret = 0, ll[MAXN], rr[MAXN];
		memset(ll, 0xFF, sizeof(ll));
		memset(rr, 0xFF, sizeof(rr));
		for (int i = 0; i < n; i++) {
			memset(tail, 0xFF, sizeof(tail));
			int q = 0;
			head[0] = i;
			for (int p = 0; p <= q; p++) {
				if (ll[i] >= 0) break;
				int k = head[p];
				for (int j = 0; j < m; j++) {
					if (ll[i] >= 0) break;
					if (mat[k][j] && tail[j] < 0) {
						head[++q] = rr[j];
						tail[j] = k;
						if (head[q] < 0) {
							for (p = j; p >= 0; j = p) {
								rr[j] = k = tail[j];
								p = ll[k];
								ll[k] = j;
							}
						}
					}
				}
			}
			if (ll[i] >= 0) ret++;
	 	}
		return ret;
	}
} mmat;

int N, M, price[MAXN][MAXN];

inline int SIGN(int x) {
	if (x > 0) return 1;
	if (x < 0) return -1;
	return 0;
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) scanf("%d", &price[i][j]);
		}
		memset(mmat.mat, 0, sizeof(mmat.mat));
		mmat.n = mmat.m = N;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				bool flag = true;
				for (int k = 1; k < M; k++) {
					if (SIGN(price[i][k - 1] - price[j][k - 1]) * SIGN(price[i][k] - price[j][k]) <= 0) {
						flag = false;
						break;
					}
				}
				if (flag && price[i][0] > price[j][0]) mmat.mat[i][j] = true;
			}
		}
		printf("Case #%d: %d\n", oo + 1, N - mmat.maxMatch());
	}
	return 0;
}
