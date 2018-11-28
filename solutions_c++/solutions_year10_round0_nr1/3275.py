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
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	{
		unsigned long Nsnpappers,Ksnaps;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> Nsnpappers;
		ss >> Ksnaps;
		fprintf(f2,"Case #%d: ",i+1);
		unsigned long pow2Ns = pow(2,Nsnpappers);
	    if ((Ksnaps %pow2Ns) == (pow2Ns-1)) fprintf(f2,"ON\n");
		else {if (i!=(numCases-1)) fprintf(f2,"OFF\n");
		      else fprintf(f2,"OFF");
		}

		
        
	    
			
	}
	
  return 0;	
}