#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char** argv) {
	if (argc < 2) {
		return 1;
	}

	ifstream fin;
	ofstream fout;
	fin.open(argv[1], ifstream::in);
	fout.open("A.out", ofstream::out);

	int T;
	fin >> T;

	for (int t = 0; t < T; ++t) {
		int N;
		long K;

		fin >> N >> K;

		bool onOff = true;
		for (int i = 0; i < N; ++i) {
			int digit = (K >> i) & 1;

			if (!digit) {
				onOff = false;
				break;
			}
		}

		cout << "Case #" << (t+1) << ": " << (onOff ? "ON" : "OFF") << endl;
		fout << "Case #" << (t+1) << ": " << (onOff ? "ON" : "OFF") << endl;
	}

	fin.close();
	fout.close();

	return 0;
}