#include <fstream>
using namespace std;

int main() {
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");

	int nTestCases;
	fin >> nTestCases;

	for (int testNo = 0; testNo < nTestCases; testNo++) {
		unsigned int devs, toggles;
		fin >> devs >> toggles;

		unsigned int enabledMask = (1u << devs) - 1;

		fout << "Case #" << testNo+1 << ": ";

		if ((toggles & enabledMask) == enabledMask) {
			fout << "ON" << endl;
		} else {
			fout << "OFF" << endl;
		}
	}


	return 0;
}