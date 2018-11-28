#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
char A[128][128], B[128][128];
vector < pair <int,int> > L;
int m, n;
int live(int i, int j) {
	if (0 <= i && i < m && 0 <= j && j < n && B[i][j] == 1) {
		return 1;
	}
	return 0;
}
int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int R;
		scanf("%d", &R);
		memset(A, 0, sizeof(A));
		L.clear();
		m = 0;
		n = 0;
		for (int r = 0; r < R; r++) {
			int a, b, c, d;
			scanf("%d %d %d %d", &a, &b, &c, &d);
			for (int i = a; i <= c; i++) {
				for (int j = b; j <= d; j++) {
					if (A[i][j] == 0) {
						L.push_back(make_pair(i, j));
					}
					A[i][j] = 1;
				}
			}
			m = max(c+1, m);
			n = max(d+1, n);
		}
		int time;
		for (time = 0; L.size() > 0; time++) {
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					B[i][j] = A[i][j];
					A[i][j] = 0;
				}
			}
			for (int l = 0; l < L.size(); l++) {
				int i = L[l].first;
				int j = L[l].second;
				if (live(i-1, j) || live(i, j-1)) {
					A[i][j] = 1;
				}
				if (live(i-1, j+1)) {
					A[i][j+1] = 1;
				}
			}
			L.clear();
			int nm = 0, nn = 0;
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					if (A[i][j] == 1) {
						L.push_back(make_pair(i, j));
						nm = max(nm, i+1);
						nn = max(nn, j+1);
					}
				}
			}
			m = nm;
			n = nn;
		}
		printf("Case #%d: %d\n", test+1, time);
	}
	return 0;
}
