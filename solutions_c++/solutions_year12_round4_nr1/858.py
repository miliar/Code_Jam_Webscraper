#include <cstdio>
#include <algorithm>
#define INF 0x7fffffff
using namespace std;

int main() {
	int T;

	scanf("%d", &T);
	for(int _t = 1; _t <= T; ++_t) {
		int N, D;
		scanf("%d", &N);

		int X[N+1], L[N+1];
		for(int i = 0; i < N; ++i) {
			scanf("%d%d", &X[i], &L[i]);
		}
		scanf("%d", &D);
		X[N] = D;
		L[N] = INF;

		int max_h[N+1];
		fill(max_h, max_h + N + 1, 0);
		max_h[N] = -1;

		max_h[0] = min(X[0], L[0]);
		for(int i = 0; i < N; ++i) {
			int swing = max_h[i];
			for(int j = i + 1; j <= N && (X[j] - X[i]) <= swing; ++j) {
				max_h[j] = max(max_h[j], min(L[j], X[j] - X[i]));
			}
		}


		bool sol = max_h[N] > -1;
		printf("Case #%d: %s\n", _t, sol ? "YES" : "NO");
	}

	return 0;
}
