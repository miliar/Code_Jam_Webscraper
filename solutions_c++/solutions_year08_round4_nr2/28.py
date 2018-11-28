#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


int main() {
	ifstream fin("B-large.txt");
	ofstream fout("outputb-large.txt");
	int cases;
	fin >> cases;

	long long a;
	long long n, m;

	for (int testcase = 1; testcase <= cases; testcase++) {
		fin >> n >> m >> a;
		a = a;
		if (n * m < a) {
			fout << "Case #" << testcase << ": IMPOSSIBLE" << endl;
			continue;
		}
		long long x, y, x1, y1;
		x = n;
		y = (a-1) / n + 1;
		x1 = x*y - a;
		y1 = 1;
		if (x*y - x1*y1 != a || x1 > x || y1 > y || y > m)
			cout << "here\n";
		fout << "Case #" << testcase << ": 0 0 " << x << ' ' << y1 << ' ' << x1 << ' ' << y << endl;
	}
	return 0;
}
