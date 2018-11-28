#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char** argv) {
	int cases;

	ifstream fin(argv[1]);

	fin >> cases;
	for(int c = 0; c < cases; c++) {
		string input, tmp(20, '0');

		fin >> input;

		tmp.replace(22 - input.size(), input.size(), input);

		next_permutation(tmp.begin(), tmp.end());
		cout << "Case #" << c+1 << ": " << tmp.substr(tmp.find_first_not_of('0')) << endl;
	}

	fin.close();
	return 0;
}
