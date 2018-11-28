#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cctype>

using std::cout;
using std::endl;
using std::ios;
using std::ifstream;
using std::string;
using std::stringstream;
using std::getline;

int PrintUsage(void);
int FindNumOfRecycledPairs(const int A, const int B);
int FindNumOfRecycledPairs(const int number, const int A, const int B, const int digits);
int GetRecylcledNumber(const int number, const int digits);

static const int TenPowers[] = {
	1, 10, 100, 1000, 10000, 100000, 1000000, 10000000
};

int main(int argc, char* argv[]) {
	if(argc < 2)
		return PrintUsage();

	string filename = argv[1];
	string line;
	int numOfTestCases(0), testCase(1);
	int A(0), B(0);

	ifstream ifs(filename.c_str(), ios::in);
	getline(ifs, line);
	numOfTestCases = atoi(line.c_str());
	
	while(testCase <= numOfTestCases) {
		getline(ifs, line);
		stringstream ss(line);
		ss >> A;
		ss >> B;
		cout << "Case #" << testCase << ": " << FindNumOfRecycledPairs(A, B) / 2 << endl;
		++testCase;
	}
	return 0;
}

int PrintUsage(void) {
	cout << "Usage\n\tRecycledNumbers.exe [filename]" << endl;
	return 0;
}

int FindNumOfRecycledPairs(const int A, const int B) {
	int numOfRecycledPairs(0);
	int digits(0);
	while(0 != (A / TenPowers[digits])) {
		++digits;
	}

	for(int i = A; i <= B; ++i)
		numOfRecycledPairs += FindNumOfRecycledPairs(i, A, B, digits);
	return numOfRecycledPairs;
}

int FindNumOfRecycledPairs(const int number, const int A, const int B, const int digits) {
	int recycledPairs(0), count(0);
	int recycled = GetRecylcledNumber(number, digits);
	while(number != recycled) {
		if(recycled >= A && recycled <= B)
			++count;
		recycled = GetRecylcledNumber(recycled, digits);
	}
	return count;
}

int GetRecylcledNumber(const int number, const int digits) {
	return (number * 10 + number / TenPowers[digits - 1]) % TenPowers[digits];
}