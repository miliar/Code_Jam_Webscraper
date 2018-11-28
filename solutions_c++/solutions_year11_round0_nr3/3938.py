/*
 *  qualC.cpp
 *  codejam11
 *
 *  Created by Victor Ochikubo on 5/7/11.
 *  Copyright 2011 Stanford University. All rights reserved.
 *
 */


#include <iostream>
#include <sstream>
#include <fstream>

#include <vector>

using namespace std;

const string INFILE = "C-small-attempt0.in";
const string OUTFILE = "C-small-attempt0.out";

void OpenFile(ifstream& input) {
	input.open(INFILE.c_str());
	if (input.fail()) {
		cout << "Error: Couldn't open file." << endl;
	}
}

void OpenOutputFile(ofstream& output) {
	output.open(OUTFILE.c_str());
	if (output.fail()) {
		cout << "Error: Couldn't open output file." << endl;
	}
}

size_t GetNumCases(ifstream& input) {
	stringstream s;
	string str;
	getline(input, str);
	// cout << str << endl; // for testing only, should be a single number
	s << str;
	size_t numCases = 0;
	s >> numCases;
	return numCases;
}

string SizeToString(size_t num) {
	stringstream s;
	s << num;
	return s.str();
}

void ProcessCase(ifstream& input, vector<size_t>& values) {
	string str;
	getline(input, str);
	stringstream s1;
	s1 << str;
	size_t numCandies = 0;
	s1 >> numCandies;
	
	stringstream s2;
	getline(input, str);
	s2 << str;
	
	size_t currVal = 0;
	for (size_t i = 0; i < numCandies; ++i) {
		s2 >> currVal;
		values.push_back(currVal);
	}
	
	/*
	// for testing
	for (size_t i = 0; i < values.size(); ++i) {
		cout << values[i] << " ";
	}
	cout << endl;
	 */
	
}

size_t Recurse(vector<size_t>& values, size_t index, size_t patrickActual, size_t patrickWrong, size_t seanWrong, size_t patrickCount, size_t seanCount) {
	size_t best = 0;
	
	if (index == values.size()) {
		// if sean or patrick has 0 things in his pile, doesn't work as a solution, nonempty piles
		if (patrickCount == 0 || seanCount == 0) return 0;
		if (patrickWrong == seanWrong) return patrickActual;
		else return 0;
	}
	
	size_t currPiece = values[index];
	
	size_t givePatrick = Recurse(values, index + 1, patrickActual + currPiece, patrickWrong ^ currPiece, seanWrong, patrickCount + 1, seanCount);
	size_t giveSean = Recurse(values, index + 1, patrickActual, patrickWrong, seanWrong ^ currPiece, patrickCount, seanCount + 1);
	
	if (givePatrick != 0) best = givePatrick;
	if (giveSean != 0 && giveSean > best)
		best = giveSean;
	
	return best;
	
	// current piece, try it with both sean and patrick
}

size_t RunCase(vector<size_t>& values) {
	size_t best = 0;
	size_t actual = 0;
	size_t patrickWrong = 0, seanWrong = 0;
	size_t patrickCount = 0, seanCount = 0;
	
	size_t index = 0;
	best = Recurse(values, index, actual, patrickWrong, seanWrong, patrickCount, seanCount);
	
	
	return best;
}

void DoOutput(ofstream& output, size_t best, size_t caseNum) {
	output << "Case #" << SizeToString(caseNum) << ": ";
	
	if (best == 0) {
		cout << "NO" << endl;
		output << "NO" << endl;
	}
	else {
		cout << best << endl;
		output << best << endl;
	}
	
}

void DoCase(ifstream& input, ofstream& output, size_t caseNum) {

	vector<size_t> values;
	
	cout << "case # " << caseNum << endl;
	
	ProcessCase(input, values);
	
	size_t best = RunCase(values);
	
	DoOutput(output, best, caseNum);
}

int main() {
	
	ifstream input;
	OpenFile(input);
	ofstream output;
	OpenOutputFile(output);
	
	size_t numCases = GetNumCases(input);
	
	cout << "numCases = " << numCases << endl;
	
	for (size_t i = 0; i < numCases; ++i) {
		DoCase(input, output, i + 1);
	}
	
	
	return 0;
}