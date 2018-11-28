#include <cstdio>

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) do {} while (0);
#endif

void rotate(int n, char map[][100]) {
	char temp[100][100] = {{}};

	for (int i = 0; i < n; i++) {
		for (int k = 0; k < n; k++)
			temp[i][k] = map[n-k-1][i];
	}

	for (int i = 0; i < n; i++)
		for (int k = 0; k < n; k++)
			map[i][k] = temp[i][k];
}

void solve(const int CASE, int n, int K) {
	char map[100][100] = {{}};
	for (int i = 0; i < n; i++)
		fgets(map[i], 100, stdin);
	rotate(n, map);

	for (int i = n-1; i >= 0; i--) {
		for (int k = 0; k < n; k++) {
			if (map[i][k] == '.') continue;
			int j = i;
			while (j+1 < n && map[j+1][k] == '.') {
				map[j+1][k] = map[j][k];
				map[j][k] = '.';
				j++;
			}
		}
	}
//	for (int i = 0; i < n; i++)
//		D("%s", map[i]);

	bool blue = false;
	bool red = false;

	for (int i = 0; i < n; i++) {
		for (int k = 0; k < n; k++) {
			if (map[i][k] == '.') continue;
			for (int d = 0; d < 4; d++) {
				const int dx[] = {-1, 1, 1, 0};
				const int dy[] = { 1, 0, 1, 1};
				bool win = true;
				for (int len = 0; len < K; len++) {
					int nx = k + dx[d] * len;
					int ny = i + dy[d] * len;
					if (nx >= n || ny >= n) {
						win = false; break;
					}
					if (map[ny][nx] != map[i][k]) {
						win = false;
						break;
					}
				}

				if (win) {
					if (map[i][k] == 'B')
						blue = true;
					if (map[i][k] == 'R')
						red = true;
				}
			}
		}
	}
	printf("Case #%d: ", CASE+1);
	if (red && blue) {
		printf("Both\n");
	} else if (red) {
		printf("Red\n");
	} else if (blue) {
		printf("Blue\n");
	} else {
		printf("Neither\n");
	}
}


int main() {
	// freopen("", "w", stdout);

	int nCases;
	scanf("%d\n", &nCases);

	for (int i = 0; i < nCases; i++) {
		int a, b;
		scanf("%d %d\n", &a, &b);
		solve(i, a, b);
	}

	return 0;
}
