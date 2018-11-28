#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <complex>
using namespace std;
typedef long long ll;

#define PN 16
int _p[PN], _q;
void pblock(int p = _p[_q]) { while (p && !kill(p, 0)) usleep(1e4L); }

int case_x, case_n;
int H, W, D, H2, W2;
int A[512][512];
ll B[1024][1024], C[1024][1024];
ll BY[1024][1024], CY[1024][1024];
ll BX[1024][1024], CX[1024][1024];

int input() {
	scanf("%d%d%d", &H, &W, &D);
	for (int y = 0; y < H; y++)
	 for (int x = 0; x < W; x++) {
		scanf("%01d", &A[y][x]);
		A[y][x] += D;
	}
	return 1;
}

ll area(int x1, int y1, int x2, int y2) {
	return C[y2][x2] - C[y2][x1]
	 - C[y1][x2] + C[y1][x1];
}

complex<ll> sarea(int x1, int y1, int x2, int y2) {
	return complex<ll>(
	 (CX[y2][x2] - CX[y2][x1] - CX[y1][x2] + CX[y1][x1]),
	 (CY[y2][x2] - CY[y2][x1] - CY[y1][x2] + CY[y1][x1]));
}

int solve() {
	pblock();
	H2 = H * 2; W2 = W * 2;
	for (int y = 0; y < H2; y++)
	 for (int x = 0; x < W2; x++) {
		B[y][x] = A[y / 2][x / 2];
		BY[y][x] = A[y / 2][x / 2] * y;
		BX[y][x] = A[y / 2][x / 2] * x;
	}
	for (int y = 1; y <= H2; y++)
	 for (int x = 1; x <= W2; x++) {
		C[y][x] = B[y - 1][x - 1] + C[y - 1][x] + C[y][x - 1] - C[y - 1][x - 1];
		CY[y][x] = BY[y - 1][x - 1] + CY[y - 1][x] + CY[y][x - 1] - CY[y - 1][x - 1];
		CX[y][x] = BX[y - 1][x - 1] + CX[y - 1][x] + CX[y][x - 1] - CX[y - 1][x - 1];
	}
	/*
	for (int y = 0; y < H2; y++) {
		for (int x = 0; x < W2; x++) {
			printf("%d ", area(x, y, x + 1, y + 1));
		}
		puts("");
	}
	*/
	int ans = 0;
	for (int k = 500; 3 <= k; k--) {
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				if (H < y + k || W < x + k) continue;
				complex<ll> axis = sarea(x * 2, y * 2, x * 2 + k * 2, x * 2 + k * 2)
				 - sarea(x * 2, y * 2, x * 2 + 2, y * 2 + 2)
				 - sarea(x * 2, y * 2 + k * 2 - 2, x * 2 + 2, y * 2 + k * 2)
				 - sarea(x * 2 + k * 2 - 2, y * 2, x * 2 + k * 2, y * 2 + 2)
				 - sarea(x * 2 + k * 2 - 2, y * 2 + k * 2 - 2, x * 2 + k * 2, y * 2 + k * 2);
				ll sum = area(x * 2, y * 2, x * 2 + k * 2, x * 2 + k * 2)
				 - area(x * 2, y * 2, x * 2 + 2, y * 2 + 2)
				 - area(x * 2, y * 2 + k * 2 - 2, x * 2 + 2, y * 2 + k * 2)
				 - area(x * 2 + k * 2 - 2, y * 2, x * 2 + k * 2, y * 2 + 2)
				 - area(x * 2 + k * 2 - 2, y * 2 + k * 2 - 2, x * 2 + k * 2, y * 2 + k * 2);
				ll test_sumx = 0, test_sumy = 0, test_sum = 0;
				for (int yy = y; yy < y + k; yy++) {
					for (int xx = x; xx < x + k; xx++) {
						if ((yy == y || yy == y + k - 1) &&
						 (xx == x || xx == x + k - 1)) continue;
						test_sumx += xx * A[yy][xx];
						test_sumy += yy * A[yy][xx];
						test_sum += A[yy][xx];
					}
				}
				//printf("%d,%d,%d: %lld %lld %lld\n", x, y, k, test_sumx, test_sumy, test_sum);
				if (test_sumx * 2 == (2 * x + k - 1) * test_sum &&
				 test_sumy * 2 == (2 * y + k - 1) * test_sum) {
					ans = k;
					goto print_ans;
				}
				/*
				if (axis.real() * 2 == sum * (x * 4 + k * 2 - 1) &&
				 axis.imag() * 2 == sum * (y * 4 + k * 2 - 1)) {
					ans = k;
					goto print_ans;
				}
				/*
				int top_left = area(y * 2, x * 2, y * 2 + 2, x * 2 + 2),
				 top_right = area(y * 2, x * 2 + 2 * k - 2, y * 2 + 2, x * 2 + 2 * k),
				 bottom_left = area(y * 2 + 2 * k - 2, x * 2, y * 2 + 2 * k, x * 2 + 2),
				 bottom_right = area(y * 2 + 2 * k - 2, x * 2 + 2 * k - 2, y * 2 + 2 * k, x * 2 + 2 * k);
				int top_half = area(y * 2, x * 2, y * 2 + k, x * 2 + 2 * k)
				 - top_left - top_right,
				 bottom_half = area(y * 2 + k, x * 2, y * 2 + 2 * k, x * 2 + 2 * k)
				 - bottom_left - bottom_right;
				int left_half = area(y * 2, x * 2, y * 2 + k * 2, x * 2 + k)
				 - top_left - bottom_left,
				 right_half = area(y * 2, x * 2 + k, y * 2 + 2 * k, x * 2 + 2 * k)
				 - top_right - bottom_right;
				if (top_half != bottom_half) continue;
				if (left_half != right_half) continue;
				if (top_half + bottom_half != left_half + right_half) {
					fprintf(stderr, "ERROR! #%d\n", case_x);
				}
				*/
			}
		}
	}
	// Block before writing
print_ans:
	/*
	printf("%d %d\n", W, H);
	for (int y = 0; y < H; y++) {
		for (int x = 0; x < W; x++) {
			printf("%d ", A[y][x]);
		}
		puts("");
	}
	*/
	printf("Case #%d: ", case_x);
	if (ans) printf("%d", ans); else printf("IMPOSSIBLE");
	puts("");
}

int main() {
	int case_n; scanf("%d", &case_n);
	signal(SIGCHLD, SIG_IGN);
	for (case_x = 1; case_x <= case_n; case_x++) {
		input();
		int _r = (_q + 1) % PN;
		pblock(_p[_r]);
		if (_p[_r] = fork()) _q = _r;
		else return solve();
	}
	pblock();
	return 0;
}
