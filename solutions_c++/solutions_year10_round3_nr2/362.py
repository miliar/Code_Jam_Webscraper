// Load_Testing.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char* argv[])
{
	int t;
	double l,p,c;
	int i=0,j=0;
	ifstream fin("B-large.in",ios::in);
	ofstream fout("output.txt",ios::out);
	fin>>t;
	int y=0;

	for(int tt=0;tt<t;tt++)
	{
		y=0;
		fin>>l>>p>>c;
		double b=((double)p)/l;
	//	cout<<b<<endl;
		if(b<=c) 
		{fout<<"Case #"<<tt+1<<": 0"<<endl;continue;}
		else 
		{
			y++;			
			while(sqrt(b)>c)
			{y++;b=sqrt(b);}
		}
		fout<<"Case #"<<tt+1<<": "<<y<<endl;

	}


	fin.close();
    fout.close();
	return 0;
}
