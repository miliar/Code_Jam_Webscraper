//============================================================================
// Name        : Recycle.cpp
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

#include <math.h>
#include <map>

using namespace std;

int A, B;
map<pair<int, int>, int > ma;

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

int digitCount(int number)
{
    int digits = 0;
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}

/*
123-231
123 % 100 = 23
123 / 100 = 1
23*10 + 1
123-312
123 % 10 = 3
123 /10 = 12
3 * 100 + 12 = 312
1234-2341
1234 % 1000 = 234
1234 / 1000 = 1
234 * 10 + 1 = 2341
1234-3412
1234 % 100 = 34
1234 / 100 = 12
34 * 100 + 12 = 3412
1234-4123
1234 % 10 = 4
1234 / 10 = 123
4 * 1000 + 123 = 4123
 */
//Returns the best result value based on surprising/non-surprising scores criteria
void algos(int n, int digits) {
	int m, divA, divB, x, y;
	//int recycleCount = 0;
	for(int i = digits - 1; i > 0; --i){
		divA = pow(10, i);
		divB = pow(10, digits - i);
		x = n % divA;
		y = n / divA;
		m = x * divB + y;
		if(m > n && m <= B) {
			//recycleCount++;
			//cout << "n = " << n << " & m = " << m << endl;
			ma[make_pair(n,m)] = 1;
		}
	}
//	return recycleCount;
}

/*
12345, 12345
12345, 23451
12345, 34512
12345, 45123
12345, 51234
10-40
11, 11
12, 21
13, 31
100-532
101, 110
102, 210
103, 310
104, 410
111, 111
112, 121
112, 211
...
123, 231
123, 312
...
312,
355, 535
355, 553
...
415
*/
/*
start with A...till and go until B
case 1: if 1st digit biggest skip
*/
int compute(string& line) {
	vector<int> tokens;
	string delim = " ";
	tokenize(line, tokens, delim);
	vector<int>::iterator iterator = tokens.begin();
	A = tokens[0], B = tokens[1];
	int digits = digitCount(A);
	int nextDigit = pow(10, digits) - A;
	int i;
	for(i = A; i <= B &&  nextDigit--; ++i) {
		algos(i, digits);
	}
	while(i <= B) {
		digits++;
		nextDigit = pow(10, digits) - pow(10, digits -1);
		for(;i <= B &&  nextDigit--; ++i) {
			algos(i, digits);
		}
	}
	return ma.size();
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
			ma.clear();
			getline( ifs, line );
			*output << "Case #" << testCase << ": " << compute(line) << endl;
		}
	}
	output->close();
	return 0;
}
