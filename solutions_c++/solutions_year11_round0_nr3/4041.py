#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int Add(int a, int b);
bool Process(std::vector < int > & candiesVector, int & value, int ii, int p1, int p2, int v1, int v2);

int main(void)
{
	ifstream            input;
	int                 candies   = 0;
	int                 candy     = 0;
	int                 cc        = 0;
	int                 p1        = 0;
	int                 p2        = 0;
	int                 testCase  = 0;
	int                 testCases = 0;
	int                 value     = 0;
	ofstream            output;
	std::vector < int > candiesVector;

	//----------------------------------------------------------------------------------------------
	//  Open the input file.
	//----------------------------------------------------------------------------------------------
	input.open("C-small.in");
	if (false == input.is_open())
	{
		cout << "Unable to open input file!" << endl;
		return 1;
	}

	//----------------------------------------------------------------------------------------------
	//  Open the output file.
	//----------------------------------------------------------------------------------------------
	output.open("C-small.out");
	if (false == output.is_open())
	{
		cout << "Unable to open output file!" << endl;
		input.close();
		return 2;
	}

	//----------------------------------------------------------------------------------------------
	//  Load the input file.
	//----------------------------------------------------------------------------------------------
	input >> testCases;

	//----------------------------------------------------------------------------------------------
	//  Read all the test cases.
	//----------------------------------------------------------------------------------------------
	for (testCase = 1; testCase <= testCases; testCase++)
	{
		//------------------------------------------------------------------------------------------
		//  Read all the candies of the test case.
		//------------------------------------------------------------------------------------------
		candiesVector.erase(candiesVector.begin(), candiesVector.end());
		input >> candies;
		for (candy = 0; candy < candies; candy++)
		{
			input >> cc;
			candiesVector.push_back(cc);
		}

		output << "Case #" << testCase << ": ";
		p1 = 0;
		p2 = 0;
		value = -1;
		Process(candiesVector, value, 0, 0, 0, 0, 0);
		if (-1 == value)
			output << "NO" << endl;
		else
			output << value << endl;
	}

	input.close();
	output.close();

	return 0;
}

bool Process(std::vector < int > & candiesVector, int & value, int ii, int p1, int p2, int v1, int v2)
{
	if (ii >= candiesVector.size())
	{
		if (v1 == v2 && 0 != p1 && 0 != p2)
		{
			if (p1 > value)
				value = p1;
			else if (p2 > value)
				value = p2;

			return true;
		}

		return false;
	}

	Process(candiesVector, value, ii + 1, p1 + candiesVector[ii], p2, Add(v1, candiesVector[ii]), v2);
	Process(candiesVector, value, ii + 1, p1, p2 + candiesVector[ii], v1, Add(v2, candiesVector[ii]));

	return false;
}

int Add(int a, int b)
{
	int aa = a;
	int bb = b;
	aa = a & (~(a & b));
	bb = b & (~(a & b));
	return aa + bb;
}
