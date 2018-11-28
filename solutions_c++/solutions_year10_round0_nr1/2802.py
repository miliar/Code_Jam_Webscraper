//============================================================================
// Name        : snapper.cpp
// Author      : jivjot
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include<cmath>
using namespace std;

int main() {
	FILE* fin,*fout;
	fin=fopen("A-large.in","r");
	fout=fopen("output.in","w");
	int t;
	fscanf(fin,"%d\n",&t);
	long n,k;
	double power;
	long temp;
	for(int i=0;i<t;i++)
	{
		fscanf(fin,"%ld %ld",&n,&k);
		power=pow(2,n);
		temp=(int)power;
		if((k%temp)==(temp-1))
		{
			fprintf(fout,"Case #%d: ON\n",i+1);
		}
		else
		{
			fprintf(fout,"Case #%d: OFF\n",i+1);
		}
	}
	return 0;
}
