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

int R, k, n;
vector<int> g;

void roller(int& offs, int& sum) {
	int sav = offs;
	sum = 0;
	while (sum+g[offs] <= k) {
		sum += g[offs];
		offs = (offs+1)%n;
		if (offs == sav) break;
	}
}

int main() {
	freopen("C-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		printf("Case #%d: ", test);
		scanf("%d%d%d", &R, &k, &n);
		g.resize(n);
		REP(i, n) scanf("%d", &g[i]);
		int offs = 0;
		int64 sum = 0;
		vector<int> steps(n, -1);
		vector<int64> sums(n);
		int step = 0;
		while (R > 0) {
			if (steps[offs] == -1) {
				steps[offs] = step++;
				sums[offs] = sum;
				int x;
				roller(offs, x);
				sum += x;
				--R;
			} else {
				sum += (sum-sums[offs])*(R/(step-steps[offs]));
				R %= step-steps[offs];
				while (R > 0) {
					int x;
					roller(offs, x);
					sum += x;
					--R;
				}
			}
		}
		printf("%I64d\n", sum);
	}

	exit(0);
}
