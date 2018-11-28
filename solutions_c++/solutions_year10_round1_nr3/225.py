#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <memory>
#include <vector>
#include <string>
#include <set>
#include <map>

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long int64;

int T;

bool win(int a, int b) {
	if (a < b) return win(b, a);

	if (b == 0) return true;

	int p = a / b, q = a % b;
	
	assert(p > 0);

	if (p == 1 && (q > 0 && win(b, q) || q == 0)) return false;

	return true;
}

int64 length(int a, int b) {
	if (a > b) return 0;
	return (b-a+1);
}

int finder(int l, int r, int a) {
	int m, b = -1;

	while (l <= r) {
		m = (l + r) / 2;

		if (!win(m, a)) {
			r = m - 1;
			b = m;
		}
		else {
			l = m + 1;
		}
	}

	return b;
}
             
int main() {
	#ifdef LOCAL
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		cerr << cs << endl;
		printf("Case #%d: ", cs);

		int a1, a2, b1, b2;
		int64 answer = 0;

		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);

		for (int a = a1; a <= a2; a++) {
			int minb = finder((a+2)/2, a, a);

			answer += length(b1, b2) - length(max(b1, minb), min(b2, a+minb-1));
		}

		printf("%I64d", answer);

		printf("\n");
	}

	//int a = 5;
	//scanf("%d", &a);

	//for (int b = 1; b <= 10000; b++) if (!win(a, b)) printf("%d ", b);

	return 0;
}

