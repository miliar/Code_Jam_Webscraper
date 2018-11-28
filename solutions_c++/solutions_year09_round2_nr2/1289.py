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
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)


using namespace std;

long getNext(long tbase)
{
	long i,j,k;
	int freq[10];
	int freq2[10];
	long temp = tbase;
	long power = 10;
	int digit;
	rep(i,0,10) freq[i] = 0;
	rep(i,0,10) freq2[i] = 0;
	while (temp > 0 )
	{
		digit = temp % power;
		temp = temp/power;
		freq[digit]++;
	}
	for (j =1;j<10000000;++j)
	{
		temp = tbase + j;
		rep(i,0,10) freq2[i] = 0;
		while (temp > 0 )
		{
		digit = temp % power;
		temp = temp/power;
		freq2[digit]++;
		}
		bool found = true;
		for (k=1;k<10;++k)
		{
			if (freq[k] != freq2[k]) found = false;
		}
		if (found) return tbase+j;
	}
	
	return 0;
}

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
	//repz(i,numCases);
	{
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		long tbase;
		ss >> tbase;
		
		fprintf(f2,"Case #%d: %d\n",i+1,getNext(tbase));
	
	}
	
	return 0;
}

