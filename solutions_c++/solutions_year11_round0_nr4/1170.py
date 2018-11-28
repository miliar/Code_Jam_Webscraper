#include      <iostream>
#include      <fstream>
#include      <algorithm>

int main(int argc, char **argv) {
	int nTests;
	int nNumbers;
	int anNumber[1000];
	int anNumberSorted[1000];

	std::ifstream in("in");
	std::ofstream out("out");

	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nNumbers;

		for (int i = 0; i < nNumbers; ++i) {
			in >> anNumber[i];
		}

		std::copy(anNumber, anNumber + nNumbers, anNumberSorted);
		std::sort(anNumberSorted, anNumberSorted + nNumbers);

		int nDiff = 0;

		for (int i = 0; i < nNumbers; ++i) {
			if (anNumber[i] != anNumberSorted[i]) {
				++nDiff;
			}
		}

		out << "Case #" << nTest << ": " << nDiff << ".000000" << std::endl;
	}

	in.close();
	out.close();

	return 0;
}
