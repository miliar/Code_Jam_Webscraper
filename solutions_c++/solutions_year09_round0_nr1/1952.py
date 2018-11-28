#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int L, D, N;
ifstream infile;
vector<string> words;
vector<string> testcases;
vector<string> testMatrix;

void readNumbers() {
	string firstLine;
	getline(infile, firstLine);
	
	istringstream iss(firstLine);
	iss >> L;
	iss >> D;
	iss >> N;

}

void readWords() {
	string word;
	for (int i=0; i<D; i++)
	{
		getline(infile, word);
		words.push_back(word);
	}	
}

void readCases() {
	string testcase;
	for (int i=0; i<N; i++)
	{
		getline(infile, testcase);
		testcases.push_back(testcase);
	}
}

int testOneCase(int testCaseNumber)
{
	// Construct a matrix for the current testCase
	testMatrix.clear();
	string currentTestCase = testcases[testCaseNumber];
	for (int i=0; i<currentTestCase.length(); i++)
	{
		int start = i;
		if (currentTestCase[i]=='(')
		{
			i++;
			start++;
			while (currentTestCase[i] != ')')
				i++;
			testMatrix.push_back(currentTestCase.substr(start, i-start));
		}
		else
		{
			testMatrix.push_back(currentTestCase.substr(start, 1));
		}
	}
	
	// Now go over the dicitonary to verify each word
	int retval = 0;
	
	for (int i=0; i<D; i++)
	{
		for (int j=0; j<L; j++)
		{
			if (testMatrix[j].find(words[i][j]) == -1) break;
			if (j == L-1) retval++;
		}
	}
	
	return retval;
}

void testAll() {
	for (int i=0; i<N; i++)
	{
		cout << "Case #" << i+1 << ": ";
		cout << testOneCase(i);
		cout <<endl;
	}
}

int main (int argc, char * const argv[]) {
	infile.open("large.in");
	
	// Read input
	readNumbers();
	readWords();
	readCases();
	
	// Test all, one by one
	testAll();
	
	infile.close();
	return 0;
}
