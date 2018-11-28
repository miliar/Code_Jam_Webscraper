// Snapper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int calc(int N, int K)
{
	long a=0,x,y;
	a = ((long)pow((float)2,N));
	if(K < a-1)
		return 0;
	else if (K == a-1 )
		return 1;
	else
	{
		y = (K%a);
		if(y == a-1)
			return 1;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T=0,N=0,K=0,i;
	string line;
	ifstream myfile ("example.txt");
	ofstream outfile("out.txt");
	if (myfile.is_open())
	{
		getline (myfile,line);
		T = atoi(line.c_str()); 
		for(i=0; i<T; i++)
		{
			getline (myfile,line);
			char *pch = (char *)line.c_str();
			N = atoi(strtok (pch," "));
			K = atoi(strtok (NULL," "));
			int ret = calc(N,K);
			if(ret == 0)
				outfile << "Case #" << i+1 << ": OFF" << endl;
			else
				outfile << "Case #" << i+1 << ": ON" << endl;
		}
		myfile.close();
		outfile.close();
	}
	return 0;
}

