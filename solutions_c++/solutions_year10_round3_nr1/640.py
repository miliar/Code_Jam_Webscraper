// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin, *fout;
	fin = fopen("a.in","r");
	fout = fopen("a.out","w");
	int t;
	fscanf(fin,"%d\n",&t);
	for(int casecount = 0; casecount < t; casecount++)
	{
		int n;
		fscanf(fin,"%d\n",&n);
		vector<int> A;
		vector<int> B;
		for(int i = 0; i < n; i++)
		{
			int a,b;
			fscanf(fin,"%d %d\n",&a, &b);
			A.push_back(a);
			B.push_back(b);
		}

		int count = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = i; j < n ; j++)
			{
				if((A[j] - A[i])*(B[j] - B[i]) < 0)
				{
					count++;
				}
			}
		}

		fprintf(fout,"Case #%d: %d\n",casecount+1,count);
	}
	return 0;
}

