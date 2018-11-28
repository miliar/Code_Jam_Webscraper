// testcpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"


#include "stdio.h"
#include "stdlib.h"
#include "signal.h"
#include "process.h"
#include "malloc.h"

#include "fstream"
#include "list"
#include "vector"
#include "algorithm"
#include "time.h"

#include "queue"
#include "stack"

using namespace std;


typedef unsigned __int64 uint64;

char aa[51][60];

int main()
{
	int T;
	cin >> T;

	int K, N;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" <<t <<": ";
		cin >> N >>K;
		int maxR, maxB;
		maxB = maxR = 0;

		for (int i = 0; i < N; ++i)
		{
			cin >> aa[i];
		}

		for (int i = 0; i < N; ++i)
		{
			int ed = N-1;
			
			
			while (ed > 0){
			int j = ed;
			while (aa[i][j] == '.' && j >=0)
			{
				--j;
			}


			int len = ed-j;

			if (len > 0 && j >= 0)
			{
				for (int k = j; k >=0; --k)
					aa[i][k+len] = aa[i][k];
				
				for (int k = 0; k < len; ++k)
					aa[i][k]='.';
			}

			if (j < 0) break;

			while (aa[i][ed] != '.' && ed >=0)--ed;
			}
		}


			int tmpB, tmpR;
			tmpB = tmpR=0;

			for (int k = 0; k < N; ++k)
			{
				tmpB = tmpR = 0;
				for (int kk = 0; kk < N; ++kk)
				{
					if (aa[k][kk] == 'R')
					{
						tmpR++;
						if (tmpR > maxR)
						{
							maxR = tmpR;
						}
						tmpB = 0;
					}
					else if (aa[k][kk] == 'B')
					{
						tmpB++;
						if (tmpB > maxB)
						{
							maxB = tmpB; 
						}
						tmpR = 0;
					}
					else
					{
						tmpB = tmpR = 0;
					}
				}
			}

			for (int k = 0; k < N; ++k)
			{
				tmpB = tmpR = 0;
				for (int kk = 0; kk < N; ++kk)
				{
					if (aa[kk][k] == 'R')
					{
						tmpR++;
						if (tmpR > maxR)
						{
							maxR = tmpR;
						}
						tmpB = 0;
					}
					else if (aa[kk][k] == 'B')
					{
						tmpB++;
						if (tmpB > maxB)
						{
							maxB = tmpB; 
						}
						tmpR = 0;
					}
					else
					{
						tmpB = tmpR = 0;
					}
				}
			}


			for (int k = 0; k < N; ++k)
			{
				tmpB = tmpR = 0;
				for (int kk = 0; kk <=k; ++kk)
				{
					if (aa[kk][k-kk] == 'R')
					{
						tmpR++;
						if (tmpR > maxR)
						{
							maxR = tmpR;
						}
						tmpB = 0;
					}
					else if (aa[kk][k-kk] == 'B')
					{
						tmpB++;
						if (tmpB > maxB)
						{
							maxB = tmpB; 
						}
						tmpR = 0;
					}
					else
					{
						tmpB = tmpR = 0;
					}
				}
			}

			for (int k = N; k <= 2*(N-1); ++k)
			{
				tmpB = tmpR = 0;

				for (int kk = k-N+1; kk < N; ++kk)
				{
					if (aa[kk][k-kk] == 'R')
					{
						tmpR++;
						if (tmpR > maxR)
						{
							maxR = tmpR;
						}
						tmpB = 0;
					}
					else if (aa[kk][k-kk] == 'B')
					{
						tmpB++;
						if (tmpB > maxB)
						{
							maxB = tmpB; 
						}
						tmpR = 0;
					}
					else
					{
						tmpB = tmpR = 0;
					}

				}
			}

			for (int k = 0; k < N; ++k)
			{
				tmpB = tmpR = 0;

				for (int kk = k; kk < N; ++kk)
				{
					if (aa[kk][kk-k] == 'R')
					{
						tmpR++;
						if (tmpR > maxR)
						{
							maxR = tmpR;
						}
						tmpB = 0;
					}
					else if (aa[kk][kk-k] == 'B')
					{
						tmpB++;
						if (tmpB > maxB)
						{
							maxB = tmpB; 
						}
						tmpR = 0;
					}
					else
					{
						tmpB = tmpR = 0;
					}

				}
			}

			for (int k = 1; k < N; ++k)
			{
				tmpB = tmpR = 0;

				for (int kk = 0; kk < N -k; ++kk)
				{
					if (aa[kk][kk+k] == 'R')
					{
						tmpR++;
						if (tmpR > maxR)
						{
							maxR = tmpR;
						}
						tmpB = 0;
					}
					else if (aa[kk][kk+k] == 'B')
					{
						tmpB++;
						if (tmpB > maxB)
						{
							maxB = tmpB; 
						}
						tmpR = 0;
					}
					else
					{
						tmpB = tmpR = 0;
					}

				}
			}

			if (maxR >= K && maxB >= K)
				cout << "Both";
			else if (maxR >= K)
				cout << "Red";
			else if (maxB >= K)
				cout << "Blue";
			else
				cout << "Neither";
			if (t < T)
				cout << endl;


	}
	return 0;
}