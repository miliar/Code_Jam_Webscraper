#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int nTC;
int M[105][105];
char hasil[105][105];

const int mr[4] = {-1, 0, 0, 1};
const int mc[4] = {0, -1, 1, 0};

int nrows, ncols;
char nama = 'a', curnama;

inline bool valid (int r, int c) {
	return (r >= 0) && (r < nrows) && (c >= 0) && (c < ncols);
}

void rec (int r, int c) {
	//printf ("%d %d\n", r, c);
	if (hasil[r][c] != 0) {
		curnama = hasil[r][c];
		return;
	}
	int mnr = -1, mnc;
	for (int i = 0; i < 4; i++)
		if (valid (r + mr[i], c + mc[i]) && (mnr == -1 || M[r + mr[i]][c + mc[i]] < M[mnr][mnc]))
			mnr = r + mr[i], mnc = c + mc[i];
	if (mnr == -1 || M[mnr][mnc] >= M[r][c]) {
		curnama = nama;
		nama++;
		hasil[r][c] = curnama;
	} else {
		rec (mnr, mnc);
		hasil[r][c] = curnama;
	}
	//printf ("curnama = %c\n", curnama);
}

int main() {
	int nTC;
	scanf ("%d", &nTC);
	
	for (int tc = 1; tc <= nTC; tc++) {
		printf ("Case #%d:\n", tc);
		scanf ("%d%d", &nrows, &ncols);
		memset (hasil, 0, sizeof (hasil));
		for (int i = 0; i < nrows; i++)
			for (int j = 0; j < ncols; j++)
				scanf ("%d", &M[i][j]);
		nama = 'a';
		for (int i = 0; i < nrows; i++) {
			for (int j = 0; j < ncols; j++) {
				if (j) printf (" ");
				if (!hasil[i][j])
					rec (i, j);
				printf ("%c", hasil[i][j]);
			}
			printf ("\n");
		}
	}
	
	return 0;
}
