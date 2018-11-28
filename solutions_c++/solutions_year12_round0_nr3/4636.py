/*
 * RecycledNumbers.cpp
 *
 *  Created on: April 14, 2012
 *      Author: Steven Zittrower
 *		For: Google Cup 2012
 */

#include <vector>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool recycled_pair (int n, int m) {
	// Convert to strings
	stringstream ssa;
	stringstream ssb;
	string a, b;
	ssa << n;
	a = ssa.str ();
	ssb << m;
	b = ssb.str ();
	b += b;
	//printf ("a = %s, b = %s\n", a.c_str (), b.c_str ());
	if (b.find (a) != string::npos) {
		return true;
	}
	return false;
}

int main (int argc, char * argv[]) {
	ifstream inputFile;
	string line;
	int tests;
	
	if (argc < 2) {
		printf ("Error: forgot to include a file!\n");
		return -1;
	}
	char *pFilename = argv[1];
	
	inputFile.open (pFilename);
	if (inputFile.is_open ()) {
		getline (inputFile, line); // the number of test cases
		tests = atoi (line.c_str ());
		for (int i = 0; i < tests; i++) { // loop for each test
			vector <string> tokens;
			getline (inputFile, line);
			
			istringstream iss (line); // used to split line
			copy (istream_iterator <string> (iss),
					istream_iterator <string> (),
					back_inserter <vector <string> > (tokens)); // split tokens by space
					
			int A = atoi (tokens[0].c_str ());
			int B = atoi (tokens[1].c_str ());
			int num_recycled = 0;
			for (int n = A; n < B; n++) {
				for (int m = n + 1; m <= B; m++) {
					if (recycled_pair (n, m)) {
						num_recycled++;
					}
				}
			}
			printf ("Case #%d: %d\n", i + 1, num_recycled);
		}
	}
	return 0;
}