#include <fstream>

using namespace std;

/*
Input

The first line of the input gives the number of test cases, T. T lines follow. 
Each line contains 3 integers -- N, PD and PG.

Output

For each test case, output one line containing "Case #x: y", 
where x is the case number (starting from 1) and y is either "Possible" or "Broken".
*/

int gcd(int a, int b) {
	if (a == 0) 
		return b;
	return 
		gcd(b%a, a);
}

void Find(int p, int& a1, int& a2) {
	a1 = p;
	a2 = 100 - p;
	int d = gcd(a1, a2);
	a1 /= d;
	a2 /= d;
}

int main() {

	ifstream in("A-large.in");
	ofstream out("out.txt");

	int t;
	in >> t;
	for (int tc = 1; tc <= t; ++tc) {
		long long n;
		int pd, pg, d1, d2, g1, g2;
		in >> n >> pd >> pg;
		Find(pd, d1, d2);
		Find(pg, g1, g2);

		bool pos = true;

		if(d1 + d2 > n) {
			pos = false;
		}
		else {
			if ((g1 == 0 && d1 != 0) || (g2 == 0 && d2 != 0))
				pos = false;
		}

		if (pos)
			out << "Case #" << tc << ": Possible" <<  endl;
		else 
			out << "Case #" << tc << ": Broken" <<  endl;
	}
	return 0;
}