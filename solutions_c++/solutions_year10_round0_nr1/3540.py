#include <fstream>

using namespace std;

int main() {
	ifstream fin("A-large.in");
	if (!fin) return 1;
	ofstream fout("A-large.out");
	if (!fout) return 1;

	long n, t, k;
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fin >> n >> k;
		k++;
		if (k % (1 << n) == 0) {
			fout << "Case #" << i << ": ON" << endl;
		}
		else {
			fout << "Case #" << i << ": OFF" << endl;
		}
	}
	return 0;
}

