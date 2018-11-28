#include <fstream>
#include <string>
#include <vector>

using namespace std;

#define FILENAME	"A-large-0"

double wp[128], owp[128], oowp[128];
int games[128], wins[128];

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int N;
		in >> N;

		vector<string> table(N);
		for (int i = 0; i < N; ++i)
			in >> table[i];

		for (int i = 0; i < N; ++i) {
			games[i] = 0;
			wins[i] = 0;
			for (int j = 0; j < N; ++j) {
				if (table[i][j] == '1')
					++wins[i];
				if (table[i][j] != '.')
					++games[i];
			}
			wp[i] = wins[i] / (double) games[i];
		}

		for (int i = 0; i < N; ++i) {
			owp[i] = 0;
			for (int j = 0; j < N; ++j) {
				if (table[i][j] != '.')
					owp[i] += (wins[j] - (table[i][j] == '0' ? 1 : 0)) / (double) (games[j] - 1);
			}
			owp[i] /= games[i];
		}

		for (int i = 0; i < N; ++i) {
			oowp[i] = 0;
			for (int j = 0; j < N; ++j) {
				if (table[i][j] != '.')
					oowp[i] += owp[j];
			}
			oowp[i] /= games[i];
		}

		out << "Case #" << test << ":" << endl;
		for (int i = 0; i < N; ++i) {
			out.precision(8);
			out << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << endl;
		}
		out << endl;
	}

	return 0;
}