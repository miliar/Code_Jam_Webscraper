#include <iostream>
#include <fstream>
#include "Scores.h"

using namespace std;

int main (int argc, const char * argv[])
{
	int n;
	string temp;
	ifstream inFile("B-small-attempt2.in");
	ofstream outFile("output.txt");
	getline(inFile, temp);
	n = atoi(temp.c_str());

	for (int i = 0; i < n; i++)
	{
		string input;
		getline(inFile,input);
		Scores scores;
		outFile << "Case #"<< i + 1 << ": " << scores.findMaxP(input) << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}