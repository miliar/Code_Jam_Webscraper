#include <stdio.h>
#include <vector>

using std::vector;
typedef long long ll;

int T, R, k, N;
vector<int> g, v;

int main() {
	scanf("%d ", &T);
	for (int t = 1; t <= T; ++ t) {
		scanf("%d %d %d ", &R, &k, &N);
		g.clear();
		v.clear();
		for (int i = 0; i < N; ++ i) {
			int x;
			scanf("%d ", &x);
			g.push_back(x);
		}

		vector<int> end(g.size(), 0);
		vector<ll> money(g.size(), 0L);

		for (int i = 0; i < N; ++ i) {
			ll sum = 0L;
			int j = i;
			int groups = 0;
			do {
				sum += g[j];
				j = (j + 1) % N;
				++ groups;
			} while (groups < N && sum + g[j] <= k);
			end[i] = j;
			money[i] = sum;
		}

		ll e = 0L;
		int p = 0;
		for (int i = 0; i < R; ++ i) {
			e += money[p];
			p = end[p];
		}

		printf("Case #%d: %lld\n", t, e);
	}
	return 0;
}

