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


using namespace std;

unsigned __int64 x;

int resultcomb[501][501];

#define MAXN 501 /* largest n or m */
long binomial_coefficient(long n,long m)
{
int i,j; /* counters */
if (n<m) return 0;
long bc[MAXN][MAXN]; /* table of binomial coefficients */
for (i=0; i<=n; i++) bc[i][0] = 1;
for (j=0; j<=n; j++) bc[j][j] = 1;
for (i=1; i<=n; i++)
for (j=1; j<i; j++)
bc[i][j] = (bc[i-1][j-1] + bc[i-1][j]) % 100003;
return( bc[n][m] % 100003 );
}

long getComb(int nx,int  nr)
{
	if (resultcomb[nx][nr]!=-1) return resultcomb[nx][nr];
	long res = 0;
	int k;
	int l;
	rep(l,1,nr)
	{
		res += (getComb(nr,l)*binomial_coefficient(nx-nr-1,nr-l-1)) % 100003;
	}
	resultcomb[nx][nr]=res % 100003;
	return res % 100003;
}

int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
    
//	ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
//	ifstream fin("C-large.in");FILE *f2 = fopen("C-large.out","w");
//	ifstream fin("C-small-attempt0.in");FILE *f2 = fopen("C-small-attempt0.out","w");
//	ifstream fin("C-small-attempt1.in");FILE *f2 = fopen("C-small-attempt1.out","w");
	ifstream fin("C-small-attempt2.in");FILE *f2 = fopen("C-small-attempt2.out","w");
//	ifstream fin("C-small-attempt3.in");FILE *f2 = fopen("C-small-attempt3.out","w");

	
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	rep(i,0,501) 
		rep(j,0,501)
	{
		resultcomb[i][j]=-1;
	}
	rep(i,0,501) resultcomb[i][1]=1;
	for (i=0;i<numCases;++i)
	{
		unsigned long Nints;
		long result = 0;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> Nints;
        rep(k,1,Nints)
		{
			result = (result +getComb(Nints,k)) % 100003;
		}
		fprintf(f2,"Case #%ld: %ld\n",i+1,result% 100003);
	

		
        
	    
			
	}
	
  return 0;	
}