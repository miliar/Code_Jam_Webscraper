#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int L, n, c, arr[1002], dis[1000010];
long long t, sum[1000010];

void solve() {
	long long ans = 0;

	scanf("%d%lld%d%d", &L, &t, &n, &c);
	for (int i = 0; i < c; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < n; i++) {
		dis[i] = arr[i % c];
	}
	sum[0] = dis[0];
	for (int i = 1; i < n; i++) {
		sum[i] = sum[i - 1] + dis[i];
	}

	t >>= 1;
	int k = -1;

	vector<long long> last;
	for (int i = 0; i < n; i++) {
		if (t <= sum[i]) {
			k = i;
			last.push_back(sum[i] - t);
			ans += t * 2;
			break;
		}
	}
	for (int i = k + 1; i < n; i++) {
		last.push_back(dis[i]);
	}
	sort(last.begin(), last.end());
	for (int i = last.size() - 1; i >= 0; i--) {
		if (L > 0) {
			--L;
			ans += last[i];
		} else {
			ans += 2 * last[i];
		}
	}
	printf("%lld\n", ans);
	return;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("blarge.out", "w", stdout);
	int nca;
	scanf("%d", &nca);
	for (int ii = 1; ii <= nca; ii++) {
		printf("Case #%d: ", ii);
		solve();
	}
	return 0;
}
