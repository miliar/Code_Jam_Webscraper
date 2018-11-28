#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int* getNewNumbers(int numberCount, int *numbers, int exception)
{
	int *newNumbers = new int[numberCount - 1];
	for (int i = 0; i < exception; i++)
		newNumbers[i] = numbers[i];
	for (int i = exception + 1; i < numberCount; i++)
		newNumbers[i - 1] = numbers[i];
	return newNumbers;
}

int findCountCase(int pCount, int numberCount, int* numbers, int previous, int totalAdd, int totalXor)
{
	int result = -1;
	int sean;
	if (pCount == 1)
	{
		int sDumb;
		int pDumb;
		for (int i = 0; i < numberCount; i++)
		{
			sDumb = totalXor ^ numbers[i];// dumbAdd(numberCount, numbers, i);
			pDumb = previous ^ numbers[i];
			if (sDumb == pDumb)
			{
				sean = totalAdd - numbers[i];// normalAdd(numberCount, numbers, i);
				result = result > sean ? result : sean;
			}
		}
	}
	else
	{
		for (int i = 0; i < numberCount; i++)
		{
			int *newNumbers = getNewNumbers(numberCount, numbers, i);
			sean = findCountCase(pCount - 1, numberCount - 1, newNumbers, previous ^ numbers[i], totalAdd - numbers[i], totalXor ^ numbers[i]);
			delete newNumbers;
			result = result > sean ? result : sean;
		}
	}
	return result == 2000000000 ? -1 : result;
}

inline string toString(int x)
{
   char buf[32];
   _itoa_s( x, buf, 32, 10 );
   return string( buf );
}

int dumbAdd(int numberCount, int* numbers, int exception)
{
	int result = 0;
	for (int i = 0; i < numberCount; i++)
		if (i != exception)
		result = result ^ numbers[i];
	return result;
}

int normalAdd(int numberCount, int* numbers, int exception)
{
	int result = 0;
	for (int i = 0; i < numberCount; i++)
		if (i != exception)
		result += numbers[i];
	return result;
}

string Solve(int numberCount, int* numbers)
{
	int result = -1;
	int sean, totalAdd, totalXor;
	for (int i = 1; i < (numberCount / 2) + 1; i++)
	{
		totalAdd = normalAdd(numberCount, numbers, -1);
		totalXor = dumbAdd(numberCount, numbers, -1);
		sean = findCountCase(i, numberCount, numbers, 0, totalAdd, totalXor);
		if (sean != -1)
			sean = sean > totalAdd - sean ? sean : totalAdd - sean;
		result = result > sean ? result : sean;
	}
	return result == -1 ? "NO" : toString(result);
}

int* split(string line, int numberCount)
{
	int *result = new int[numberCount];
	int currentNumber = 0;
	string number;
	for (int i = 0; i < line.size(); i++)
	{
		if (line[i] == ' ')
		{
			result[currentNumber++] = atoi(number.c_str());
			number = "";
		}
		else
			number += line[i];
	}
	result[numberCount - 1] =  atoi(number.c_str());
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile("C-small-attempt1.in");
	ofstream outfile("C-small-attempt1.out");
	//ifstream infile("input.txt");
	//ofstream outfile("output.txt");
	string line;
	getline(infile, line);
	int cases = atoi(line.c_str());
	int numberCount;
	int *numbers;
	for (int i = 0; i < cases; i++)
	{
		getline(infile, line);
		numberCount = atoi(line.c_str());
		getline(infile, line);
		int *numbers = split(line, numberCount);
		outfile << "Case #" + toString(i + 1) + ": " + Solve(numberCount, numbers) << endl;
		delete numbers;
	}
	outfile.close();
	return 0;
}