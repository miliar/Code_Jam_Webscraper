#include      <iostream>
#include      <algorithm>
#include      <string>
#include      <fstream>
#include      <list>
#include      <map>

using namespace std;


int main(int argc, char **argv) {
	int nTests;
	long long nLowest, nHighest, nOther;
	bool bCanFind;
	long long nResNote;

	long long anOther[100];

	std::ifstream in("in");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nOther >> nLowest >> nHighest;

		for (long long i = 0; i < nOther; ++i) {
			in >> anOther[i];
		}

		bCanFind = false;

		for (long long nNote = nLowest; nNote <= nHighest && bCanFind == false; ++nNote) {
			bCanFind = true;

			for (long long i = 0; i < nOther && bCanFind; ++i) {
				if ((anOther[i] % nNote) != 0 && (nNote % anOther[i]) != 0) {
					bCanFind =false;
				}
			}

			if (bCanFind == true) {
				nResNote = nNote;
			}
		}

		cout << "Case #" << nTest << ": ";
		if (bCanFind) {
			cout << nResNote << endl;
		}else{
			cout << "NO" << endl;
		}

	}

	in.close();

	return 0;
}
