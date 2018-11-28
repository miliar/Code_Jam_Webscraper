#include <algorithm>
#include <assert.h>
#include <stdio.h>
#include <stdint.h>

int C, D;
int P[200];
int V[200];

bool possible(int64_t move) {
	int64_t prev = -1000000000000LL;
	for (int i = 0; i < C; ++i) {
		int64_t left = std::max<int64_t>(prev + D, P[i] - move);
		int64_t right = left + (V[i] - 1) * D;
		if (right - P[i] > move) return false;
		prev = right;
	}
	return true;
}

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		scanf("%d %d", &C, &D);
		D *= 2;
		for (int c = 0; c < C; ++c) scanf("%d %d", &P[c], &V[c]), P[c] *= 2;
		int64_t ub = 0;
		while (!possible(ub)) {
			if (ub == 0) ub = 1;
			else ub <<= 1;
		}
		int solution = -1;
		if (ub == 0) {
			solution = 0;
		}
		else {
			// lo is never possible, hi is always possible
			int lo = ub >> 1;
			int hi = ub;
			while (lo < hi - 1) {
				int mid = lo + (hi - lo) / 2;
				//fprintf(stderr, "> lo,mid,hi = %d,%d,%d\n", lo, mid, hi);
				assert(lo < mid && mid < hi);
				if (possible(mid)) {
					hi = mid;
				}
				else {
					lo = mid;
				}
			}
			solution = hi;
		}
		printf("Case #%d: %.1lf\n", t + 1, (double)solution / 2);
	}
}
