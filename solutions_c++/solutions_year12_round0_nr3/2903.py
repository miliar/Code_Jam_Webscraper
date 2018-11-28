#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main() {

	int t, a, b, d[1000], c, temp, count;
	ifstream in("input.in");
	ofstream out("output.txt");
	in >> t;
	for (int i = 1; i <= t; i++) {
		in >> a;
		in >> b;
		count = 0;
		if (a == b) {
			out << "Case #" << i << ": " << 0 << endl;
			continue;
		}

		for (int k = a; k <= b; k++) {
			temp = k;
			c = 0;
			while (temp > 0) {
				d[c] = temp % 10;
				c++;
				temp /= 10;
			}

			for (int j = 1; j < c; j++) {
				temp = 0;
				for (int z = 0; z < c; z++)
					temp += d[z]* pow(10.0, (z + j) % c);
				if (temp >= a && temp <= b && temp>k)
					count++;
			}
		}
		out << "Case #" << i << ": " << count << endl;
	}
}
