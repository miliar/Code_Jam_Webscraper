#include <cstdio>
int main() {
	int T;
	long long N;
	int pd, pg;
	scanf("%d", &T);
	for(int t=0;t<T;t++) {
		scanf("%lld%d%d", &N, &pd, &pg);
		printf("Case #%d: ", t+1);
		int m;
		for(m=1;m<=100;m++) {
			if (m * pd % 100 == 0) break;
		}
		if (m > N) {printf("Broken\n"); continue;}
		int twin = m * pd / 100, tlose = m - twin;
		if (twin > 0 && pg == 0) {printf("Broken\n"); continue;}
		if (tlose > 0 && pg == 100) {printf("Broken\n"); continue;}
		printf("Possible\n");
	}
	return 0;
}
