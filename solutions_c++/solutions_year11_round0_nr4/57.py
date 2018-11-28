#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
using namespace std;

fstream in, out;

int t, n;

int nums[1000];

int main() {
	in.open("probd.in", fstream::in);
	out.open("probd.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		in >> n;

		for (int j = 0; j < n; j++) {
			in >> nums[j];
		}

		double ans = n + 0.0;
		for (int k = 0; k < n; k++) {
			if (nums[k] == k + 1) {
				ans--;
			}
		}
		
		out << "Case #" << i + 1 << ": ";
		out << setprecision(6);
		out << fixed;
		out << ans << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
