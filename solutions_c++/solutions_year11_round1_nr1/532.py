#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

//#define in cin
//#define out cout

ifstream in("input.txt");
ofstream out("output.txt");

int t;
long long n, d, g;

int main() {
	in >> t;
	for (int tt = 0; tt < t; tt++) {
		out << "Case #" << tt + 1 << ": ";
		in >> n >> d >> g;

		int p = d, q = 100;

		for (int i = 2; i <= 100; ++i) {
			while (!(p % i) && !(q % i)) {
				p /= i;
				q /= i;
			}
		}

		if (q > n || (g == 100 && d != 100) || (g == 0 && d != 0)) out << "Broken\n";
		else out << "Possible\n";
	}


	return 0;
}
