#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <list>

using namespace std;

bool checkCyc (string num, int bPos);
bool checkPal (string num);

list<int> cycledNumbers;
int A, B;

int main (void)
{
	cout << "Starting..." << endl;

	//open files
	ifstream inFile ("C-small-attempt0.in");
	ofstream outFile ("C-small-attempt0.out");

	//get number of test cases
	int T;
	inFile >> T;

	for (int t = 1; t <= T; t++)
	{
		cout << "Start case" << endl;
		//get A and B
		
		inFile >> A;
		inFile >> B;

		string mStr;

		stringstream buf;

		int recycleCount = 0;
		int overCount = 0;

		//go through all numbers from A-B
		for (int m = A+1; m <= B; m++)
		{
			buf.clear();
			buf << m;
			buf >> mStr;

			int noDigits = mStr.length();
			int aPos, bPos, a, b;

			cycledNumbers.clear();

			//search through all the digits
			for (aPos = 0, bPos = 1; bPos < noDigits; bPos++)
			{
				if (checkCyc (mStr, bPos))
					recycleCount++;
			}
				
		}

		outFile << "Case #" << t << ": " << recycleCount << endl;
	}

	return 0;
}

bool checkCyc (string num, int bPos)
{
	//cycle the number
	string cycled;

	if (num[bPos] == '0')
		return false;

	for (int i = bPos; i < num.length(); i++)
		cycled += num[i];

	for (int i = 0; i < bPos; i++)
		cycled += num[i];

	int val = atoi(num.c_str());
	int cycVal = atoi(cycled.c_str());

	if (cycVal < val && cycVal >= A)
	{
		list<int>::iterator it;
		for (it = cycledNumbers.begin(); it != cycledNumbers.end(); it++)
		{
			if (*it == cycVal)
				return false;
		}

		cycledNumbers.push_back(cycVal);
		return true;
	}

	return false;
}


