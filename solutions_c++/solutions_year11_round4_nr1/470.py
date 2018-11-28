#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
using namespace std;

fstream in, out;

int TT;

int x, s, r, n, t;

vector<int> lens;

int main() {
	in.open("proba.in", fstream::in);
	out.open("proba.out", fstream::out);
	out << setprecision(8);
	out << fixed;

	in >> TT;

    for (int i = 0; i < TT; i++) {
		in >> x >> s >> r >> t >> n;
		lens.clear();
		for (int ii = 0; ii < 101; ii++) {
			lens.push_back(0);
		}

		int prevend = 0;
		int bi, ei, wi;
		for (int j = 0; j < n; j++) {
			in >> bi >> ei >> wi;
			lens[0] += bi - prevend;
			lens[wi] += ei - bi;
			prevend = ei;
		}
		lens[0] += x - ei;

		double remtime = t;
		int stop = 101;
		for (int k = 0; k < 101; k++) {
			if (lens[k] >= (r + k + 0.0) * remtime) {
				stop = k;
				break;
			} else {
				remtime -= lens[k] / (r + k + 0.0);
			}
		}

		double ans = 0;
		double timecalc = t;
		for (int l = 0; l < 101; l++) {
			if (l < stop) {
				ans += lens[l] / (r + l + 0.0);
				timecalc -= lens[l] / (r + l + 0.0);
			} else if (l == stop) {
				ans += timecalc + (lens[l] - (r + l + 0.0) * timecalc) / (s + l + 0.0);
			} else {
				ans += lens[l] / (s + l + 0.0);
			}
		}		

		out << "Case #" << i + 1 << ": " << ans << endl;
	}
   
	in.close();
	out.close();

	return 0;
}
