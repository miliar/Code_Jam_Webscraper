#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

typedef long long i64;
static std::vector<i64> mins;

i64 gcd(i64 a, i64 b)
{
	if (b == 0) return a;
	return gcd(b, a % b);
}

i64 findMinD(int n)
{
	if (n == 0) return 1;
	if (n == 100) return 1;

	/*
	n = 100 * a / b

	97 = 100 * (9700 / 10000)
	*/

	for (i64 i=1; ; i++) {
		i64 y = i * 100 / n;
		if (i * 100 == n * y) return y;
	}
}

void processCase(istream& in, ostream& out)
{
	i64 N, Pd, Pg;
	in >> N;
	in >> Pd;
	in >> Pg;

	if (Pg == 100 && Pd != 100) {
		out << "Broken";
		return;
	}
	if (Pg == 0 && Pd != 0) {
		out << "Broken";
		return;
	}

	if (mins[Pd] > N) {
		out << "Broken";
		return;
	}

	// Print result
	out << "Possible";
}

int main()
{
	findMinD(50);

	mins.resize(101);
	for (int i=0; i<=100; i++) {
		mins[i] = findMinD(i);
	}

	//ifstream in("input_a.txt");
	//ostream& out = cout;
	ifstream in("A-large.in");
	ofstream out("A-large.out", std::ios_base::out);

	int nCases;
	in >> nCases;
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
