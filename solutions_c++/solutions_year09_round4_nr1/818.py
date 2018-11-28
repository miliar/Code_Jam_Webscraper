#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <cmath>

using namespace std;

typedef vector<int> Rows;

int numNeeded(Rows rows, int accum, int off)
{
	if (rows.size() == 0) {
		return accum;
	} else {
		for (size_t i=0; i<rows.size(); i++) {
			if (rows[i] <= off) {
				rows.erase(rows.begin()+i);
				return numNeeded(rows, accum+i, off+1);
			}
		}
	}
	throw std::exception();
}

void processCase(int lineN, istream& in, ostream& out)
{
	int n;
	in >> n;

	Rows rows(n, -1);

	for (int y=0; y<n; y++) {
		// Read a row
		int rightMost = -1;
		for (int x=0; x<n; x++) {
			char c;
			in >> c;
			if (c == '1')
				rightMost = x;
		}
		rows[y] = rightMost;
	}

	int result = numNeeded(rows, 0, 0);

	// Print result
	out << "Case #" << lineN << ": ";
	out << result;
	out << endl;
}

int main()
{
	ifstream in("A-large.in");
	//ostream& out = cout;
	ofstream out("A-large.out", std::ios_base::out | std::ios_base::binary);

	int nCases;
	in >> nCases;
	char tmp[2];
	in.getline(tmp, 2);
	for (int i=0; i<nCases; i++) {
		processCase(i+1, in, out);
	}

	out.flush();
}
