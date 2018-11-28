#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int M = 64;

int main() {
	int c, t, n, b, k;
	scanf("%d", &c);
	for (int kase = 0; kase < c; ++kase) {
		scanf("%d%d%d%d", &n, &k, &b, &t);
		int dist[M], vel[M], nswap[M], tmp;
		int canbe[M];
		double time[M];
		vector<int> res;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &tmp);
			dist[i] = b - tmp;
		}
		for (int i = 0; i < n; ++i) {
			scanf("%d", &vel[i]);
			time[i] = (double)dist[i] / vel[i];
		}
		memset(nswap, 0, sizeof(nswap));
		memset(canbe, 0, sizeof(canbe));
		for (int i = 0; i < n; ++i)
			canbe[i] = time[i] <= t + 1e-8;
		for (int i = 0; i < n; ++i) {
			if (!canbe[i]) continue;
			for (int j = i + 1; j < n; ++j) {
				if (!canbe[j]) {
					nswap[i] ++;
				}
			}
			if (canbe[i]) {
				res.push_back(nswap[i]);
			}
		}
		sort(res.begin(), res.end());
		if (res.size() < k) {
			printf("Case #%d: IMPOSSIBLE\n", kase + 1);
		} else {
			int ret = 0;
			for (int i = 0; i < k; ++i)
				ret += res[i];
			printf("Case #%d: %d\n", kase + 1, ret);
		}
	}
	return 0;
}

