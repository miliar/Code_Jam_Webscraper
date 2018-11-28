#include <cstdlib>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

const char *inFile = "D-large-0.in";
const char *outFile = "D-large-0.out";

void solveCase(int caseNum, istream &in, ostream &out) {
    int n, outOfOrder = 0;
    in >> n;
    for (int i = 1; i <= n; ++i) {
	int c;
	in >> c;
	if (c != i)
	    ++outOfOrder;
    }
    out << "Case #" << caseNum << ": "
	<< fixed << setprecision(6) << static_cast<double>(outOfOrder)
	<< endl;
}

int main() {
    ifstream in(inFile);
    ofstream out(outFile);

    int t;
    in >> t;
    for (int i = 1; i <= t; ++i)
	solveCase(i, in, out);

    return EXIT_SUCCESS;
}

