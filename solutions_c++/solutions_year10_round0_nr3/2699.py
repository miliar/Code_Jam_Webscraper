// fair.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int *groups, tg = 0;
long total = 0;

void calc(int k)
{
	int i,sum=0,c,j;
	int *temp = new int[tg];
	int *waste;
	for(i=0;i<tg;i++)
	{
		if(sum+groups[i]>k)
			break;
		sum+=groups[i];
	}
	total+=sum;
	c = 0;
	for(j=i;j<tg;j++)
		temp[c++] = groups[j];
	for(j=0;j<i;j++)
		temp[c++] = groups[j];
	waste = groups;
	groups = temp;
	delete waste;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int r=0,n=0,k=0,i,t,j;
	string line;
	ifstream myfile ("example.txt");
	ofstream outfile("out.txt");
	if (myfile.is_open())
	{
		getline (myfile,line);
		t = atoi(line.c_str()); 
		for(i=0; i<t; i++)
		{
			getline (myfile,line);
			char *pch = (char *)line.c_str();
			r = atoi(strtok (pch," "));
			k = atoi(strtok (NULL," "));
			n = atoi(strtok (NULL," "));
			tg = n;

			groups = new int[n];
			getline (myfile,line);
			pch = (char *)line.c_str();
			groups[0] = atoi(strtok (pch," "));
			for(j=1;j<n;j++)
				groups[j] = atoi(strtok (NULL," "));
			for(j=0;j<r;j++)
				calc(k);
			outfile << "Case #" << i+1 << ": " << total<< endl;
			total = 0;
			delete groups;
		}
		myfile.close();
		outfile.close();
	}
	return 0;
}

