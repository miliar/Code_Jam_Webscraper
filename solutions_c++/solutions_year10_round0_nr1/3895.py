// googleTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;
int countRes(int n, int k)
{
	k = k+1;
	do {
		if (k%2 != 0)
			return 0;
		k = k/2;
		n --;
	}while(n > 0);
	return 1;
}
int main(int argc, char* argv[])
{
	ifstream infile("A-large.in");
	ofstream outfile("resFile");
	string line;
	getline(infile,line);
	int lineCnt= 0;
	while(getline(infile,line))
	{
		int N,k;
		lineCnt ++;
		sscanf(line.data(),"%d %d",&N,&k);
		outfile << "Case #" << lineCnt << ": ";
		if (countRes(N,k))
			outfile << "ON" << endl;
		else
			outfile << "OFF" << endl;
	}
	outfile.close();
	infile.close();
}

