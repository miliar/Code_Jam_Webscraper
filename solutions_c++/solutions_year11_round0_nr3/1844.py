#include <fstream>

using namespace std;

int main(void) {

	ifstream fin("test.in");
	ofstream fout("test.out");

	int T, ncase;
	int N, v, i, s, min, sum;

	fin >> T;
	for (ncase = 1; ncase <= T; ++ncase) {
		fin >> N;

		fin >> v; min = sum =s = v;
		for (i = 1; i < N; ++i) {
			fin >> v;
			s ^= v; sum += v;
			if (v < min) min = v;
		}

		fout << "Case #" << ncase << ": ";
		if (s != 0)
			fout << "NO\n";
		else
			fout << sum - min << '\n';
	}

	fin.close();
	fout.close();

	return 0;
}
