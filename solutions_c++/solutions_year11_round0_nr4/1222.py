#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

int main(int argc, char** argv) {
	char file_name[1024];
	sprintf(file_name, "%s", argv[1]);

	ifstream inFile;

	inFile.open(file_name);
	if(!inFile) {
		cerr << "Error reading input file\n";
		exit(1);
	}

	int total_testcases;
	inFile >> total_testcases;

	for(int i = 0; i < total_testcases; ++i) {

		double hits = 0.0;;
		int vals, tmp;
		// Create the number list
		inFile >> vals;
		vector<int> numlist;
		for(int v = 0; v < vals; ++v) {
			inFile >> tmp;
			numlist.push_back(tmp);

			if (v + 1 != tmp)
				++hits;
			//hits += abs(v - tmp + 1);
		}

		cout << "Case #" << i+1 << ": " ;
		printf("%f", hits); // FIXME	
		cout << endl;
	}	
}
