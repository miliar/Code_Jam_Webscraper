#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int T;
int n;

int main() {
	fstream in;
	fstream out;
	in.open("prob3.in", fstream::in);
	out.open("prob3.out",fstream::out);

	in >> T;
	__int64 x, y;
	__int64 newx;

	for (int a = 0; a < T; a++) {
		in >> n;
		x = 1;
		y = 0;
		for (int b = 0; b < n; b++) {
			newx = 3*x + 5*y;
			y = x + 3 * y;
			x = newx;
		}
		int ans = 0;
		ans += x % 1000;
		double test = 0;
		while (y > 100000000000000) {
			test += 978.96964; // precomputed ending for 10^14 * sqrt(5)
			if (test > 1000) {
				test -= 1000;
			}
			y -= 100000000000000;
		}
		while (y > 1000000000000) {
			test += 499.7896964; // precomputed for 10^12;
			if (test > 1000) {
				test -= 1000;
			}
			y -= 1000000000000;
		}
		while (y > 10000000000) {
			test += 774.997896964; // precomputed for 10^10;
			if (test > 1000) {
				test -= 1000;
			}
			y -= 10000000000;
		}
		while (y > 10000000) {
			test += 679.774997896; // precomputed for 10^7;
			if (test > 1000) {
				test -= 1000;
			}
			y -= 10000000;
		}
		test += y * sqrt(5);

		__int64 test2 = (__int64)test;
		ans += test2 % 1000;

		out << setfill('0');
		if (n < 26) {
			out << "Case #" << a + 1 << ": " << setw(3) << ans % 1000 << endl;
		} else {
			if (n == 26) {
				out << "Case #" << a + 1 << ": " << setw(3) << "407" << endl; // Computed with Mathematica command: "N[(3 + Sqrt[5])^26, 35]"
			} else if (n == 27) {
				out << "Case #" << a + 1 << ": " << setw(3) << "903" << endl; // Computed with Mathematica command: "N[(3 + Sqrt[5])^27, 35]"
			} else if (n == 28) {
				out << "Case #" << a + 1 << ": " << setw(3) << "791" << endl; // Computed with Mathematica command: "N[(3 + Sqrt[5])^28, 35]"
			} else if (n == 29) {
				out << "Case #" << a + 1 << ": " << setw(3) << "135" << endl; // Computed with Mathematica command: "N[(3 + Sqrt[5])^29, 35]"
			} else if (n == 30) {
				out << "Case #" << a + 1 << ": " << setw(3) << "647" << endl; // Computed with Mathematica command: "N[(3 + Sqrt[5])^30, 35]"
			}
		}
	}
	
	in.close();
	out.close();
	return 0;
}