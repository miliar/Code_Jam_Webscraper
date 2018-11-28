#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;

double CalcWP(int N, int RowSchedule[20]);
int main()
{
	//ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large.in");
	//ifstream fin("TestData.txt");

	//ofstream fout("SmallOut.txt");
	//ofstream fout("A_SmallOut.txt");
	ofstream fout("LargeOut.txt");

	int nCaseNum,nCaseIdx;
	int N,nRowIdx,nColIdx,nPIdx;
	int Schedule[20][20];
	int nTotal[20];
	double WP[20],OWP[20][20],OWP2[20],OOWP[20],RPI[20];
	char chInput;

	fin >> nCaseNum;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		fin >> N;
		for (nRowIdx=0;nRowIdx<N;nRowIdx++)
			nTotal[nRowIdx] = 0;

		for(nRowIdx=0;nRowIdx<N;nRowIdx++)
		{
			for(nColIdx=0;nColIdx<N;nColIdx++)
			{
				fin >> chInput;
				switch(chInput)
				{
					case '.':Schedule[nRowIdx][nColIdx] = 0;break;
					case '0':Schedule[nRowIdx][nColIdx] = -1;nTotal[nRowIdx]++;break;
					case '1':Schedule[nRowIdx][nColIdx] = 1;nTotal[nRowIdx]++;break;				
				}
			}
		}

		for(nPIdx=0;nPIdx<N;nPIdx++)
		{
			int nWin=0;
			for(int idx=0;idx<N;idx++)	
				if (Schedule[nPIdx][idx]>0)
					nWin++;
			WP[nPIdx] = double(nWin)/double(nTotal[nPIdx]);
			//cout << WP[nPIdx] << endl;
		}

		int nPidx,nidx,nidx2;
		for(nPidx=0;nPidx<N;nPidx++)
		{
			OWP[nPidx][nPidx] = 0;
			for(nidx=0;nidx<N;nidx++)
			{
				int nWin = 0, nTotal =0;
				if(nidx!= nPidx)
				{
					for(nidx2=0;nidx2<N;nidx2++)
					{
						if (nidx2 != nPidx)
						{
							if (Schedule[nidx][nidx2]!=0)
								nTotal++;
							if (Schedule[nidx][nidx2]>0)	
								nWin++;
						}
					}
				}
				OWP[nPidx][nidx] = double(nWin)/double(nTotal);
			}
		}

		for(nPidx=0;nPidx<N;nPidx++)
		{
			double dSum  = 0;
			for(nidx=0;nidx<N;nidx++)
				if (Schedule[nPidx][nidx]!=0)
					dSum += OWP[nPidx][nidx];				
			OWP2[nPidx] = dSum/nTotal[nPidx];
		}

		for(nPidx=0;nPidx<N;nPidx++)
		{
			double dSum  = 0;
			for(nidx=0;nidx<N;nidx++)
				if (Schedule[nPidx][nidx]!=0)
					dSum += OWP2[nidx];				
			OOWP[nPidx] = dSum/double(nTotal[nPidx]);
		}

		for(nPidx=0;nPidx<N;nPidx++)
			RPI[nPidx] = 0.25*WP[nPidx]+0.5*OWP2[nPidx]+0.25*OOWP[nPidx];

		fout << "Case #" << nCaseIdx+1 << ": " << endl;
		for(nPidx=0;nPidx<N;nPidx++)
			fout << setprecision(10) << RPI[nPidx] << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
/*
double CalcWP(int N, int RowSchedule[20])
{
	int idx;
	int nWin=0,nTotal=0;
	for(idx=0;idx<N;idx++)
	{
		if (RowSchedule[idx]!=0)
			nTotal++;
		if (RowSchedule[idx]>0)
			nWin++;
	}
	return double(nTotal)/double(nTotal);
}

double CalcOWP(int N, int Schedule[20][20],double [])
{
	double OWP[20][20];
	int nPidx,nidx,nidx2;
	for(nPidx=0;nPidx<N;nPidx++)
	{
		OWP[nPidx][nPidx] = 0;
		for(nidx=0;nidx++;nidx<N)
		{
			int nWin = 0, nTotal =0;
			if(nidx!= nPidx)
			{
				for(nidx2=0;nidx2<N;nidx2++)
				{
					if (nidx2 != nPidx)
					{
						if (Schedule[nidx][nidx2]!=0)
							nTotal++;
						if (Schedule[nidx][nidx2]>0)	
							nWin++;
					}
				}
			}
			OWP[nPidx][nidx] = double(nWin)/double(nTotal);
		}
	}
}
*/