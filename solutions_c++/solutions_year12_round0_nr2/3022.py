#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

bool can_unsurp(int best, int total) {
	total -= best;
	int l = max(0, best-1);
	int r = best;
	return (2*l <= total && total <= 2*r);
}

bool can_surp(int best, int total) {
	if (best < 2) return false;
	total -= best;
	total -= best-2;
	int l = best-2;
	int r = best;
	return (l <= total && total <= r);
}

bool can_unsurp_min(int minbest, int total) {
	while (minbest <= 10) {
		if (can_unsurp(minbest, total)) {
			return true;
		}
		++minbest;
	}
	return false;
}

bool can_surp_min(int minbest, int total) {
	while (minbest <= 10) {
		if (can_surp(minbest, total)) {
			return true;
		}
		++minbest;
	}
	return false;
}

int main() {
	//printf("%d\n", can_unsurp_min(8, 23));

	int tc;
	scanf("%d\n", &tc);
	for (int tt = 1; tt <= tc; ++tt) {
		printf("Case #%d: ", tt);
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);

		int cs = 0, cus = 0, cb = 0;

		for (int i = 0; i < n; ++i) {
			int t;
			scanf("%d", &t);
			bool _cs = can_surp_min(p, t);
			bool _cus = can_unsurp_min(p, t);
			if (_cs && _cus) ++cb;
			else if (_cs) ++cs;
			else if (_cus) ++cus;
		}

		if (cs > s) cs = s;

		printf("%d\n", cs+cus+cb);
	}
}
