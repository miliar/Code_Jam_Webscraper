#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


const int R = 1, B = 2;

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N, K;
		scanf("%d %d", &N, &K);

		int tab[N][N], hor[N][N], vert[N][N], diag1[N][N]/* / */, diag2[N][N]/* \ */;
		int line[N];
		bool redWin = false, blueWin = false;

		for (int i = 0; i < N; i++) {
			getchar(); //\n

			for (int j = 0; j < N; j++) {
				char c = getchar();

				switch(c) {
					case '.':
						line[j] = 0;
						break;
					case 'R':
						line[j] = R;
						break;
					case 'B':
						line[j] = B;
						break;
				}

				tab[i][j] = hor[i][j] = vert[i][j] = diag1[i][j] = diag2[i][j] = 0;
			}

			for (int j = N-1, k = N-1; j >= 0; j--) {
				if (line[j] != 0)
					tab[i][k--] = line[j];
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = N-1; j >= 0; j--) {
				if (tab[i][j] == 0) break;
				if ((tab[i][j] == R && redWin) || (tab[i][j] == B && blueWin)) continue;

				// horizontal
				if (j < N-1 && tab[i][j] == tab[i][j+1]) {
					hor[i][j] = hor[i][j+1] + 1;
					if (hor[i][j] == K-1) {
						if (tab[i][j] == R) redWin = true;
						else                blueWin = true;
					}
				}

				// vertical
				if (i > 0 && tab[i][j] == tab[i-1][j]) {
					vert[i][j] = vert[i-1][j] + 1;
					if (vert[i][j] == K-1) {
						if (tab[i][j] == R) redWin = true;
						else                blueWin = true;
					}
				}

				// diagonal '/'
				if (i > 0 && j < N-1 && tab[i][j] == tab[i-1][j+1]) {
					diag1[i][j] = diag1[i-1][j+1] + 1;
					if (diag1[i][j] == K-1) {
						if (tab[i][j] == R) redWin = true;
						else                blueWin = true;
					}
				}

				// diagonal '\'
				if (i > 0 && tab[i][j] == tab[i-1][j-1]) {
					diag2[i][j] = diag2[i-1][j-1] + 1;
					if (diag2[i][j] == K-1) {
						if (tab[i][j] == R) redWin = true;
						else                blueWin = true;
					}
				}
			}
		}

		printf("Case #%d: ", t);
		if (redWin) {
			if (blueWin)
				printf("Both\n");
			else
				printf("Red\n");
		}
		else {
			if (blueWin)
				printf("Blue\n");
			else
				printf("Neither\n");
		}
	}

	return 0;
}
