#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

#define ABS(x) ((x) > 0 ? (x) : -(x))

int m[1500];
int cost[600][600];

int calc_p(int n) {
	int r = 1;
	for(int i = 0; i < n; ++i) {
		r *= 2;
	}
	return r;
}

int n;
int solve() {
	int res = 0;
	int g = 1;
	int p = calc_p(n);
	for(int i = 0; i < n; ++i) {
		g *= 2;
		for(int j = 0; j < p; j += g) {
			bool buy = false;
			for(int k = 0; k < g; ++k) {
				if (m[j+k] == i) {
					++m[j+k];
					buy = true;
				}
			}
			if (buy == true)
				res += cost[i][j / g];
		}
	}

	return res;
}

int main() {
	freopen("f:/downloads/B-small-attempt0.in", "r", stdin);
	freopen("f:/downloads/output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int z = 0; z < T; ++z) {
		scanf("%d", &n);
		int p = calc_p(n);

		for(int i = 0; i < p; ++i) {
			scanf("%d", &m[i]);
		}

		for(int i = 0; i < n; ++i) {
			p /= 2;
			for(int j = 0; j < p; ++j) {
				scanf("%d", &cost[i][j]);
			}
		}

		printf("Case #%d: %d\n", z + 1, solve());
	}
}
