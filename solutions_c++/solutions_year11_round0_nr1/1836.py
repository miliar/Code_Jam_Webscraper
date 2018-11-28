#include <fstream>
#include <cassert>

using namespace std;

const int NMAX = 128;

int sgn(int x) {
	if (x < 0) return -1;
	if (x == 0) return 0;
	return 1;
}

int main(void) {

	ifstream fin("test.in");
	ofstream fout("test.out");

	int T, ncase, i, time, k, pozO, pozB, no, nb;
	int O[NMAX], NO, B[NMAX], NB;
	int N, P[NMAX];
	char C[NMAX], moved;

	fin >> T;

	for (ncase = 1; ncase <= T; ++ncase) {
		fin >> N;

		NO = NB = 0;
		for (i = 0; i < N; ++i) {
			fin >> C[i] >> P[i];
			if (C[i] == 'O') O[NO++] = P[i];
			else B[NB++] = P[i];
		}

		time = 0; k = 0;
		pozO = 1; pozB = 1;
		no = nb = 0;
		do {
			++time; moved = 0;
			if ((C[k] == 'O' && pozO == P[k]) || (C[k] == 'B' && pozB == P[k])) {
				C[k] == 'O' ? ++no : ++nb;
				moved = C[k++];
			}
			if (moved != 'O' && no < NO) {
				pozO += sgn(O[no] - pozO);
			}
			if (moved != 'B' && nb < NB) {
				pozB += sgn(B[nb] - pozB);
			}
		} while (k < N);

		fout << "Case #" << ncase << ": " << time << '\n';
	}

	fin.close();
	fout.close();

	return 0;
}
