#include <cstdio>
#include <memory.h>

#define MAXN 51

int dx[4] = {0, 1, 1, 1};
int dy[4] = {1, 0, 1, -1};

int T, N, K;

int arr[MAXN][MAXN], low[MAXN], win[2];

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	scanf("%d", &T);
	for (int q = 1; q <= T; q++) {
		scanf("%d %d\n", &N, &K);

		memset(arr, 0, sizeof(arr));

		for (int j = 0; j < N; j++) {
			for (int i = 0; i < N; i++) {
				char c;
				scanf("%c", &c);

				if (c == 'R') {
					arr[N - 1 - j][i] = 1;
				} else
				if (c == 'B') {
					arr[N - 1 - j][i] = -1;
				}
			}
			scanf("\n");
		}

		for (int i = 0; i < N; i++) {
			low[i] = N - 1;
		}
		for (int j = N - 1; j >= 0; j--) {
			for (int i = 0; i < N; i++) {
				if (arr[i][j] != 0 && j != low[i]) {
					arr[i][low[i]] = arr[i][j];
					arr[i][j] = 0;
					low[i]--;
				}
				if (arr[i][j] != 0) {
					low[i]--;
				}
			}
		}
		win[0] = win[1] = 0;

		int xx, yy;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) if (arr[i][j] != 0) {
				for (int k = 0; k < 4; k++) {
					for (int l = 0; l < K; l++) {
						xx = i + l * dx[k],
						   yy = j + l * dy[k];

						if (xx >= N || yy < 0 || yy >= N || arr[xx][yy] != arr[i][j]) break;
						if (l == K - 1) {
							win[(arr[i][j] + 1) >> 1] = 1;
						}
					}
				}
			}
		}

		printf("Case #%d: ", q);
		if (win[0] && win[1]) {
			puts("Both");
		} else
		if (win[1]) {
			puts("Red");
		} else
		if (win[0]) {
			puts("Blue");
		} else {
			puts("Neither");
		}
	}

	return 0;
}

