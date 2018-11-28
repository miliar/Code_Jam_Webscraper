//============================================================================
// Name        : Round1A2011PartA.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

bool isPossible(size_t n, size_t p_d, size_t p_g) {
	//cout << "HERE" << endl;
	if (p_g == 100 && p_d != 100) return false;
	if (p_d > 0 && p_g == 0) return false;

	for (size_t i = 1; i <= n; ++i) {
		//cout << "HERE" << endl;
		double value = (double)(p_d/100.) * i;
		//cout << "HERE" << endl;
		double intpart = 0;
		if (modf(value, &intpart) == 0.0) {
			//cout << "agaega" << endl;
			return true;
		}
		//cout << "asfsaf" << endl;
	}

	return false;
}

int main() {
	string file_name = "/Users/sameerarya/Documents/CodeJamInput/A-small-attempt0.in.txt";
	ifstream infile(file_name.c_str());
	ofstream outfile("round1apartasampleoutput.txt");
	if (!infile.is_open()) cout << "ERROR" << endl;
	size_t num_cases, n, pd, pg;
	infile >> num_cases;

	for (size_t i = 1; i <= num_cases; ++i) {
		infile >> n;
		infile >> pd;
		infile >> pg;
		//bool ispossible = isPossible(n, pd, pg);
		if (isPossible(n, pd, pg)) outfile << "Case #" << i << ": " << "Possible" << endl;
		else outfile << "Case #" << i << ": " << "Broken" << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}
