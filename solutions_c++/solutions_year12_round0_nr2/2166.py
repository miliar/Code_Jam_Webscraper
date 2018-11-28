//============================================================================
// Name        : Dancing.cpp
// Author      : Jitesh Nambiar
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

template<class T>
T string_to_digits(std::string& str)
{
	T value;
	std::string parsedStr;
	std::string::const_iterator iterator;
	for(iterator = str.begin(); iterator != str.end(); iterator++)
		if((*iterator) != ',')
			parsedStr += *iterator;
	std::istringstream myFloat(parsedStr);
	myFloat >> value;
	return value;
}

void tokenize(string& str, vector<int>& tokens, const string& delimiters)
{
    size_t lastPos = str.find_first_not_of(delimiters, 0);
    size_t pos = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
    	string temp = str.substr(lastPos, pos - lastPos);
        tokens.push_back(string_to_digits<int>(temp));
        lastPos = str.find_first_not_of(delimiters, pos);
        pos = str.find_first_of(delimiters, lastPos);
    }
}

//Returns the best result value based on surprising/non-surprising scores criteria
int algos(int tpoints, bool surprising) {
	int modulus, leastPt, maxPt;

	/*
	0 % 3 = 0;
	(0 - 3) / 3 = 0;
	1 % 3 = 1;
	(1 - 4) / 3 = -1;
	*/
	if(tpoints < 2)
		return tpoints;

	/*
	2 % 3 = 2;
	(2 - 2) / 3 = 0;
	3 % 3 = 0;
	(3 - 3) / 3 = 0;
	18 % 3 = 0;
	(18 - 3)/ 3 = 5;
	19 % 3 = 1;
	(19 - 4) / 3 = 5;
	20 % 3 = 2;
	(20 - 2) /3 = 6;
	21 % 3 = 0;
	(21 - 3) / 3 = 6;*/
	if(surprising) {
		modulus = tpoints % 3;
		if(modulus < 2) {
			leastPt = (tpoints - (3 + modulus)) / 3;
		} else { //modulus = 2
			leastPt = (tpoints - modulus) / 3;
		}
		maxPt = leastPt +2;
	} else {
		modulus = tpoints % 3;
		maxPt = leastPt = tpoints / 3;
		if(modulus > 0) {
			maxPt = leastPt + 1;
		}
	}
	return maxPt;
}

int compute(string& line) {
	vector<int> tokens;
	string delim = " ";
	tokenize(line, tokens, delim);
	vector<int>::iterator iterator = tokens.begin();
	int N = tokens[0], S = tokens[1], p = tokens[2];

	//sort and start from bottom to find the best result for a surprising score
	sort(tokens.begin()+3, tokens.end());

	int maxGooglers = 0, bestResult;
	for(int i = 3; i < N + 3; ++i) {
		//if surprising triplet score remaining
		if(S) {
			bestResult = algos(tokens[i], true);
			if(bestResult >= p) {
				maxGooglers++;
				S--;
			}
		} else {
			bestResult = algos(tokens[i], false);
			if(bestResult >= p) {
				maxGooglers++;
			}
		}
	}
	return maxGooglers;
}

int main() {
	ofstream* output;
	string filename = "input.in";
	string line;
	std::ifstream ifs(filename.c_str());
	string output_file = "output.op";
	output = new ofstream(output_file.c_str());

	int T = 0, testCase = 1;
	if ( ifs.is_open() ) {
		if( !ifs.eof() ) {
			getline( ifs, line );
			T = string_to_digits<int>(line);
		}
		for(int i = 0; !ifs.eof() && T > 0; i++, testCase++, T-- ) {
			getline( ifs, line );
			*output << "Case #" << testCase << ": " << compute(line) << endl;
		}
	}
	output->close();
	return 0;
}
