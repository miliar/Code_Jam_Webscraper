#include <cstdio>
#include <memory.h>
#include <cassert>

#define MAXN 1000


int gr[MAXN], next[MAXN], cost[MAXN], was[MAXN];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int q = 1; q <= T; q++) {
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &gr[i]);
		}

		for (int i = 0; i < N; i++) {
			int now = 0;
			int j = i;
			do {
				if (now + gr[j] > k) break;
				now += gr[j];
				j = (j + 1) % N;
			} while (j != i);

			next[i] = j;
			cost[i] = now;
			assert(cost[i] <= k);
		}

		long long ans = 0;
		memset(was, 0, sizeof(was));
			
		int i = 0, t = 1;
		while (!was[i]) {
			was[i] = t++;

			ans += cost[i];
			i = next[i];

			R--;
			if (R == 0) break;
		}

		int v = i;
		int cyclen = 0;
		long long cyccost = 0;
		do {
			cyccost += cost[i];
			assert(cyccost < 1e18);
			cyclen++;
			i = next[i];
		} while (i != v);

		ans += cyccost * (R / cyclen);
		R %= cyclen;

		while (R > 0) {
			ans += cost[i];
			R--;
			i = next[i];
		}
		assert(ans < 1e18);

		printf("Case #%d: %Ld\n", q, ans);
	}


}	
