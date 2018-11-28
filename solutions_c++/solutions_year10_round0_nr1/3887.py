#include <fstream>

using namespace std;

int T, N, K;

int main() {
	ifstream fin ("C:\\A-large.in");
	ofstream fout ("C:\\A-large.out");

	fin >> T;

	for (int casenum = 1; casenum <= T; casenum++) {
		fin >> N;
		fin >> K;

		fout << "Case #" << casenum << ": ";

		if (((K+1) % (int)(pow((double)2,N)))==0) {
			fout << "ON" << endl;
		} else {
			fout << "OFF" << endl;
		}
	}
}