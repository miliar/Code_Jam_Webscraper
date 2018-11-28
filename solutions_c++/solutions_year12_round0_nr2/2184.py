#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;

int main() {
	ifstream in;
	ofstream out;

	in.open("C:/Users/Jeric Bryle Sy Dy/Downloads/B-large.in");
	out.open("C:/Users/Jeric Bryle Sy Dy/Downloads/B-large.out");

	uint t;
	in >> t;

	for (uint tIter=0; tIter<t; ++tIter) {
		uint n;
		uint s;
		uint p;

		in >> n;
		in >> s;
		in >> p;

		uint cnt = 0;
		uint pot = 0;

		for (uint nIter=0; nIter<n; ++nIter) {
			uint score;
			in >> score;

			uint rem = score % 3;
			uint div = score / 3;

			if (score >= 2) {
				if (div + (rem? 1: 0) >= p) {
					++cnt;
				} else if (rem == 0) {
					if (div + 1 >= p) {
						++pot;
					}
				} else if (rem == 2) {
					if (div + 2 >= p) {
						++pot;
					}
				}
			} else {
				if (score >= p) {
					++cnt;
				}
			}
		}

		out << "Case #" << tIter+1 << ": " << cnt + min(pot, s) << endl;
		//cout << cnt << " - " << pot << endl;
	}

	in.close();
	out.close();
}
