#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>

using namespace std;

_int64 get_Difference(_int64 nA, _int64 nB);
_int64 get_Max_Divisor(_int64 nA, _int64 nB);

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("B-small-attempt1.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("B-small-attempt1.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	int N;
	_int64 preTi,postTi; 

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//²Ù×÷Çø
		inFile >> N;
		inFile >> preTi;
		inFile >> postTi;
		_int64 maxDivisor = get_Difference(preTi,postTi);
		for (int j=2; j<N; j++)
		{
			preTi = postTi;
			inFile >> postTi;
			maxDivisor = get_Max_Divisor(maxDivisor,get_Difference(preTi,postTi));
		}
		_int64 tail;
		_int64 outData;
		if (maxDivisor <= 0)
		{
			outData = 0;
		}
		else
		{
		tail = preTi%maxDivisor;
		if (tail == 0)
		{
			outData = 0;
		}
		else
		{
			outData = maxDivisor - tail;
		}
		}
		outFile << "Case #" << i+1 << ": " << outData << endl;
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}

_int64 get_Difference(_int64 nA, _int64 nB)
{
	if (nA > nB)
	{
		return nA-nB;
	}
	else
	{
		return nB-nA;
	}
}

_int64 get_Max_Divisor(_int64 nA, _int64 nB)
{
	if (0==nA)
	{
		return nB;
	}
	if (0==nB)
	{
		return nA;
	}
	_int64 tail;
	if (nA > nB)
	{
		tail = nA%nB;
		if (0==tail)
		{
			return nB;
		}
		else
		{
			return get_Max_Divisor(nB,tail);
		}
	}
	else
	{
		tail = nB%nA;
		if (0==tail)
		{
			return nA;
		}
		else
		{
			return get_Max_Divisor(nA,tail);
		}
	}
}