#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char a[55][55];
char bb[55][55];
int cntr[4][500], cntb[4][500];

int main()
{
	int T;
	int N, K;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i)
			scanf("%s", a[i]);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				bb[i][j] = a[N - 1 - j][i];
			}
		}
		for (int i = 0; i < N; ++i) {
			int k = N - 1;
			while (bb[k][i] != '.' && k >= 0)
				--k;
			int j = k;
			while (true) {
				while (bb[k][i] != '.' && k >= 0)
					--k;
				while (bb[j][i] == '.' && j >= 0)
					--j;
				if (k >= 0 && j >= 0)
					swap(bb[k][i], bb[j][i]);
				else
					break;
			}
		}
		//for (int i = 0; i < N; ++i) {
		//	for (int j = 0; j < N; ++j) {
		//		putchar(bb[i][j]);
		//	}
		//	puts("");
		//}
		//puts("");
		int resb = 0, resr = 0;
		for (int i = 0; i < N; ++i) {
			int b = 0, r = 0;
			for (int j = 0; j < N; ++j) {
				if (bb[i][j] == 'R') {
					++r;
					b = 0;
					if (r >= K)
						resr = 1;
				}
				else if (bb[i][j] == 'B') {
					++b;
					r = 0;
					if (b >= K)
						resb = 1;
				}
				else {
					b = r = 0;
				}
			}
		}
		for (int i = 0; i < N; ++i) {
			int b = 0, r = 0;
			for (int j = 0; j < N; ++j) {
				if (bb[j][i] == 'R') {
					++r;
					b = 0;
					if (r >= K)
						resr = 1;
				}
				else if (bb[j][i] == 'B') {
					++b;
					r = 0;
					if (b >= K)
						resb = 1;
				}
				else {
					b = r = 0;
				}
			}
		}
		for (int i = 0; i < N; ++i) {
			int b1 = 0, r1 = 0;
			int b2 = 0, r2 = 0;
			int x1 = i, y1 = 0;
			int x2 = x1, y2 = y1;
			for (int j = 0; j < N; ++j) {
				if (x1 >= 0 && x1 < N && y1 >= 0 && y1 < N) {
					if (bb[x1][y1] == 'R') {
						++r1;
						b1 = 0;
						if (r1 >= K)
							resr = 1;
					}
					else if (bb[x1][y1] == 'B') {
						++b1;
						r1 = 0;
						if (b1 >= K)
							resb = 1;
					}
					else {
						b1 = r1 = 0;
					}
				}
				if (x2 >= 0 && x2 < N && y2 >= 0 && y2 < N) {
					if (bb[x2][y2] == 'R') {
						++r2;
						b2 = 0;
						if (r2 >= K)
							resr = 1;
					}
					else if (bb[x2][y2] == 'B') {
						++b2;
						r2 = 0;
						if (b2 >= K)
							resb = 1;
					}
					else {
						b2 = r2 = 0;
					}
				}
				++x1;
				++y1;
				--x2;
				++y2;
				if (y2 >= N)
					break;
			}
		}
		for (int i = 0; i < N; ++i) {
			int b1 = 0, r1 = 0;
			int b2 = 0, r2 = 0;
			int x1 = i, y1 = N - 1;
			int x2 = x1, y2 = y1;
			for (int j = 0; j < N; ++j) {
				if (x1 >= 0 && x1 < N && y1 >= 0 && y1 < N) {
					if (bb[x1][y1] == 'R') {
						++r1;
						b1 = 0;
						if (r1 >= K)
							resr = 1;
					}
					else if (bb[x1][y1] == 'B') {
						++b1;
						r1 = 0;
						if (b1 >= K)
							resb = 1;
					}
					else {
						b1 = r1 = 0;
					}
				}
				if (x2 >= 0 && x2 < N && y2 >= 0 && y2 < N) {
					if (bb[x2][y2] == 'R') {
						++r2;
						b2 = 0;
						if (r2 >= K)
							resr = 1;
					}
					else if (bb[x2][y2] == 'B') {
						++b2;
						r2 = 0;
						if (b2 >= K)
							resb = 1;
					}
					else {
						b2 = r2 = 0;
					}
				}
				++x1;
				--y1;
				--x2;
				--y2;
				if (y2 < 0)
					break;
			}
		}
		printf("Case #%d: ", t);
		if (resb) {
			if (resr) {
				printf("Both\n");
			}
			else {
				printf("Blue\n");
			}
		}
		else {
			if (resr)
				printf("Red\n");
			else
				printf("Neither\n");
		}

	}
	return 0;
}