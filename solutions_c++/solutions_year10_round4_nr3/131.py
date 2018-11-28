#include <algorithm>
#include <map>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

int R, W, H;
int A[128][128], B[128][128];

int solve() {
	scanf("%d", &R);
	memset(A, 0, sizeof(A));
	for (int i = 0; i < R; i++) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int y = y1; y <= y2; y++)
		 for (int x = x1; x <= x2; x++) {
			A[y][x] = 1;
		}
	}
	for (int t = 1;; t++) {
		int sum = 0;
		for (int y = 110; 1 <= y; y--)
		 for (int x = 110; 1 <= x; x--) {
			if (!A[y - 1][x] && !A[y][x - 1]) {
				A[y][x] = 0;
			} else if (A[y - 1][x] && A[y][x - 1]) {
				A[y][x] = 1;
			}
			sum += A[y][x];
		}
		if (!sum) return t;
	}
	return 0;
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int case_x = 1; case_x <= case_n; case_x++)
	 printf("Case #%d: %d\n", case_x, solve());
	return 0;
}
