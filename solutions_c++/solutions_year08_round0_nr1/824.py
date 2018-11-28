#include <fstream>
#include <string>

using namespace std;

const int QMAX = 1024;
const int SMAX = 128;

int DP[QMAX][SMAX];

int main(void) {
	ifstream fin("large.in");
	ofstream fout("test.out");

	int N, Q, S, R;
	string name[SMAX], query;
	int i, j, k, t;

	fin >> N;

	for (i = 1; i <= N; ++i) {
		fin >> S;

		getline(fin, query);
		memset(DP, 0x3f, sizeof(DP));
		for (j = 0; j < S; ++j) {
			getline(fin, name[j]);
			DP[0][j] = 0;
		}
	
		fin >> Q;
		getline(fin, query);
		for (j = 0; j < Q; ++j) {
			getline(fin, query);

			for (k = 0; k < S; ++k) {
				if (query != name[k])
					DP[j+1][k] = min(DP[j+1][k], DP[j][k]);
				else for (t = 0; t < S; ++t)
					if (k != t) DP[j+1][t] = min(DP[j+1][t], DP[j][k] + 1);
			}
		}

		R = DP[Q][0];
		for (j = 1; j < S; ++j)
			R = min(R, DP[Q][j]);

		fout << "Case #" << i << ": " << R << '\n';
	}

	fin.close();
	fout.close();

	return 0;
}
