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

int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
    
	//ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
	ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
//ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
//	ifstream fin("C-small-attempt1.in");FILE *f2 = fopen("C-small-attempt1.out","w");
//	ifstream fin("C-small-attempt2.in");FILE *f2 = fopen("C-small-attempt2.out","w");
//	ifstream fin("C-small-attempt3.in");FILE *f2 = fopen("C-small-attempt3.out","w");

	
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	{
		unsigned long Nwires;
		int A1[1001],B1[1001];
		long result = 0;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> Nwires;
        rep(k,0,Nwires)
		{
			fin.getline(temp,2000);
			strstream ss1;
			ss1 << temp;
			ss1 >> A1[k];
			ss1 >> B1[k];
		}
		rep(k,0,Nwires)
		{
			rep(j,k+1,Nwires)
			{
				if (j==k) continue;
				if ((A1[k]>A1[j]) && (B1[k] < B1[j])) ++ result;
				if ((A1[k]<A1[j]) && (B1[k] > B1[j])) ++ result;
			}
		}


		fprintf(f2,"Case #%ld: %ld\n",i+1,result);
	

		
        
	    
			
	}
	
  return 0;	
}