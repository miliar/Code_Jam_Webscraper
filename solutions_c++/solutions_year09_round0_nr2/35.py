using namespace std;

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cstdlib>
#include <cstring>

#define FORI(p, X) for (__typeof( (X).begin() ) p = (X).begin(); p != (X).end(); ++p)
#define ALL(X) (X).begin(), (X).end()
#define PB push_back
#define MP make_pair

const int INF = 0x3f3f3f3f;

typedef pair <int, int> PII;
typedef vector <int> VI;
typedef long long lint;

const int NMAX = 128;
const int NDIR = 4;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

char R[NMAX][NMAX];
int A[NMAX][NMAX], N, M, curent;

char go(int i, int j) {
	if (R[i][j]) return R[i][j];
	int k;

	for (k = 0; k < NDIR; ++k) {
		int x, y, t;
		x = i + dx[k];
		y = j + dy[k];

		if (A[x][y] >= A[i][j])
			continue;

		for (t = 0; t < NDIR; ++t) {
			int x1, y1;
			x1 = i + dx[t];
			y1 = j + dy[t];

			if (A[x1][y1] < A[x][y])
				break;
		}

		if (t == NDIR)
			return (R[i][j] = go(x, y));
	}

	return (R[i][j] = 'a' + curent++);
}

int main(void) {
	FILE *fin = fopen("B-large.in", "rt");
	FILE *fout = fopen("output.out", "wt");
	int NCASE, ncase;
	int i, j;

	fscanf(fin, " %d", &NCASE);

	for (ncase = 1; ncase <= NCASE; ++ncase) {

		fscanf(fin, " %d %d", &N, &M);
		curent = 0;

		for (i = 1; i <= N; ++i)
			for (j = 1; j <= M; ++j)
				fscanf(fin, " %d", A[i] + j);

		for (i = 1; i <= N; ++i)
			A[i][0] = A[i][M+1] = INF;
		for (j = 1; j <= M; ++j)
			A[0][j] = A[N+1][j] = INF;

		memset(R, 0x00, sizeof(R));

		for (i = 1; i <= N; ++i)
			for (j = 1; j <= M; ++j)
				if (!R[i][j])
					go(i, j);

		fprintf(fout, "Case #%d:\n", ncase);

		for (i = 1; i <= N; ++i) {
			for (j = 1; j < M; ++j)
				fprintf(fout, "%c ", R[i][j]);
			fprintf(fout, "%c\n", R[i][M]);

		}
	}


	fclose(fin);
	fclose(fout);

	return 0;
}
