#include <cstdio>
#include <algorithm>

using namespace std;

const int inf = 1<<30;
int cache[123][123], N, S, CAP;

void init() {
	for (int i=0; i<123; i++) {
		for (int j=0; j<123; j++) {
			cache[i][j] = -inf;
		}
	}
	cache[0][0] = 0;
}

int norm(int val) {
	return min((((val-1)/3)+1), val)>=CAP;
}
int supr(int val) {
	return min((((val+1)/3) +1), val)>=CAP;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=1; ti <= t; ti++) {
		init();
		scanf("%d%d%d", &N, &S, &CAP);
		int best = 0;
		for (int i=0; i<N; i++) {
			int ni;
			scanf("%d", &ni);
			//printf("%d or %d\n", (((ni-1)/3)+1), (((ni+1)/3) +1));
			int j = i+1;
			for (int k=S; k>=0; k--) {
				cache[j][k] = max(cache[j][k], cache[j-1][k] + norm(ni));
				if (k) cache[j][k] = max(cache[j][k], cache[j-1][k-1] + supr(ni));
				//printf("cache[%d][%d] = %d\n", j, k, cache[j][k]);
			}
		}
		printf("Case #%d: %d\n", ti, cache[N][S]);
	}
	return 0;
}