#include <stdio.h>

#define FN "A-large"

FILE* fid;
FILE* fout;


char board[60][60];

int N,K;

static inline int lcheck(int sx, int sy, int dx, int dy, char player) {

	for (int i=0; i < K; i++) {
		if (board[sy+dy*i][sx+dx*i] != player) return 0;
	}
	return 1;

}

// 1 = line exists
int check(char player) {
	int KM = K-1;

	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {

			if (x + KM < N  && lcheck(x,y,1,0,player)) return 1;
			if (y + KM < N && lcheck(x,y,0,1,player)) return 1;
			if (x + KM < N && y + KM < N && lcheck(x,y,1,1,player)) return 1;


			if (x >= KM && y + KM < N && lcheck(x,y,-1,1,player)) return 1;

		}
	}


	return 0;
}


int main(int argc, char** argv) {
	fid = fopen(FN ".in", "r");
	fout = fopen(FN ".out", "w");

	int T;
	fscanf(fid, "%d", &T);

	for (int cas = 1; cas <= T; ++cas) {

		fscanf(fid, "%d %d\n", &N, &K);

		for (int row = 0; row < N; row++) {
			fscanf(fid, "%s", board[row]);


			int egg = N-1;

			for (int col = N-1; col >= 0; --col) {
				if ('.' != board[row][col])
					board[row][egg--] = board[row][col];
			}

			for ( ; egg >= 0; --egg) {
				board[row][egg] = '.';
			}

		}

		//for (int row = 0; row < N; row++) {
		//	printf("{%s}\n", board[row]);
		//}




		int rw = check('R');
		int bw = check('B');


		fprintf(fout, "Case #%d: %s\n", cas, rw ? (bw ? "Both" : "Red") : (bw ? "Blue" : "Neither"));


	}

}
