// b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <vector>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin, *fout;
	fin = fopen("b.in","r");
	fout = fopen("b.out","w");
	int c;
	fscanf(fin,"%d\n",&c);
	for(int casecount =0; casecount < c; casecount++)
	{
		int n,k,b,t;
		fscanf(fin,"%d %d %d %d\n",&n, &k, &b, &t);
		vector<int> X;
		vector<int> V;
		for(int i = 0; i < n; i++)
		{
			int x;
			if(i == n-1)
				fscanf(fin,"%d\n",&x);
			else
				fscanf(fin,"%d ",&x);
			X.push_back(x);
		}
		for(int i = 0; i < n; i++)
		{
			int v;
			if(i == n-1)
				fscanf(fin,"%d\n",&v);
			else
				fscanf(fin,"%d ",&v);
			V.push_back(v);
		}

		int swapcount = 0;
		int getcount = 0;
		for(int i = n-1; i>=0; i--)
		{
			if(X[i] + V[i]*t >= b)
			{
				getcount++;
				for(int j = i; j < n; j++)
				{
					if(X[j] + V[j]*t < b)
					{
						swapcount++;
					}
				}
			}
			if(getcount == k)break;
		}

		if(getcount < k)
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",casecount+1);
		else
			fprintf(fout,"Case #%d: %d\n",casecount+1,swapcount);
		
	}
	return 0;
}

