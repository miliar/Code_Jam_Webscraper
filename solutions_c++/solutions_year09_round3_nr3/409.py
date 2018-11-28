// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)
/*#define MAXN 100
//Binomial functions typed from Programming Challenges  - Skiena, Revilla
long bc[MAXN][MAXN];
long binomial_cofficient(int n,int m)
{
   int i,j;
   repz(i,n+1) bc[i][0] = 1;
   repz(j,n+1) bc[j][j] = 1;

   rep(i,1,n+1)
	   rep(j,1,i)
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j];
   return bc[n][m];
}
*/

using namespace std;

long getCost(int rel[],int rels,int P)
{
	int i,j,k;
	int *A;
	A = new int[P];
	rep(i,0,P) A[i] = 1;
	long cost = 0;


	rep(j,0,rels)
	{
		int relp = rel[j]-1;
		A[relp] = 0;
		int ii,jj;
		ii = relp -1;
		jj = relp+1;
		if (ii >= 0)
		{
			while (A[ii]==1 && ii>=0)
			{
				--ii;
				++cost;
			}
		}
		if (jj < P)
		{
			while (A[jj]==1 && jj < P)
			{
				++jj;
				++cost;
			}
		}
	}
	return cost;
}

int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	char temp[2000];
	int relQ[102];
	fin >> numCases;
	fin.getline(temp,2000);

	for (i=0;i<numCases;++i)
	//repz(i,numCases);
	{

		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		int P, Q;
		ss >> P >> Q;
		fin.getline(temp,2000);
		strstream ss1;
		ss1 << temp;
		rep(j,0,Q)
		{
			int tempi;
			ss1>>tempi;
			relQ[j] = tempi;
		}
		long mincost = getCost(relQ,Q,P);
		while (next_permutation(relQ,relQ+Q))
		{
			long tcost = getCost(relQ,Q,P);
			if ((tcost) < mincost) mincost = tcost;
			
		}

		fprintf(f2,"Case #%d: %ld\n",i+1,mincost);
	}

	return 0;
}

