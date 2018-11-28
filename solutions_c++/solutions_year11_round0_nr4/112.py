#include <cstdio>
int main() {
	int T, k, N, i, j, a[1010], ans;
	scanf("%d", &T);
	for(k=1;k<=T;k++) {
		scanf("%d", &N);
		ans = 0;
		for(i=0;i<N;i++) {
			scanf("%d", &a[i]);
			if (i != a[i]-1) ans++;
		}
		printf("Case #%d: %.6lf\n", k, double(ans));
	}
	return 0;
}
