#include <stdio.h>
#include <string.h>

#define TRACE(x) 

char mat[55][55];
char newmat[55][55];
int N, K;

int D[][2] = {
	{ -1, -1 },
	{ -1, 0 },
	{ -1, 1 },
	{ 0, -1 },
	{ 0, 1 },
	{ 1, -1 },
	{ 1, 0 },
	{ 1, 1 },
};

bool test2(int i, int j, int d, char ch, int k=0) {
	if (k >= K) return true;
	if (i < 0 || i >= N || j < 0 || j >= N) return false;
	if (newmat[i][j] != ch) return false;
	return test2(i+D[d][0], j+D[d][1], d, ch, k+1);
}

char test(int i, int j) {
	for (int d=0; d < 8; d++) {
		if (test2(i, j, d, newmat[i][j])) return newmat[i][j];
	}
	return '.';
}

int main() {
	int _42;
	scanf(" %d", &_42);
	for (int __42=1; __42 <= _42; __42++) {
		scanf(" %d %d", &N, &K);
		for (int i=0; i < N; i++) for (int j=0; j < N; j++) {
			scanf(" %c", &mat[i][j]);
		}

		// rotate
		memset(newmat, '.', sizeof(newmat));
		for (int i=N-1; i >= 0; i--) {
			int k = N-1;
			for (int j=N-1; j >= 0; j--) {
				if (mat[i][j] == '.') continue;

				newmat[k--][N-1-i] = mat[i][j];
			}
		}

#if TRACE(1)+0
		for (int i=0; i < N; i++) {
			for (int j=0; j < N; j++) {
				printf("%c", newmat[i][j]);
			}
			printf("\n");
		}
#endif

		bool red = false, blue = false;
		for (int i=0; i < N; i++) {
			for (int j=0; j < N; j++) {
				if (newmat[i][j] == '.') continue;

				char ret = test(i,j);
				if (ret == 'R') red = true;
				else if (ret == 'B') blue = true;
			}
		}

		printf("Case #%d: ", __42);
		if (red && blue) printf("Both\n");
		else if (!red && !blue) printf("Neither\n");
		else if (red) printf("Red\n");
		else printf("Blue\n");
	}
	return 0;
}
