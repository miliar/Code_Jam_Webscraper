// google code soln to C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream inputFile;
ofstream outputFile;

void Print4Digits(int num);
int SolveCurrent(string phrase, int L);

int main()
{
	inputFile.open ("C:\\Documents and Settings\\AnnamariaD\\My Documents\\Visual Studio 2005\\Projects\\google code soln to C\\google code soln to C\\input.txt");
	outputFile.open("C:\\Documents and Settings\\AnnamariaD\\My Documents\\Visual Studio 2005\\Projects\\google code soln to C\\google code soln to C\\output.txt");

	string phrase;
	int L;

	//There are N cases
	int N;
	inputFile >> N;

	getline(inputFile, phrase);

	//For each word (each test case)
	for (int iii=0; iii<N; iii++)
	{
		getline(inputFile, phrase);
		L = phrase.length();

		outputFile << "Case #" << (iii + 1) << ": ";
		Print4Digits( SolveCurrent(phrase, L) );
	}

	inputFile.close();
	outputFile.close();
	return 0;
}

void Print4Digits(int num)
{
	if (num >= 10000)
		num = (num%10000);
	if(num < 1)
		outputFile << "0000" << endl;
	else if (num <10)
		outputFile << "000" << num << endl;
	else if (num < 100)
		outputFile << "00" << num << endl;
	else if (num < 1000)
		outputFile << "0" << num << endl;
	else if (num < 10000)
		outputFile << num << endl;
}

int SolveCurrent(string phrase, int L)
{
	int letterArray [19] = {0};

	//Go through the entire string and accumulate
	for (int iii = 0; iii < L; iii++)
	{
		char c = phrase[iii];
		if (c=='w')
		{
			letterArray [0] ++;
		}
		else if (c == 'e')
		{
			letterArray[1] += letterArray[0];
			letterArray[6] += letterArray[5];
			letterArray[14] += letterArray[13];
		}
		else if (c == 'l')
		{
			letterArray[2] += letterArray[1];
		}
		else if (c == 'c')
		{
			letterArray[3] += letterArray[2];
			letterArray[11] += letterArray[10];
		}
		else if (c == 'o')
		{
			letterArray[4] += letterArray[3];
			letterArray[9] += letterArray[8];
			letterArray[12] += letterArray[11];
		}
		else if (c == 'm')
		{
			letterArray[5] += letterArray[4];
			letterArray[18] += letterArray[17];
		}
		else if (c == ' ')
		{
			letterArray[7] += letterArray[6];
			letterArray[10] += letterArray[9];
			letterArray[15] += letterArray[14];
		}
		else if (c == 't')
		{
			letterArray[8] += letterArray[7];
		}
		else if (c == 'd')
		{
			letterArray[13] += letterArray[12];
		}
		else if (c == 'j')
		{
			letterArray[16] += letterArray[15];
		}
		else if (c == 'a')
		{
			letterArray[17] += letterArray[16];
		}
	}
	return letterArray [18];
}

