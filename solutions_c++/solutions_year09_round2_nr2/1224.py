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

string testOneCase(int testCaseNumber)
{
	string str = testcases[testCaseNumber];
	string::iterator it;
	string::iterator currentMax = str.end()-1;
	string::reverse_iterator rit;
	string::iterator it2;
	
	for (it = str.end() - 1; it>=str.begin(); it--)
	{
		if (*it < *currentMax) // time to swap
		{
			for (it2 = currentMax; (*it2 > *it) && (it2!=str.end()); it2++)
			{
				// do nothing
			}
			char swap = *(it2-1);
			str.erase(it2-1);
			it = str.insert(it,swap);
			
			// sort everything after it
			sort(it+1, str.end());

			return str;
		}
		
		currentMax = it;
	}
	
	// still no return, need add a 0;
	string newString("");
	bool needFirstChar = true;
	

	for (rit = str.rbegin(); rit<str.rend(); rit++)
	{
		if (*rit == '0')
		{
			newString.push_back(*rit);
		}
		
		else if (needFirstChar)
		{
			newString.insert(newString.begin(), *rit);
			newString.push_back('0');
			needFirstChar = false;
		}
		
		else 
		{	
			newString.push_back(*rit);
		}
	}
		
	return newString;
}

void testAll() {
	for (int i=0; i<N; i++)
	{
		outfile << "Case #" << i+1 << ": ";
		outfile << testOneCase(i);
		outfile << endl;
	}
}


int main (int argc, char * const argv[]) {
	infile.open("B-large.in");
	outfile.open("B-large.out");
	
	// Read input
	readNumbers();
	readCases();
	
	// Test all, one by one
	testAll();
	
	infile.close();
	outfile.close();
	
    return 0;
}
