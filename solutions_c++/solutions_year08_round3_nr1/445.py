// ProblemA.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>
#include <fstream>

using namespace std;

int L[1001];
int K[1001];

int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int main()
{	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	if(!fin) {
		cout << "Cannot open input file.\n";
		return 1;
	}

	int N;
	fin >> N;

	for(int nN=0; nN < N; nN++)
	{
		cout << "Case #" << nN+1 << ":" << " ";

		int P, nK, nL;
		fin >> P >> nK >> nL;

		for(int l=0; l < nL; l++)
		{
			fin >> L[l];
		}

		qsort(L, nL, sizeof(int), compare);

		if(P*nK < nL)
		{
			cout << "Impossible" << endl;
			continue;
		}

		for(int k=0; k<nK; k++)
		{
			K[k] = 0;			
		}

		long long presses = 0;
		int k=0;
		for(int l=0; l<nL; l++)
		{
			while(1)
			{
				k = k%nK;
				K[k]++;
				presses += L[l] * K[k];
				k++;
				break;
			}			
		}

		cout << presses << endl;
	}

	return 0;
}