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

#define INF 2000000000

ifstream in("input.txt");
ofstream out("output.txt");

int t, n, x;

int main() {
	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		in >> n;
		int m = INF, sum = 0, p = 0;

		for (int i = 0; i < n; ++i) {
			in >> x;
			m = min(m, x);
			sum += x;
			p ^= x;
		}
		out << "Case #" << tt + 1 << ": ";
		if (p != 0) out << "NO\n";
		else out << sum - m << endl;
	}

	return 0;
}
