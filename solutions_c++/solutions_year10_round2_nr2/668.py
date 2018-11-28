// r1b2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>

int Solve(int *xi, int *vi, int n, int k, int b, int t)
{
	double ti[51];

	int nSuccesses = 0;
	for (int i = 0; i < n; i++)
	{
		// see if this chick is past the mark in time 
		if (xi[i] + vi[i] * t >= b) nSuccesses++; 

		if (vi[i] == 0)
		{
			ti[i] = 1e99;
		}
		else
		{
			ti[i] = (double)(b - xi[i]) / (double)vi[i];
		}
	}
	if (nSuccesses < k) return -1;

	int nJumps = 0;
	nSuccesses = 0;
	
	for (int i = n - 1; i >= 0 && nSuccesses < k; i--)
	{
		// if this is not going to make it, jump it for those below that will
		if (ti[i] > (double)t) 
		{
			nJumps += k - nSuccesses;
		}
		else 
		{
			nSuccesses++;
		}
	}

	return nJumps;
}

int _tmain(int argc, _TCHAR* argv[])
{
    FILE * fIn = fopen("B-large.in", "r");
    FILE * fOut = fopen("test.out", "w");

    int nTests = 0;
    fscanf(fIn, "%d", &nTests);
    printf("%d tests\n", nTests);

    for (int iTest = 1; iTest <= nTests; iTest++)
    {
		printf ("Test %d:", iTest);
		
		int xi[51];
		int vi[51];

		int n, k, b, t; fscanf(fIn, "%d %d %d %d", &n, &k, &b, &t);

		for (int i = 0; i < n; i++)
		{
			fscanf(fIn, "%d", &xi[i]);
		}
		for (int i = 0; i < n; i++)
		{
			fscanf(fIn, "%d", &vi[i]);
		}

		int iRes = Solve(xi, vi, n, k, b, t);

		fprintf(fOut, "Case #%d: ", iTest);
		if (iRes == -1) fprintf(fOut, "IMPOSSIBLE\n");
		else fprintf(fOut, "%d\n", iRes);
	}

	return 0;
}

