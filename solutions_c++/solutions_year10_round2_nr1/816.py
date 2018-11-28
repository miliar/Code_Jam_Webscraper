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

int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
    
//	ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
	ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
//	ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
//	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
//	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
//	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");

	
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	{
		unsigned long Nsnpappers,Ksnaps;
		set <string> existing;
		vector <string> newdirs;
        int result = 0;
		fin.getline(temp,2000);
		strstream ss;
		int N,M;
		ss << temp;
		ss >> N;
		ss >> M;
		rep(k,0,N) 
		{
			fin.getline(temp,2000);
			existing.insert(temp);
		}
		rep(j,0,M) 
		{
			fin.getline(temp,2000);
			newdirs.push_back(temp);
		}
		

		rep(k,0,newdirs.size())
		{
			string currdir = newdirs[k];
			int base = currdir.find_first_of('/',1);
			while (base > 0)
			{
				string pdir = currdir.substr(0,base);
				if (existing.find(pdir)==existing.end())
				{
					++result;
					existing.insert(pdir);
				}

				base = currdir.find_first_of('/',base+1);
			}
			
				if (existing.find(currdir)==existing.end())
				{
					++result;
					existing.insert(currdir);
				}

		}

		fprintf(f2,"Case #%d: %d\n",i+1,result);
	
		
        
	    
			
	}
	
  return 0;	
}