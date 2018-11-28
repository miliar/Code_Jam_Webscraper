#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
using namespace std;

fstream in, out;

int t, n;

vector<int> primes;

int numdiv(int k, int j) {
	double tempk = k;
	int ret = 0;
	while (tempk >= j) {
		tempk /= (j + 0.0);
		ret++;
	}
	return ret;
}	

int main() {
	in.open("probc.in", fstream::in);
	out.open("probc.out", fstream::out);
 
	in >> t;

	primes.clear();
	for (int ii = 2; ii <= 1001; ii++) {
		bool flag = true;
		for (int jj = 2; jj*jj <= ii; jj++) {
			if (ii % jj == 0 && jj < ii) {
				flag = false;
				break;
			}
		}
		if (flag) {
			primes.push_back(ii);
		}
	}

    for (int i = 0; i < t; i++) {
		in >> n;
		int ans = 0;
		if (n == 1) {
			ans = 0;
		} else {
			for (int j = 0; j < primes.size(); j++) {
				if (primes[j] * primes[j] <= n) {
					ans += numdiv(n, primes[j]) - 1;
				}
			}
			ans += 1;
		}

		out << "Case #" << i + 1 << ": " << ans << endl;
	}
   
	in.close();
	out.close();

	return 0;
}
