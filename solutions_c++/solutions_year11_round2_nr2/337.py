#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double MinTime(int D, int N1, int N2, int nDist[20][2]);
int main()
{
	//ifstream fin("B-small-attempt0.in");
	ifstream fin("B-large.in");
	//ifstream fin("TestData.txt");

	//ofstream fout("SmallOut.txt");
	//ofstream fout("B_SmallOut.txt");
	ofstream fout("B_LargeOut.txt");

	int nCaseNum,nCaseIdx;
	long long nDist[20][2];
	int C,D;
	int nCidx;
	int nIdx1,nIdx2;
	int nVtotal;
	fin >> nCaseNum;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		fin >> C >> D;
		nVtotal = 0;
		for (nCidx=0;nCidx<C;nCidx++)
		{
			fin >> nDist[nCidx][1] >> nDist[nCidx][0];
			nVtotal += nDist[nCidx][1];
		}
		double dMaxTime = 0,dTime;
		for(nIdx1=0;nIdx1<C;nIdx1++)
		{
			for (nIdx2=nIdx1;nIdx2<C;nIdx2++)
			{
				dTime = MinTime(D,nIdx1,nIdx2,nDist);
				if (dMaxTime<dTime)
					dMaxTime = dTime;
			}
		}


		fout << "Case #" << nCaseIdx+1 << ": ";
		fout << dMaxTime;
		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}

double MinTime(int D, int N1, int N2, long nDist[20][2])
{
	 int nIdx1;
	 int nTotalMan = 0;
	 for(nIdx1 = N1;nIdx1<=N2;nIdx1++)
		 nTotalMan += nDist[nIdx1][0];
	 long long nExpand = (nTotalMan-1)*D;
	 if(nExpand<(nDist[N2][1]-nDist[N1][1]))
		 return 0;
	 else
		 return double(nExpand-nDist[N2][1]+nDist[N1][1])/2;

}