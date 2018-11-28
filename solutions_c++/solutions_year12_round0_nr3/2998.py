#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

string intToString(int integer)
{
	stringstream  ss;
	ss << integer;
	return ss.str();
}

bool isRecyledPair(int n, int m)
{
	string seed = intToString(n);
	string desired = intToString(m);

	if(seed.size() != desired.size())
		return false;

	for(int i=1; i<seed.size(); i++)
	{
		string firstPart = seed.substr(0,i);
		string secondPart = seed.substr(i,seed.size());

		string test = secondPart + firstPart;
		if(atoi(test.c_str()) == m)
			return true;
	}

	return false;
}

typedef struct {
	int A;
	int B;
	int number;
	int reycledPair;
} tracker;

vector<tracker> trackme;

void getRecycledNumbers(int number, vector<int> &recycledNumbers)
{
	string seed = intToString(number);

	for(int i=1; i<seed.size(); i++)
	{
		string firstPart = seed.substr(0,i);
		string secondPart = seed.substr(i,seed.size());

		int recycledNumber = atoi((secondPart + firstPart).c_str());
		
		bool exists = false;

		for(int j=0; j<recycledNumbers.size(); j++)
		{
			if(recycledNumbers[j] == recycledNumber)
			{
				exists = true;
				break;
			}			
		}

		if(!exists)
			recycledNumbers.push_back(recycledNumber);
	}
}

int numRecycledPairs(int number, int lowerBound, int upperBound)
{	
	vector<int> recycledNumbers;
	getRecycledNumbers(number, recycledNumbers);
	int numRecycledPairs = 0;

	for(int i=0; i<recycledNumbers.size(); i++)
	{
		if(number<recycledNumbers[i] && recycledNumbers[i]<=upperBound)
		{
			numRecycledPairs++;
		}
	}

	return numRecycledPairs;
}

int totalNumRecycledPairs(int lowerBound, int upperBound)
{
	int totalPairs = 0;
	for(int i=lowerBound; i<=upperBound; i++)
	{
		totalPairs += numRecycledPairs(i, lowerBound, upperBound);
	}
	return totalPairs;
}

int main(void)
{
	int num_of_testcases = 0;
	vector<int> testcases;
	
	cin >> num_of_testcases;

	for(int i=0; i<num_of_testcases; i++)
	{
		int lowerBound;
		int upperBound;

		cin >> lowerBound >> upperBound;

		testcases.push_back(totalNumRecycledPairs(lowerBound,upperBound));
	}

	for(int i=0; i<testcases.size(); i++)
	{
		cout << "Case #" << i+1 <<  ": " << testcases[i] << endl;
	}

	return 0;
}