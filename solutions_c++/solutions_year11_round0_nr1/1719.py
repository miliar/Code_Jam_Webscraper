#include <fstream>
#include <iostream>
using namespace std;

int main() {
	int T, N, P;
	char R;
	int b_total, o_total;
	int bp, op;
	ifstream is("H:\\temp\\A-large.in");
	is >> T;
	ofstream os("H:\\temp\\A-large.out");
	for (int t = 1; t <= T; t++) {
		bp = op = 1;
		b_total = o_total = 0;
		is >> N;
		for (int n = 0; n < N; n++) {
			is >> R >> P;
			if ('O' == R) {
				int o_time = abs(P - op) + 1;
				if (b_total + 1 < o_total + o_time)
					o_total += o_time;
				else
					o_total = b_total + 1;
				op = P;
			} else if ('B' == R) {
				int b_time = abs(P - bp) + 1;
				if (o_total + 1 < b_total + b_time)
					b_total += b_time;
				else
					b_total = o_total + 1;
				bp = P;
			}
		}
		os << "Case #" << t << ": " << max(b_total, o_total) << endl;
	}
	is.close();
	os.close();
	return 0;
}