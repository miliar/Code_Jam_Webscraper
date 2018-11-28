// Rope_Intranet.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;


int main(int argc, char* argv[])
{

	int i=0,j=0;
	int a[1000];
	int b[1000];
	int t=0,n=0,y=0;
	ifstream fin("A-large.in",ios::in);
	ofstream fout("output.txt",ios::out);
	fin>>t;
	for(int tt=0;tt<t;tt++)
	{
		y=0;
		fin>>n;
		for(j=0;j<n;j++)
		{fin>>a[j];fin>>b[j];}
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
			{
				if((a[i]>a[j] && b[i]<b[j])||(a[i]<a[j] && b[i]>b[j])) y++;

			}
		fout<<"Case #"<<tt+1<<": "<<y<<endl;

		
	}

	  fin.close();
    fout.close();
	return 0;
}
