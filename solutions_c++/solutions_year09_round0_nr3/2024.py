#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>

using namespace std;

int N;
ifstream infile;
vector<string> testcases;
ofstream outfile;
string testQuery("welcome to code jam");

void readNumbers() {
	string firstLine;
	getline(infile, firstLine);
	
	istringstream iss(firstLine);
	iss >> N;
}

void readCases() {
	string testcase;
	for (int i=0; i<N; i++)
	{
		getline(infile, testcase);
		testcases.push_back(testcase);
	}
}


int countString(string testCase, string query)
{
	//cout <<"Debug:" << testCase << "::::" << query << endl;
	int retval = 0;
	if (testCase.length() < query.length())
		return 0;
	
	char firstChar = query[0];
	for (int i=0; i<testCase.length(); i++)
	{
		if (testCase[i]==firstChar)
		{
			if (query.length() == 1) {
				retval += 1;
			}
			else {
				retval += countString(testCase.substr(i+1), query.substr(1));
				//cout << retval << "\t";
			}
		}
	}
	
	return retval;
}

int testOneCase(int testCaseNumber)
{
	return countString(testcases[testCaseNumber], testQuery);
}

void testAll() {
	for (int i=0; i<N; i++)
	{
		outfile << "Case #" << i+1 << ": ";
		outfile << setfill('0') << setw(4);
		outfile << testOneCase(i) % 10000;
		outfile << endl;
	}
}


int main (int argc, char * const argv[]) {
	infile.open("C-small-attempt0.in");
	outfile.open("C-small-attempt0.out");
	
	// Read input
	readNumbers();
	readCases();
	
	// Test all, one by one
	testAll();
	
	infile.close();
	outfile.close();
	
    return 0;
}
