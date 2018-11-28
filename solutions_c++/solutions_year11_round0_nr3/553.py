#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define sz(v)		((int) v.size())
#define fv(v, i)	for (int i = 0; i < sz(v); ++i)
#define fn(n, i)	for (int i = 0; i < n; ++i)

#define FILENAME	"C-large-0"

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int summ = 0, min = 1000001, xsumm = 0, N, c;
		in >> N;
		fn(N, i) {
			in >> c;
			if (c < min) min = c;
			summ += c;
			xsumm ^= c;
		}
		out << "Case #" << test << ": ";
		if (xsumm == 0)
			out << summ - min;
		else
			out << "NO";
		out << endl;
	}

	return 0;
}