// FreeCell Statistics.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int solve(int upper, int dper, int gper) 
{
	if (dper != 100 && gper == 100) {
		return 0;
	}
	if (dper != 0 && gper == 0) {
		return 0;
	}
	if (upper > 100) {
		upper = 100;
	}
	for (int i = 1; i <= upper; ++i) {
		if ( (i * dper) % 100 == 0 ) {
			return 1;
		}
	}
	return 0;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int upper;
		int dper;
		int gper;
		cin >>upper >>dper >>gper;
		int result = solve(upper, dper, gper);
		cout << "Case #" <<curCase << ": " << (result == 0 ? "Broken" : "Possible") <<endl;
	}
}