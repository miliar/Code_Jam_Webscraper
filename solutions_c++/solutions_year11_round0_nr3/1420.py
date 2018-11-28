#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <list>
#include <cmath>

using namespace std;

void processCase(istream& in, ostream& out)
{
	int n;
	in >> n;
	vector<int> values(n);
	for (int i=0; i<n; i++) in >> values[i];

	int accum = 0;
	int smallest = INT_MAX;
	int sum = 0;
	for (int i=0; i<n; i++) {
		accum ^= values[i];
		smallest = min(values[i], smallest);
		sum += values[i];
	}

	if (accum != 0) {
		out << "NO";
		return;
	}

	out << (sum - smallest);
}

int main()
{
	ifstream in("C-large.in");
	//ostream& out = cout;
	ofstream out("C-large.out", std::ios_base::out);

	int nCases;
	in >> nCases;
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
