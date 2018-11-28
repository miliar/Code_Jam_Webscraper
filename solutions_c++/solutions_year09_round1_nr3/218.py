#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;


int C;
int N;

double table[42][42];

void construct() {

	for (int x=0; x < 42; x++) {
		for (int y=0; y < 42; y++) {
			table[x][y] = 0;
		}
	}

	table[0][0] = 1;


	for (int x=0; x < C; x++) {
		for (int y=0; y <= N; y++) {
			// We have considered x possible cards
			// We have already struck y overlaps

			// What is the probiability that the next is an overlap?

			double P = ((double)N-y)/(C-x);

			table[x+1][y] += (1 - P) * table[x][y];
			table[x+1][y+1] += (P) * table[x][y];

		}
	}

	for (int y=0; y <= N; y++) {
		for (int x=0; x <= C; x++) {
			//printf("%.4f ", table[x][y]);

		}
		//printf("\n");

	}


}

double E[42];

void calcE() {
	E[C] = 0;

	for (int cih = C-1; cih >= 0; cih--) {

		// E[cih] = sum(ol = 0 .. N  ,  (E[cih+N-ol]+1) * P(cih, ol))

		// E[cih] = (E[cih]+1) * P(cih, N) + sum(ol = 0 .. N  ,  (E[cih+N-ol]+1) * P(cih, ol))

		// E[cih] - (E[cih] * P(cih, N)) = (1) * P(cih, N) + sum(ol = 0 .. N  ,  (E[cih+N-ol]+1) * P(cih, ol))

		// E[cih] * (1 - P(cih, N)) = (1) * P(cih, N) + sum(ol = 0 .. N-1  ,  (E[cih+N-ol]+1) * P(cih, ol))

		E[cih] = table[cih][N];

		for (int ol = 0; ol < N; ol++) {

			if (cih+N-ol <= C)

			E[cih] += table[cih][ol] * (E[cih+N-ol]+1.0);
		}

		//printf("%.8f / %.8f -->\n", E[cih], (1 - table[cih][N]));

		E[cih] /= (1 - table[cih][N]);

		//printf("E[%d] = %.8f\n", cih, E[cih]);

	}
}

int main() {
	FILE* fid = fopen("C-large.in", "r");
	FILE* fout = fopen("C.out", "w");

	int T;

	fscanf(fid, "%d", &T);

	for (int cas = 1; cas <= T; cas++) {
		fscanf(fid, "%d%d", &C, &N);

		//printf("C = %d, N = %d\n", C, N);

		construct();
		calcE();

		fprintf(fout, "Case #%d: %.7f\n", cas, E[0]);

	}

}

