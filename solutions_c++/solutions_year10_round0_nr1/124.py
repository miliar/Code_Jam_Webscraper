#include "stdafx.h"

using namespace std;

void PrintUsage(const char* exeName)
{
	cout << "Usage: " << exeName << " infile [outfile]" << endl;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
	{
		PrintUsage(argv[0]);
		return -1;
	}
	string inName = argv[1];
	
	string outName = argc > 2 ? argv[2] : inName + ".out";
	
	ifstream inFile(inName);
	if (!inFile.is_open())
	{
		cout << "Bad input file: " << inName.c_str() << endl;
		return -2;
	}
	ofstream outFile(outName);
	if (!outFile.is_open())
	{
		cout << "Bad output file: " << outName.c_str() << endl;
		return -3;
	}

	int T;
	inFile >> T;
	if (inFile.fail())
	{
		cout << "Bad input data" << endl;
		return -4;
	}
	cout << "Number of cases: " << T;
	for (int i = 1; i <= T; ++i)
	{
		int N; int K;
		inFile >> N >> K;
		if (inFile.fail())
		{
			cout << "Bad input data" << endl;
			return -4;
		}
		int switchPeriod = (1 << N);
		int firstOn = switchPeriod - 1;
		bool isOn = (K & firstOn) == firstOn;
		outFile << "Case #" << i << ": " << (isOn ? "ON" : "OFF") << endl;
	}
	
}
