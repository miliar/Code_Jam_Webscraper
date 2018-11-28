// google.cpp : Defines the entry point for the console application.

#include <fstream>
#include <iostream>
#include <math.h>
#include <string>

using namespace std;
int main(int argc, char* argv[])
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("d:/src/google/A-large.in");
	outFile.open("d:/src/google/large.txt");
	int times;
	inFile >> times;

	for (int i = 1; i <= times; ++i)
	{
		int n, k;
		inFile >> n;
		inFile >> k;
		int power = (int) pow(2.0, n);
		string result = ((k % power) == (power - 1)) ? "ON" : "OFF";
		outFile << "Case #" << i << ": " << result << endl;
	}
	return 0;
}

