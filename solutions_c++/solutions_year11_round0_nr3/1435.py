#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	ifstream in("C.in");
	ofstream out("C.out");

	int tests;
	in >> tests;
	for (int test = 1; test <= tests; ++test) {
		out << "Case #" << test << ": ";

		int bin = 0, total = 0, lol = 1000001, cur;
		int candies;
		in >> candies;
		while (candies--) {
			in >> cur;
			lol = min(lol, cur);
			bin ^= cur;
			total += cur;
		}

		if (bin == 0) {
			out << total - lol << endl;
		} else {
			out << "NO" << endl;
		}
	}
}