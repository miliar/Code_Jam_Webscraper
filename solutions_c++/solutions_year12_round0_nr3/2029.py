// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

int inttodigits(int n, int* out) {
	int pos = 0;

	while (n > 0) {
		out[pos] = n%10;
		n = n/10;
		pos++;
	}

	return pos;
}

int digitstoint(int* input, int ndigits, int offset) {
	int output = 0;
	int multiplier = 1;
	int pos = offset;

	for (int i = 0; i < ndigits; i++) {
		if (pos == ndigits) pos = 0;
		output += input[pos]*multiplier;
		multiplier *= 10;
		pos++;
	}

	return output;
}

bool dupcheck(int* a, int n) {
	for (int i=0; i < 7; i++) {
		if (a[i] == n) return true;
	}
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int testNumber = 1;

	//Eat line specifying total number of testcases
	string input;
	getline(cin, input);
	
	while (cin.good()) {
		string input;
		getline(cin, input);
		//Ignore blank line (at end of file)
		if (input.length() == 0) continue;

		istringstream instream(input);
		
		int a;
		int b;
		instream >> a >> b;
				
		int output = 0;
		int ndigits[7];
			
		for (int n = a; n <= b; n++) {			
			int digitLength = inttodigits(n, ndigits);
			int dups[7];
			for (int j=0; j < 7; j++) dups[j] = 0;

			for (int i = 1; i < digitLength; i++) {				
				int m = digitstoint(ndigits, digitLength, i);				

				if (m > n && m <= b && !dupcheck(dups, m)) {
					//cout<<"("<<n<<","<<m<<")"<<endl;
					dups[i] = m;
					output++;
				}
			}
		}

		cout << "Case #" << testNumber << ": " << output << endl;
		testNumber++;
	}
	
	return 0;
}

