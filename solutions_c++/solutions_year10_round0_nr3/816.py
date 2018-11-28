#include <stdio.h>
#include <string.h>

int visit[1000];
long long win[1000];
int gi[1000];

int main() {
	int tc, r, n, k;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d %d %d", &r, &k, &n);
		memset(visit, -1, sizeof(int) * n);
		int rem = k;
		for (int i=0; i<n; ++i) {
			scanf("%d", &gi[i]);
			if (rem >= 0)
				rem -= gi[i];
		}
		if (rem >= 0) {
			printf("%lld\n", ((long long)r) * (k-rem));
			continue;
		}
		int cnt = 0;
		int i = 0;
		long long res = 0;
		int cyclen;
		visit[0] = 0;
		win[0] = 0;
		while(cnt < r) {
			int sum = 0;
			while(sum + gi[i] <= k) {
				sum += gi[i];
				if (++i == n)
					i = 0;
			}
			res += sum;
			++cnt;
			if (visit[i] >= 0) {
				cyclen = cnt - visit[i];
				win[i] = res - win[i];
				break;
			}
			visit[i] = cnt;
			win[i] = res;
		}
		if (cnt < r) {
			r -= cnt;
			int t = r/cyclen;
			res += t * win[i];
			r %= cyclen;
			while(r--) {
				int sum = 0;
				while(sum + gi[i] <= k) {
					sum += gi[i];
					if (++i == n)
						i = 0;
				}
				res += sum;
			}
		}
		printf("%lld\n", res);
	}
	return 0;
}
