#include <iostream>
#include <string>
#include <fstream>

using namespace std;

long solve(int R, int k, int N, int* groups) {
	long total = 0;
	int ptr = 0;

	for (int i = 0; i < R; i++) {
		int inRide = 0;
		int groupsCount = 0;

		do {
			if ((inRide + groups[ptr]) <= k) {
				inRide += groups[ptr];
				groupsCount++;
				ptr = (ptr + 1) % N;
			} else {
				break;
			}
		} while (groupsCount < N);
		
		total += inRide;
	}


	return total;
}

int main (int argc, char** argv) {
	if (argc < 2) {
		return 1;
	}

	ifstream fin;
	ofstream fout;
	fin.open(argv[1], ifstream::in);

	string outFilename = argv[1];
	outFilename += ".out";

	fout.open(outFilename.c_str(), ofstream::out);

	int T;
	fin >> T;

	for (int t = 0; t < T; ++t) {
		int R, k, N;

		fin >> R >> k >> N;

		int *groups = new int[N];

		for (int i = 0; i < N; ++i) {
			fin >> groups[i];
		}

		long solution = solve(R,k,N,groups);

		delete[] groups;
		
		cout << "Case #" << (t+1) << ": " << solution << endl;
		fout << "Case #" << (t+1) << ": " << solution << endl;
	}

	fin.close();
	fout.close();

	return 0;
}