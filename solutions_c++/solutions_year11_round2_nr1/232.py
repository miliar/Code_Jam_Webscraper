#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

const int NMAX = 128;

int main(void) {

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T, ncase;
	int N, i, j;
	char A[NMAX][NMAX];
	int gamesPlayed[NMAX], gamesWon[NMAX];
	double WP[NMAX], OWP[NMAX], OOWP[NMAX];
	double RPI;

	fin >> T;

	for (ncase = 1; ncase <= T; ++ncase) {
		fin >> N;

		for (i = 0; i < N; ++i) {
			fin >> A[i];
		}

		memset(gamesPlayed, 0x00, sizeof(gamesPlayed));
		memset(gamesWon, 0x00, sizeof(gamesWon));
		memset(OWP, 0x00, sizeof(OWP));
		memset(OOWP, 0x00, sizeof(OOWP));
		for (i = 0; i < N; ++i) {

			for (j = 0; j < N; ++j) {
				if (A[i][j] == '.') continue;
				++gamesPlayed[i];
				if (A[i][j] == '1') ++gamesWon[i];
			}
			WP[i] = (double) gamesWon[i] / gamesPlayed[i];

		}
		for (i = 0; i < N; ++i) {
			for (j = 0; j < N; ++j) {
				if (A[i][j] == '.') continue;
				OWP[i] += (double)(gamesWon[j] - (A[i][j] == '0' ? 1 : 0)) / (gamesPlayed[j] - 1); 
			}
			OWP[i] /= gamesPlayed[i];
		}

		fout << "Case #" << ncase << ":\n";
		for (i = 0; i < N; ++i) {

			for (j = 0; j < N; ++j) {
				if (A[i][j] == '.') continue;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= gamesPlayed[i];

			RPI = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];

			fout << setprecision(10) << RPI << '\n';
		}
	}

	fin.close();
	fout.close();

	return 0;
}
