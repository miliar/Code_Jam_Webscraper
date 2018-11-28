#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		int N;
		scanf("%d", &N);
		int cnt = 0;
		for (int i=0; i<N; ++i) {
			int k;
			scanf("%d", &k);
			if (k!=i+1) ++cnt;
		}
		printf("Case #%d: %.7lf\n", t+1, (double)cnt);
	}
	return 0;
}