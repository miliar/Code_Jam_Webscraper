#include <cstdio>
#include <map>

using namespace std;

int gao(int x) {
	int v = 0, y = x, w = 1;;
	while (x > 0) {
		v++;
		x /= 10;
		w *= 10;
	}
	w /= 10;
	x = y;
	int ret = x;
	for (int i = 0; i < v; ++i) {
		y = x % 10;
		x /= 10;
		x = y * w + x;
		if (y > 0) {
			ret = min(x, ret);
		}
	}
	return ret;
}

int main() {
	int a, b, T;
	scanf("%d", &T);
	map<int, int> cnt;
	for (int re = 1; re <= T; ++re) {
		scanf("%d%d", &a, &b);
		cnt.clear();
		for (int i = a; i <= b; ++i) {
			cnt[gao(i)]++;
		}

		long long ans = 0;
		for (__typeof(cnt.begin()) i = cnt.begin(); i != cnt.end(); ++i) {
			ans += (i->second - 1) * i->second;
		}
		printf("Case #%d: %lld\n", re, ans / 2);
	}

	return 0;
}
