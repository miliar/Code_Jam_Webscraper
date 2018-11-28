
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <algorithm>

using namespace std;

int T;
int numA, numB;
vector<int> results;

void getInput(ifstream& inFile, bool first = false) {
	int readValue;

	if (!inFile)
		cout << "file read error" << endl;

	if (first) {
		inFile >> T;
		return;
	}

	inFile >> numA;
	inFile >> numB;
}

int getDigitNumber(int &number) {
	return floor( log10( static_cast<double> (abs( number != 0 ? number : 1 ) ) ) ) + 1;
}

int	shiftNumber(int &number, int digits) {

	int split, rest, first;

	split = pow(static_cast<double>(10), digits-1); 
	rest = number % split;
	first = (number - rest) / split;
	number = rest * 10 + first;
	
	if (number < split)
		return -1;

	return number;
}

int testNumber(int number) {

	vector<int> pairs;
	int shift, count = 0, res;
	int digits = getDigitNumber(number);

	for (int i = 1, shift = number; i < digits; i++) {

		res = shiftNumber(shift, digits);

		if (res == -1)
			continue;

		if (shift > number && shift <= numB) { 
		
			if(find(pairs.begin(), pairs.end(), shift) != pairs.end()) {
				continue;
			}
			count++;
			pairs.push_back(shift);
		}
	}
	return count;
}

int test() {

	int result = 0;

	if (numA < 10 && numB < 10) 
		return 0;

	for (int i = numA; i < numB; i++) {

		result += testNumber(i);
	}
	return result;
}

void showResults() {
	ofstream outFile;
	outFile.open("output.txt");

	for (int i = 0; i < T; i++) {
		outFile << "Case #" << i + 1 << ": " << results[i] << endl;
		cout << "Case #" << i + 1 << ": " << results[i] << endl;
	}

	outFile.close();
}

void main() {

	int result;
	char *inName = "input.txt";
    ifstream inFile(inName);

	getInput(inFile, true);
	
	for (int i = 0; i < T; i++) {

		getInput(inFile);
		result = test();
		results.push_back(result);
	}
	inFile.close();

	showResults();

	getchar();
}