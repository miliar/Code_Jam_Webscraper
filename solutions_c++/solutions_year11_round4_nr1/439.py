#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
	//ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large2.in");
	//ifstream fin("TestData.txt");

	//ofstream fout("SmallOut.txt");
	//ofstream fout("A_SmallOut.txt");
	ofstream fout("A-LargeOut.txt");




	long nCaseNum,nCaseIdx;
    double X, S, R, t, N;
	double w[1000][2];
	double WalkWayBegin, WalkWayEnd,WalkWayW;


	fin >> nCaseNum;
	for (nCaseIdx=0;nCaseIdx<nCaseNum;nCaseIdx++)
	{
		fin >> X >> S >> R >> t >> N;
		int idx,idx2;
		double dSumWalkwayLen = 0;
		double dTotalTime=0;

		for(idx=0;idx<N;idx++)
		{
			fin >> WalkWayBegin >> WalkWayEnd >> WalkWayW;
			w[idx][0] = WalkWayEnd-WalkWayBegin;
			dSumWalkwayLen += w[idx][0];
			w[idx][1] = WalkWayW;
		}

		// Sort
		double dSortChange;
		for(idx=0;idx<N;idx++)
			for(idx2=idx+1;idx2<N;idx2++)
			{
				if(w[idx][1]>w[idx2][1])
				{
					dSortChange = w[idx2][0];
					w[idx2][0] = w[idx][0];
					w[idx][0] = dSortChange;
					dSortChange = w[idx2][1];
					w[idx2][1] = w[idx][1];
					w[idx][1] = dSortChange;
				}
			}


		double dNonWalkwayLen = X-dSumWalkwayLen;
		if(dNonWalkwayLen/R>=t)
		{
			dTotalTime = t + (dNonWalkwayLen-t*R)/S;
			for(idx=0;idx<N;idx++)
			{
				dTotalTime += w[idx][0]/(w[idx][1]+S);
			}
		}
		else
		{
			double dRunRemain = t-dNonWalkwayLen/R;
//			cout << dRunRemain << endl;
			dTotalTime = dNonWalkwayLen/R;
			for (idx=0;idx<N;idx++)
			{
				if (dRunRemain>0)
					if (w[idx][0]/(w[idx][1]+R)<=dRunRemain)
					{
						dRunRemain -=w[idx][0]/(w[idx][1]+R);
						dTotalTime += w[idx][0]/(w[idx][1]+R);
					}
					else
					{						
						dTotalTime += dRunRemain+(w[idx][0]-dRunRemain*(w[idx][1]+R))/(w[idx][1]+S);
						dRunRemain = 0;
					}
				else
					dTotalTime += w[idx][0]/(w[idx][1]+S);
			}
		}



		fout << "Case #" << nCaseIdx+1 << ": ";
		fout << setprecision(10) << dTotalTime;
		fout <<  endl;
	}

	fin.close();
	fout.close();
	return 0;
}





