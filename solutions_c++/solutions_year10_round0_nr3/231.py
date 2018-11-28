#include <stdio.h>
#include <map>
#include <vector>

using namespace std;

#define LL long long

LL go() {
	int r, k, n;
	LL res = 0;
	scanf("%d%d%d", &r, &k, &n);
	vector<int> a;
	for (int i = 0; i < n; ++i) {
		int tmp;
		scanf("%d", &tmp);
		a.push_back(tmp);
	}
	map<int, LL> profit;
	map<int, int> cnt;
	int pos = 0, i = 0;
	while (r > 0) {
		if (profit.count(pos)) {
			int T = i - cnt[pos];
			LL c = r / T;
			res += c * (res - profit[pos]);
			r %= T;
			break;
		}
		profit[pos] = res;
		cnt[pos] = i;
		--r;
		++i;
		for (int s = 0, z = 0; s + a[pos] <= k && z < n; ++z) {
			s += a[pos];
			res += a[pos];
			pos++;
			if (pos == n) pos = 0;
		}
	}
	while (r > 0) {
		--r;
		for (int s = 0; s + a[pos] <= k; ) {
			s += a[pos];
			res += a[pos];
			pos++;
			if (pos == n) pos = 0;
		}
	}
	return res;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		printf("Case #%d: %lld\n", i+1, go());
}