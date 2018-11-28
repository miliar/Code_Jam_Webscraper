#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1024;

char a[MAXN][MAXN];
char b[MAXN][MAXN];

char d[4][2] = { {-1, 1}, {0, 1}, {1, 1}, {1, 0} };

bool hasRow(int n, int k, char player) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int t = 0; t < 4; t++) {
				int ti = i, tj = j;
				bool found = true;
				for (int p = 0; p < k; p++) {
					if (ti < 0 || ti >= n || tj < 0 || tj >= n || b[ti][tj] != player) {
						found = false;
						break;
					}
					ti += d[t][0];
					tj += d[t][1];	
				}
				if (found) {
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int t;
	freopen("rotate.in", "r", stdin);
	freopen("rotate.out", "w", stdout);
	scanf("%d", &t);
	for (int ti = 0; ti < t; ti++) {
		int n, k;
		scanf("%d%d", &n, &k);

		// Read
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf(" %c", &a[i][j]);
			}
		}

		// Rotate
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				swap(b[i][j], a[n - j - 1][i]);
			}
		}

		// Fall
		for (int j = 0; j < n; j++) {
			int t = n - 1;
			for (int i = n - 1; i >= 0; i--) {
				if (b[i][j] != '.') {
					b[t--][j] = b[i][j];
				}
			}
			for (int i = t; i >= 0; i--) {
				b[i][j] = '.';
			}
		}

		bool red_wins = hasRow(n, k, 'R');
		bool blue_wins = hasRow(n, k, 'B');

		printf("Case #%d: ", ti + 1);
		if (red_wins && blue_wins) {
			printf("Both\n");
		}
		else if (red_wins) {
			printf("Red\n");
		}
		else if (blue_wins) {
			printf("Blue\n");
		}
		else {
			printf("Neither\n");
		}
	}
}
