#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

namespace gcj {
	using namespace std;

	void solve() {
		int t, n, min_val, sum_val, number, sum_xor;

		scanf("%d", &t);
		for (int i = 0; i < t; i ++) {
			min_val = 1<< 20;
			sum_val = sum_xor = 0;
			scanf(" %d", &n);
			for (int j = 0; j < n; j ++) {
				scanf(" %d", &number);
				sum_xor ^= number;
				sum_val += number;
				min_val = min(min_val, number);
			}

			if (sum_xor)
				printf("Case #%d: NO\n", i + 1);
			else
				printf("Case #%d: %d\n", i + 1, sum_val - min_val);
		}

	}
}



int main () {

	//freopen("d:/GCJ/C-large.in", "r", stdin);
	//freopen("d:/GCJ/C-large.out", "w", stdout);

	gcj::solve();
	return 0;
}