#include <cstdio>
#include <algorithm>
using namespace std;

bool solve() {
	int N, l[10010], d[10010] = {0,}, r[10010];
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d%d", &d[i], &l[i]);
		r[i] = 0;
	}
	scanf("%d", &d[N+1]);
	r[1] = min(l[1], d[1]);
	for (int i = 1; i <= N; i++) {
		int reach = d[i] + r[i];
		for (int j = i + 1; d[j] <= reach; j++) {
			if (j == N + 1) return 1;
			r[j] = max(r[j], min(l[j], d[j] - d[i]));
		}
	}
	return 0;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		printf("Case #%d: %s\n", t + 1, solve() ? "YES" : "NO");
	}
	return 0;
}
