#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;
const long MAXNUM = 100000;
bool Prime[MAXNUM];
bool checkPrime(const long N);
long getPower(const long long N, const long nPrime);

int main()
{
	//ifstream fin("C-small-attempt0.in");
	ifstream fin("C-large.in");
	//ifstream fin("TestData.txt");

	//ofstream fout("SmallOut.txt");
	//ofstream fout("C_SmallOut.txt");
	ofstream fout("C-LargeOut.txt");

	long i;
	for (i=0;i<MAXNUM;i++)
	{
		Prime[i] = true;
	}
	for(i=4;i<MAXNUM;i++)
	{
		if (!checkPrime(i))
		{
			Prime[i] = false;
		}
	}


	long nCaseNum,nCaseIdx;
	long long N;

	

	fin >> nCaseNum;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		fin >> N;
		if(N==1)
			fout << "Case #" << nCaseIdx+1 << ": 0" << endl;
		else
		{
			long long idx;
			long long nSpreadSum = 1;
			for(idx = 2;idx*idx<=N;idx++)
			{
				if (Prime[idx])
				{
					nSpreadSum += getPower(N,idx)-1;
				}
			}

			fout << "Case #" << nCaseIdx+1 << ": " << nSpreadSum <<  endl;
		}


	}

	fin.close();
	fout.close();
	return 0;
}

bool checkPrime(const long N)
{
	bool flag = true;
	for (long long i=2;i*i<=N;i++)
   {
	   if (Prime[i])
		   if (N%i ==0)
		   {
			   flag = false;
			   break;
		   }
   }
	return flag;
}

long getPower(const long long N, const long nPrime)
{
	long nPower  = 0;
	long long nProduct = nPrime;
	while(N>=nProduct)
	{
		nPower++;
		nProduct *= nPrime;
	}
	return nPower;
}