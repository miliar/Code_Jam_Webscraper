#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int FyDivide(const int N1,const int N2);

int main()
{
	//ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large.in");
	//ifstream fin("TestData.txt");
	
	//ofstream fout("SmallOut.txt");
	ofstream fout("LargeOut.txt");
	int nCaseNum,nCaseIdx;
	fin >> nCaseNum;
	int Pd, Pg;
	long long N;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{

		fin >> N >> Pd >> Pg;
		bool flag=false;
		if (Pg==100 && Pd == 100)
			flag = true;
		else if (Pg==0 && Pd ==0)
			flag = true;
		else if (Pg==100 && Pd != 100)
			flag = false;
		else if (Pg ==0 && Pd != 0)
			flag = false;
		else if (N>=100/FyDivide(100,Pd))
			flag = true;
		fout << "Case #" << nCaseIdx+1 << ": ";
		if (flag)
			fout << "Possible";
		else
			fout << "Broken";
		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}

int FyDivide(const int N1,const int N2)
{
	if (N1<N2)
		return 1;
	int M1 = N1, M2 = N2, temp;
	while(M2>1 && (M1 % M2 !=0))
	{
		temp = M1 % M2;
		M1 = M2;
		M2 = temp;
	}
	return M2;
}
