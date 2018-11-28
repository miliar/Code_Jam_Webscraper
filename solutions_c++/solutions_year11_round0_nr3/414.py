#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

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
			int total;
			in >> total;
			long* array = new long[total];
			for (int i = 0; i < total; i++)
				in >> array[i];
						
			long xorSum = array[0];
			for (int i = 1; i < total; i++)
				xorSum ^= array[i];

			if (!xorSum) {
				sort(array, array + total);
				long maxTotal = 0; 
				for (int i = 1; i < total; i++)
					maxTotal += array[i];
				cout << "Case #" << caseNo++ << ": " << maxTotal << endl;
			} else	
				cout << "Case #" << caseNo++ << ": NO" << endl;
	
			delete array;
		}
	}

	return 0;
}
