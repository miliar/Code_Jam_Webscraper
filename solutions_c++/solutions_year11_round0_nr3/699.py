#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

const char *inFile = "C-large-0.in";
const char *outFile = "C-large-0.out";

void solveCase(int caseNum, istream &in, ostream &out) {
    int n, c, xorTotal = 0, sum = 0, minimal = 1000000;
    in >> n;
    for (int i = 0; i < n; ++i) {
	in >> c;
	sum += c;
	xorTotal ^= c;
	minimal = min(c, minimal);
    }
    out << "Case #" << caseNum << ": ";
    if (xorTotal == 0)
	out << (sum - minimal) << endl;
    else
	out << "NO" << endl;
}

int main() {
    ifstream in(inFile);
    ofstream out(outFile);

    int t;
    in >> t;
    for (int i = 1; i <= t; ++i)
	solveCase(i, in, out);

    in.close();
    out.close();

    return EXIT_SUCCESS;
}

