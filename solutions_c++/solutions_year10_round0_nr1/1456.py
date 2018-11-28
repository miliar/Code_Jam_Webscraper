#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

fstream in, out;

int t, n, k;

int main() {
	in.open("prob1.in", fstream::in);
	out.open("prob1.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		in >> n >> k;
		int pow = 1;
		for (int j = 0; j < n; j++) {
			pow *= 2;
		}
		int mod = k % pow;
		if (mod == pow - 1) {
			out << "Case #" << i + 1 << ": ON" << endl;
		} else {
			out << "Case #" << i + 1 << ": OFF" << endl;	
		}
	}
    
	in.close();
	out.close();

	return 0;
}
