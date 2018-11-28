#include <cstdio>
#include <algorithm>
#define MAXN 1000
using namespace std;

typedef unsigned long long u64;

int main() {
	int T, N, next_g[MAXN];
	u64 R, k;
	u64 g[2*MAXN], s[MAXN];

	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		scanf("%lld%lld%d", &R, &k, &N);
		for(int j = 0; j < N; j++) {
			scanf("%lld", &g[j]);
			g[j+N] = g[j];
		}
		fill(s, s + MAXN, 0);
		for(int j = 0; j < N; j++) {
			int l;
			for(l = 0; l < N && s[j]+g[j+l] <= k; l++) {
				s[j] += g[j+l];
			}
			next_g[j] = (j+l)%N;
		}
		u64 sum = 0;
		int p = 0;
		for(int j = 0; j < R; j++) {
			sum += s[p];
			p = next_g[p];
		}
		printf("Case #%d: %lld\n", i+1, sum);
	}
	return 0;
}
