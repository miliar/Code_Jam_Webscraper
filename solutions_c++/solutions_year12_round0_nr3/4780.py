#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool recycled(int a, int b) {
	stringstream stream1, stream2;
	string j, k;
	int jsize = 0;
	int ksize = 0;

	bool ret = false;

	stream1 << a;
	stream1 >> j;

	stream2 << b;
	stream2 >> k;

	jsize = j.size();
	ksize = k.size();
	if (jsize != ksize) return false;
	if (jsize == 1) return false;
	if (ksize == 1) return false;

	// Let's grab the last X chars of j
	int offset = 1;
	string rebuilt;
	string end = "";
	string start = "";

	for (offset = 1; offset < jsize; offset++) {
		end = j.substr(offset);
		start = j.substr(0,offset);
		rebuilt = "";
		rebuilt.append(end);
		rebuilt.append(start);

		//cout << "Original: " << j << endl;
		//cout << "Rebuilt: " << start << "-" << end << endl;
		//cout << "Compare: " << k << " with the dynamic " << rebuilt << endl;

		if (rebuilt == k) return true;
	}

	return ret;
}

int solve_case(int min, int max) {
	int x = 0, y = 0;
	bool rec;
	int result = 0;

	for ( x = min ; x < max ; x++ ) {
		for ( y = x+1 ; y <= max ; y++ ) {
			if ( x != y ) {
				rec = recycled(x,y);
				if (rec) result++;
			}
		}
	}

	return result;
}

int main(int argc, char* argv[]) {
	// Init vars
	char szInput [256];
	fgets ( szInput, 256, stdin );
	int iCases = atoi(szInput);

	int i = 0;
	for(i = 0; i < iCases; i++) {

		// Get the current line
		string cur_line;
		getline(cin, cur_line);

		// Parse the case parameters
		istringstream iss(cur_line);
		int min, max;
		iss >> min;
		iss >> max;

		// Solve case 
		int res;
		res = solve_case(min,max);

		// Build the output
		cout << "Case #" << (i+1) << ": ";
		cout << res;
		cout << "\n";
	}
}
