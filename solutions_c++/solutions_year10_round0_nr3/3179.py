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
		unsigned long Rtrips,kCapacity,Ngroups;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> Rtrips;
		ss >> kCapacity;
		ss >> Ngroups;
		int groups[1000];
		fin.getline(temp,2000);
     	strstream ss1;
		ss1<<temp;
		for (j=0;j<Ngroups;++j)
		{
			ss1 >> groups[j];
		}
		int currpos = 0;
		int groupsflag[1000];
		unsigned long lastrent[1000];
		for (j=0;j<Ngroups;++j) groupsflag[j] = -1;
		unsigned long rent = 0;
		for (unsigned long r = 1;r <=Rtrips;++r)
		{
             int total = 0;
			 int origcurrpos = currpos;
             while ((total + groups[currpos]) <= kCapacity)
			 {
				 total = total + groups[currpos];
				 ++currpos;
				 if (currpos == Ngroups) currpos = 0;
				 if (currpos == origcurrpos) break; // All groups in the Ride can go once
			 }
             rent += total;
			 if (groupsflag[currpos] != -1)
			 {
				 //We detected a cycle
				 int cyclelength = r - groupsflag[currpos];
				 int cyclerent = rent-lastrent[currpos];
				 int ncycles = (Rtrips-r)/cyclelength;
				 rent += ncycles*cyclerent;
                 r += ncycles*cyclelength;
				 for (j=0;j<Ngroups;++j) groupsflag[j] = -1;

			 }
			 groupsflag[currpos]=r;
			 lastrent[currpos]= rent;
			 
		}



		fprintf(f2,"Case #%d: ",i+1);
	
	    fprintf(f2,"%ld\n",rent);
	
		
        
	    
			
	}
	
  return 0;	
}