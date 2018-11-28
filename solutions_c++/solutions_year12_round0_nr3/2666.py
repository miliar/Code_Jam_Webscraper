#include <cstdio>
#include <algorithm>
using namespace std;

int l, r, is[2000005];

int fn() {
	int gao[10], pow[10], ret = 0;
	pow[0] = 1;
	for (int i = 1; i < 10; ++i)
		pow[i] = pow[i - 1] * 10;
	for (int i = l; i <= r; ++i) {
		int p = -1, q = 0;
		for (int ii = i; ii; ii /= 10)
			gao[++p] = ii % 10;
		int v = i, ans = 0;
		do {
			v = v / 10 + pow[p] * gao[q];
			if (i < v && v <= r) {
				is[ans++] = v;
			}
		} while (++q <= p);
		if (ans) {
			sort(is, is + ans);
			ret += unique(is, is + ans) - is;
		}
	}
	return ret;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int index = 1; index <= t; ++index) {
		scanf("%d%d", &l, &r);
		printf("Case #%d: %d\n", index, fn());
	}
	return 0;
}
