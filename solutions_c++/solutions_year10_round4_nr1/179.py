#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
using namespace std;
#define FOR(i, n) for (int i = 0; i < (int) (n); i++)


int a[256][256];

int nr(int k, int row)
{
	return (row < k) ? row + 1 : k - (row - k + 1);
}

int start_from[256];

static inline int get(int nk, int k, int si, int sj, int i, int j)
{
	i -= si;
	if (i < 0 || i >= 2 * k - 1) return -1;
	j -= start_from[si + i];
	if (j < 0 || j >= nr(k, i)) return -1;
	return a[i][j];
}

bool ok(int nk, int k, bool print = false)
{
	int dk = nk - k + 1;
	int H = nk * 2 - 1;
	int dH = dk * 2 - 1;
	for (int si = 0; si < dH; si++) {
		for (int sjs = 0; sjs < nr(dk, si); sjs++) {
			int sj = sjs;
			if (si >= dk) sj += si - dk + 1;
			if (si >= nk) sj -= si - nk + 1;
			start_from[si] = sj;
			for (int xi = 1; xi < 2 * k - 1; xi++) {
				start_from[si + xi] = start_from[si + xi - 1];
				if (xi >= k) start_from[si + xi]++;
				if (si + xi >= nk) start_from[si + xi]--;
			}
			bool good = true;
			for (int i = 0; i < nk && good; i++) {
				int L = nr(nk, i);
				for (int j = 0; j < L/2 + L%2 && good; j++) {
					int digit = -1, t;
					t = get(nk, k, si, sj, i, j);
					if (t != -1) digit = t;
					t = get(nk, k, si, sj, i, L - 1 - j);
					if (t != -1) {
						if (digit == -1) digit = t;
						else if (digit != t) { good = false; break; }
					}
					t = get(nk, k, si, sj, H - 1 - i, j);
					if (t != -1) {
						if (digit == -1) digit = t;
						else if (digit != t) { good = false; break; }
					}
					t = get(nk, k, si, sj, H - 1 - i, L - 1 - j);
					if (t != -1) {
						if (digit == -1) digit = t;
						else if (digit != t) { good = false; break; }
					}
					/*
					int t[4] = {
						get(nk, k, si, sj, i, j),
						get(nk, k, si, sj, i, L - 1 - j),
						get(nk, k, si, sj, H - 1 - i, j),
						get(nk, k, si, sj, H - 1 - i, L - 1 - j)
					};
					FOR(ti, 4)
						for (int tj = ti + 1; tj < 4; tj++)
							if (t[ti] >= 0 && t[tj] >= 0 && t[ti] != t[tj]) {
								good = false;
								break;
							}
					*/
				}
			}
			
			if (good) {
				if (print) {
					printf("Good at nk = %d (vs %d), si = %d, sj = %d\n", nk, k, si, sj);
					FOR(i, 2*nk - 1) {
						if (i < nk) FOR(j, nk-i) printf(" ");
						if (i >= nk) FOR(j, i-nk+2) printf(" ");
						FOR(j, nr(nk, i)) {
							int t = get(nk, k, si, sj, i, j);
							if (t == -1) printf("x ");
							else printf("%d ", t);
						}
						printf("\n");
					}
				}
				return true;
			}
		}
	}
	return false;
}

int main(void)
{
	//freopen("a.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		
		int k;
		scanf("%d", &k);
		for (int i = 0; i < k * 2 - 1; i++)
			for (int j = 0; j < nr(k, i); j++)
				scanf("%d", &a[i][j]);
		int nk = k;
		while (1) {
			if (ok(nk, k)) break;
			nk++;
		}
		/*
		int l = k;
		int r = 201;
		while (l != r) {
			int m = (l + r)  / 2;
			if (ok(m, k)) {
				r = m;
			} else l = m + 1;
		}
		ok(l, k, true);*/
		printf("Case #%d: %d\n", tc, nk*nk - k*k);
	}
}
