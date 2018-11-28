// gcj_round_1_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


ifstream in;
ofstream out;

int maxKeyLetters;
int keyNumber;
int alphabetLength;
vector <int> letterFrequency;
int keyPresses;

int caseNumber;

void printData()
{
	out << "Case #" << caseNumber << ": " << keyPresses << endl;
}

void processData()
{
	++caseNumber;
	keyPresses = 0;
	if (alphabetLength > keyNumber*maxKeyLetters)
	{
		out << "Case #" << caseNumber << ": Impossible" << endl;
		return;
	}
	sort(letterFrequency.begin(), letterFrequency.end());
	reverse(letterFrequency.begin(), letterFrequency.end());

	vector<int>::iterator beg = letterFrequency.begin();
	int pressesNeeded = 1;
	int alphabet = 1;
	//for (int j=0; j<letterFrequency.size(); ++j)
	//{
	//	out << letterFrequency[j] << " ";
	//}
	//out << endl;
	while(beg != letterFrequency.end())
	{
		//out << "\tin while" << endl;
		keyPresses += *beg * pressesNeeded;
				if (alphabet>=keyNumber)
		{
			alphabet = 0;
			++pressesNeeded;
		}
		++alphabet;
		++beg;
	}
	printData();

}


void readSingleTest()
{
	in >> maxKeyLetters >> keyNumber >> alphabetLength;
	int freq;
	for (int i=0; i<alphabetLength; ++i)
	{
		//out << "\t\treading frequencies" << endl;
		in >> freq;
		letterFrequency.push_back(freq);
	}
	processData();
	letterFrequency.clear();
}


void readData()
{
	int numberOfTests;
	in >> numberOfTests;

	for (int i=0; i<numberOfTests; ++i)
	{
		readSingleTest();


		//printData();
	}
}


int main()
{
	caseNumber = 0;
	in.open("input.txt");
	out.open("output.txt");
	readData();

	//string s;
	//cin >> s;
	in.close();
	out.close();
	return 0;
}

