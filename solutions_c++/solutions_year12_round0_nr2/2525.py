#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream in;
	ofstream out;

	in.open("in.txt");
	out.open("out.txt");

	int T, N, S, p;

	in >> T;

	for (int i = 0; i < T; i++) {
		in >> N >> S >> p;

		int p_ = p - 2;
		if (p_ < 0) {
			p_ = 0;
			S = N;
		}
		p += p_ << 1;

		int countS = 0, count = 0;

		for (int j = 0; j < N; j++) {
			int value;

			in >> value;
			if (value >= p + 2) {
				count++;
			} else if (value >= p) {
				countS++;
			}
		}

		if (countS > S) countS = S;
		out << "Case #" << i + 1 << ": " << (countS + count) << endl;
	}
}
