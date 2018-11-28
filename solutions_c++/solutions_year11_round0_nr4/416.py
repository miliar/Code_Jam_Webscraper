#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;



int main(int argc, char* argv[]) {
	if (argc != 2) {
		cout << "Invalid input parameters!" << endl;
		return -1;
	}

	ifstream in(argv[1]);
	if (in) {
		int count;
		in >> count;
		int caseNo = 1;
		while(count--) {
			int numberTotal;
			in >> numberTotal;
			double numberToSort = 0.0;
			int number;
			for (int i = 0; i < numberTotal; i++) {
				in >> number;
				if (i + 1 != number)
					numberToSort++;
			}
			
			// Tricky rules found in checking D-small results. :P maybe wrong.
			cout << "Case #" << caseNo++ << ": " << setiosflags(ios::fixed) << setprecision(6) << numberToSort << endl;
		}
	}

	return 0;
}
