#include <fstream>
#include <cstring>

using namespace std;

const int NMAX = 128;

int NC, ND;
char C[40][4], D[30][4];

void combina(char Q[], int &NQ) {
	int i;
	for (i = 0; i < NC; ++i) {
		if ((Q[NQ-1] == C[i][0] && Q[NQ-2] == C[i][1]) ||
		  (Q[NQ-2] == C[i][0] && Q[NQ-1] == C[i][1])) {
			Q[NQ---2] = C[i][2];
			return;
		}
	}
}

void distruge(char Q[], int &NQ) {
	bool V[256];
	int i;

	memset(V, 0x00, sizeof(V));

	for (i = 0; i < NQ; ++i) {
		V[(int) Q[i] ] = true;
	}
	for (i = 0; i < ND; ++i) {
		if (V[ (int) D[i][0] ] && V[ (int) D[i][1] ]) {
			NQ = 0;
			return;
		}
	}
}

int main(void) {
	ifstream fin("test.in");
	ofstream fout("test.out");

	char Q[NMAX], S[NMAX];
	int T, ncase, NQ, i, N;

	fin >> T;

	for (ncase = 1; ncase <= T; ++ncase) {
		fin >> NC;
		if (NC)
			for (i = 0; i < NC; ++i)
				fin >> C[i];

		fin >> ND;
		if (ND)
			for (i = 0; i < ND; ++i)
				fin >> D[i];

		fin >> N >> S;

		NQ = 0;
		for (i = 0; i < N; ++i) {
			Q[NQ++] = S[i];

			combina(Q, NQ);
			distruge(Q, NQ);
		}

		fout << "Case #" << ncase << ": [";
		if (NQ) fout << Q[0];
		for (i = 1; i < NQ; ++i) {
			fout << ", " << Q[i];
		}
		fout << "]\n";
	}

	fin.close();
	fout.close();

	return 0;
}
