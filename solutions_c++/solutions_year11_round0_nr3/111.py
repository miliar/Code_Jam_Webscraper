#include <cstdio>
int main() {
	int T, k, N, i, a[1010], xs, sum, min;
	scanf("%d", &T);
	for(k=1;k<=T;k++) {
		scanf("%d", &N);
		xs = sum = 0;
		min = 1010101;
		for(xs=i=0;i<N;i++) {
			scanf("%d", &a[i]);
			xs ^= a[i];
			sum += a[i];
			if (min > a[i]) min = a[i];
		}
		printf("Case #%d: ", k);
		if (xs) printf("NO\n");
		else printf("%d\n", sum - min);
	}
	return 0;
}
