#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	string filename;
	cout << "File name: ";
	cin >> filename;
	ifstream in(filename + ".in");
	ofstream out(filename + ".out");

	int T;
	in >> T;
	int N, S, P; // Number of googlers, number of surprising triplets, threshold
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		in >> N >> S >> P;

		int unsurprising = 0;
		int potential = 0;
		for (int i = 0; i < N; i++) {
			int t; //  total pts of a googler
			in >> t;
			if (t >= 3*P - 2)
				unsurprising++;
			else if (P > 1 && t >= 3*P - 4)
				potential++;
		}
		int maximum = unsurprising + min(S, potential);
		out << "Case #" << caseNum << ": " << maximum << endl;
	}
}
