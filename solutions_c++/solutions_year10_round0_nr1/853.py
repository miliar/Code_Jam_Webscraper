#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int64;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)

template<typename T> int size(const T& c) { return int(c.size()); }

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		printf("Case #%d: ", test);
		int n, k;
		scanf("%d%d", &n, &k);
		bool on = true;
		while (n --> 0) {
			if (k%2 == 0) on = false;
			k /= 2;
		}
		printf(on ? "ON\n" : "OFF\n");
	}

	exit(0);
}
