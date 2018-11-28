#include <stdio.h>
#include <memory.h>
#include <math.h>
#include <set>

using namespace std;

#define FOR(i, n) for (long long i = 0; i < n; i++)
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : (-(x)))


int main() {
	long long T;
	scanf("%d", &T);
	FOR(ca, T) {
		long long N;
		scanf("%d", &N);
		
		long long d[10000], l[10000];
		FOR(i, N)
			scanf("%lld%lld", &d[i], &l[i]);
		long long D;
		scanf("%d", &D);

		printf("Case #%d: ", ca+1);
		
		
		long long f[10000] = {0};
		f[0] = d[0];
		
		for (long long i = 1; i < N; i++) {
			FOR(j, i) {
				if (f[j] + d[j] >= d[i] && MIN(l[i], d[i] - d[j]) > f[i]) {
					f[i] = MIN(l[i], d[i] - d[j]);
//					printf("i,j,d[i],d[j]=%d,%d,%d,%d ", i, j, d[i], d[j]);
				}
			}
		}
		
		FOR(i, N) {
//			printf("[%d] ", f[i]);
			if (d[i] + f[i] >= D) {
	//			printf("%lld %lld %lld\n", d[i], f[i], d[i] + f[i]);
				printf("YES\n");
				goto done;
			}
		}
		
		
		/*
				bool canreach[10000] = {1};
		bool modf = 1;
		while (modf) {
			modf = 0;
			FOR(i, N) {
				if (canreach[i]) {
					if (d[i] + l[i] > D) {
						printf("YES\n");
						goto done;
					}
					FOR(j, N) {
						if (!canreach[j] && ABS(d[i] - d[j]) < MAX(l[i], l[j])) {
							printf("canreach %d\n", j);
							canreach[j] = 1;
							modf = 1;
						}
					}
				}
			}
		}
		*/
		printf("NO\n");
done:;
	}
	
}

