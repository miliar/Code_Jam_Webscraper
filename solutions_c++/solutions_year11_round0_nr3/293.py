#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "C"

const int MNOGO = 0x3fffffff;

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		int n;
		scanf("%d", &n);

		int x = 0, sum = 0, mina = MNOGO;
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			x ^= a;
			sum += a;
			mina = min(mina, a);
		}

		if (x != 0) {
			printf("NO");
		}
		else {
			printf("%d", sum - mina);
		}

		printf("\n");
	}

	return 0;
}
