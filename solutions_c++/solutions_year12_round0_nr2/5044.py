#include <cstdio>

int main() {
	int t, s, p, T, N, i, x[110], avg[110], ans;
	scanf("%d", &T);
	for (t=1;t<=T;t++) {
		scanf("%d %d %d", &N, &s, &p);
		ans = 0;
		for (i=0;i<N;i++) {
			scanf("%d", &x[i]);
			avg[i] = x[i]/3;
			if (x[i]%3) avg[i]++;
			if (avg[i] >= p) ans++;
			else
			if (s) {
				if (x[i]%3 == 0 && x[i]) avg[i]++;
				else if (x[i]%3) avg[i]++;
				if (avg[i] >= p) {
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}