
#include <cstdio>
#include <vector>
using namespace std;

typedef long long LL;

LL best[1005][15];

int main() {
	int tst;
	scanf("%d", &tst);
	for (int cas = 0; cas < tst; ++cas) {
		LL L, t, N, C;
		scanf("%lld %lld %lld %lld", &L, &t, &N, &C);
		vector<LL> a(C);
		for (int i = 0; i < C; ++i)
			scanf("%lld", &a[i]);
		vector<LL> A(N);
		for (int i = 0; i < N; ++i)
			A[i] = a[i % C];
		for (int i = 0; i <= N; ++i)
			for (int j = 0; j <= L; ++j) {
				best[i][j] = 1LL << 60;
			}
		
		best[0][0] = 0;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j <= L; ++j) {
				best[i + 1][j] = min(best[i + 1][j], best[i][j] + A[i] * 2LL);
				if (j + 1 <= L) {
					if (best[i][j] >= t)
						best[i + 1][j + 1] = min(best[i + 1][j + 1], best[i][j] + A[i]);
					else if (best[i][j] + A[i] * 2 <= t) {
						best[i + 1][j + 1] = min(best[i + 1][j + 1], best[i][j] + A[i] * 2LL);
					} else {
						LL slowHours = t - best[i][j];
						best[i + 1][j + 1] = min(best[i + 1][j + 1], t + (A[i] - slowHours / 2));
					}
				}
			}
		printf("Case #%d: %lld\n", cas + 1, best[N][L]);
	}
	return 0;
}