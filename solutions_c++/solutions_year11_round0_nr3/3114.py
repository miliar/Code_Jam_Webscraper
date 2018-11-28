// codejamtemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>  // I/O 
#include <fstream>   // file I/O
#include <iomanip>   // format manipulation
#include <ios>
#include <string>
#include <sstream>
#include <set>
#include <list>
#include <vector>


#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

using namespace std;

int N;

template<typename RT, typename T, typename Trait, typename Alloc>
RT ss_atoi(const basic_string<T, Trait, Alloc>& the_string)
{
    basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
    RT num;
    temp_ss >> num;
    return num;
}

/*
void Swap(int a, int b, int *arr)
{
	int t = arr[a];
	arr[a] = arr[b];
	arr[b] = t;
}

void Generate(int arr[4], int k)
{
	if (k == N)
	{
		for (int i = 0; i < N; i++)
			outFile << arr[i];
		outFile << " " << endl;
	}
	else
	{
		for (int i = k; i < N; i++)
		{
			Swap(k, i, arr);
			Generate(arr, k + 1);
			Swap(k, i, arr);
		}
	}
}*/


int CalcCorrectInBag(int* bag, set<int> remove)
{
	int res = 0;
	for (int i = 0; i < N; i++)
	{
		set<int>::iterator it = remove.find(i);
		if (it == remove.end())
			res += bag[i];
	}
	return res;
}

int CalcCorrectInRemove(int* bag, set<int> remove)
{
	int res = 0;
	for (int i = 0; i < N; i++)
	{
		set<int>::iterator it = remove.find(i);
		if (it != remove.end())
			res += bag[i];
	}
	return res;
}

vector<int> GetBinary(int a)
{
	vector<int> bin(10);
	int i = 0;
	if (a > 1)
	{
		while (a / 2 >= 1)
		{
			if (i >= bin.capacity())
				bin.resize(i * 2);
			bin[i] = a % 2;
			a = a / 2;
			i++;
		}
	}
	if (i >= bin.capacity())
			bin.resize(i * 2);
	bin[i] = a;
	return bin;
}

int GetDec(vector<int> v)
{
	int res = 0;
	for (int i = 0; i < v.size(); i++)
	{
		res += v[i] * pow(2.0, i);
	}
	return res;
}

int SumNoCarry(int a, int b)
{
	vector<int> longer;
	vector<int> shorter;

	if (a > b)
	{
		longer = GetBinary(a);
		shorter = GetBinary(b);
	}
	else
	{
		longer = GetBinary(b);
		shorter = GetBinary(a);
	}

	for (int i = 0; i < shorter.size(); i++)
	{
		longer[i] = longer[i] ^ shorter[i];
	}

	return GetDec(longer);
}

int CalcNoCarryRemove(int* bag, set<int> remove)
{
	int res = 0;
	for (int i = 0; i < N; i++)
	{
		set<int>::iterator it = remove.find(i);
		if (it != remove.end())
			res = SumNoCarry(res, bag[i]);
	}
	return res;
}

int CalcNoCarryBeg(int* bag, set<int> remove)
{
	int res = 0;
	for (int i = 0; i < N; i++)
	{
		set<int>::iterator it = remove.find(i);
		if (it == remove.end())
			res = SumNoCarry(res, bag[i]);
	}
	return res;
}

int Find(int count, int start, int* bag, set<int> remove)
{
	int maximum = -1;
	for (int i = start; i < N; i++)
	{
		remove.insert(i);
		if (remove.size() == count)
		{// calc values
			int noCarryBag = CalcNoCarryBeg(bag, remove);
			int noCarryRemove = CalcNoCarryRemove(bag, remove);
			if (noCarryBag == noCarryRemove)
			{
				int correctBagValue = CalcCorrectInBag(bag, remove);
				int correctRemValue = CalcCorrectInRemove(bag, remove);
				if (maximum < MAX(correctRemValue, correctBagValue))
					maximum = MAX(correctRemValue, correctBagValue);
			}
		}
		else
		{
			int m = Find(count, i + 1, bag, remove);
			if (m > maximum)
				maximum = m;
		}
		remove.erase(i);
	}
	return maximum;
}

void ProcessCase(int caseIndex, ifstream &inFile, ofstream &outFile)
{
	inFile >> N;
	int *bag = new int[N];
	for (int i = 0; i < N; i++)
	{
		inFile >> bag[i];
	}

	set<int> remove;
	int max = -1;
	for (int i = 1; i <= double(N / 2.0); i++)
	{ //i - candys number to move to other pile
		int v = Find(i, 0, bag, remove);
		if (v > max)
			max = v;
	}
	outFile << "Case #" << caseIndex + 1 << ": ";
	if (max > 0)
		outFile << max;
	else
		outFile << "NO";
	outFile << "\n";
	delete []bag;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	inFile.open("C-small-attempt1.in", ios::in);    // open the streams
	outFile.open("C-small-attempt1.out", ios::out);

	int N; // the number of cases
	inFile >> N;
	
	for (int i = 0; i < N; i++)
	{
		ProcessCase(i, inFile, outFile);
	}

	inFile.close();   // close the streams
	outFile.close(); 
	return 0;
}
