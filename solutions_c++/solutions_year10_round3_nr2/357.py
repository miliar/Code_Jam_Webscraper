#include <iostream>
#include <math.h>
using namespace std;

typedef unsigned long long num;
num t, l, p, c;

num get_result() {
	num res = 0;
	while (true) {
		if (l * c >= p) {
			return res;
		} else {
			num cc = c;
			num k1 = 1;
			while (true) {
				num l2 = l * cc;
				double tmp = log(p/(double)l2) / log(c);
				num k2 = log(p/(double)l2) / log(c);
				if (k2 != tmp) {
					k2++;
				}
				if (k2 == k1) {
					break;
				} else if (k2 < k1) {
					cc /= c;
					break;
				}
				cc *= c;
				k1++;
			}
			l = l * cc;
			res++;
		}
	}
	return res;
}

int main() {
	cin >> t;
	for (num i = 0; i < t; i++) {
		cin >> l >> p >> c;
		cout << "Case #" << (i + 1) << ": " << get_result() << "\n";
	}
	cout.flush();
	return 0;
}
