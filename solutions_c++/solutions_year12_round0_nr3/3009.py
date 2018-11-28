/*
 * googleNumRecycle.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: Danny
 */

#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int isRecycled(int a, int b, int size);

int main(int argc, char* argv[])
{
	/*if(argc < 2)
	{
		cout << "Not enough arguments." << endl;
		return 1;
	}*/

	ifstream fin;
	fin.open("inputfile.txt");

	ofstream fout;
	fout.open("Output.txt");

	if(!fin.is_open())
	{
		cout << "File open failed." << endl;
	}

	int numCases = 0, i, j, k, a, b, numRecycled, size;
	char temp[25];
	fin >> numCases;

	cout << numCases << endl;

	for(i = 0; i < numCases; i++)
	{
		fin >> a;
		fin >> b;

		size = strlen(itoa(a, temp, 10));
		numRecycled = 0;
		fout << "Case #" << i+1 << ": ";

		for(j = a; j < b; j++)
		{
			for(k = j+1; k <=b; k++)
			{
				if(isRecycled(j, k, size))
				{
					numRecycled++;
				}
			}
		}
		fout << numRecycled << endl;

	}

	//isRecycled(1234, 4123, 4);
}

int isRecycled(int a, int b, int size)
{
	int i, j;

	char astr[20];
	char bstr[20];

	char temp;
	itoa(a, astr, 10);
	itoa(b, bstr, 10);

	//cout << astr << endl;
	//cout << bstr << endl;

	for(i = 0; i < size-1; i++)
	{
		temp = astr[0];
		//rotate and compare
		for(j = 0; j < size-1; j++)
		{
			astr[j] = astr[j+1];
		}
		astr[size-1] = temp;

		//cout << astr << " " << bstr << endl;
		if(strcmp(astr, bstr) == 0)
		{
			return 1;
		}
	}

	return 0;
}
