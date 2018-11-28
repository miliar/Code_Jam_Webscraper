#include<cstdio>

#define MAXN 20
int val[MAXN], T, N;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for(int re = 1; re <= T; ++re) {
		scanf("%d", &N);
		for(int i = 0; i < N; ++i)
			scanf("%d", &val[i]);
		int ans = -1;
		for(int ri = 1; ri < (1 << N) - 1; ++ri) {
			int cntSean = 0, cntBrother = 0;
			int tmp = ri, sum = 0;
			for(int j = 0; j < N; ++j) {
				if(tmp & 1) {
					cntSean ^= val[N - j - 1];
					sum += val[N - j - 1];
				} else {
					cntBrother ^= val[N - j - 1];
				}
				tmp >>= 1;
			}
			if(cntSean == cntBrother && ans < sum)
				ans = sum;
		}
		printf("Case #%d: ", re);
		if(ans == -1) puts("NO");
		else printf("%d\n", ans);
	}
	return 0;
}