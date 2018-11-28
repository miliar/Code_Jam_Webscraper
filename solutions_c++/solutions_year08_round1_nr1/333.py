#include <string>
#include <list>
#include <fstream>
#include <iostream>

#include "stdio.h"
#include <stdlib.h>

using namespace std;

list<long long> A;
list<long long> B;

void main()
{
	ifstream inFile("c:\\A-large.in");
	ofstream outFile("c:\\out");

	int numberOfCases = 0;	
	long long value = 0;

	inFile >> numberOfCases ;

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		A.clear();
		B.clear();

		long long n;
		inFile >> n ;

		for(int i = 1; i <= n ; i++)
		{
			inFile >> value;
			A.push_back(value);
		}

		for(int i = 1; i <= n ; i++)
		{
			inFile >> value;
			B.push_back(value);
		}

		A.sort();
		B.sort();

		std::list<long long>::iterator it1 = A.begin();
		std::list<long long>::reverse_iterator it2 = B.rbegin();

		value = 0;

		for(int i = 1; i <= n ; i++)
		{
			long long a = *it1;
			long long b = *it2;

			value += a * b;

			it1++;
			it2++;
		}
			

		outFile << "Case #" << caseNumber << ":" << " " << value << endl;
	}
}