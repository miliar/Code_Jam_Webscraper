/*
 * main.cpp
 *
 *  Created on: 14.4.2012.
 *      Author: Adnan
 */

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
	int tc, n, s, p, t[100], rem, div, count;

	ifstream in("Input.txt");
	ofstream out("Output.txt");

	if (!in) {
		cout << "Cannot open input file.\n";
		return 1;
	}

	if (!out) {
		cout << "Cannot open output file.\n";
		return 1;
	}

	in >> tc;

	for (int i = 0; i < tc; i++) {
		count = 0;

		in >> n;
		in >> s;
		in >> p;

		for (int j = 0; j < n; j++) {
			in >> t[j];
			div = t[j] / 3;
			rem = t[j] % 3;

			if (div >= p) {
				count++;
			} else if ((div == (p - 2))&&(rem==2) && (s>0) && (p >= 2)) {
				s--;
				count++;
			} else if ((div == (p - 1))&&(rem>=1) && (p >= 1) ) {
				count++;
			} else if ((div == (p - 1))&&(rem==0) && (s>0) && (div >= 1)) {
				s--;
				count++;
			}
		}

		out << "Case #" << i+1 << ": " << count << endl;

	}

	in.close();
	out.close();

	return 0;
}
