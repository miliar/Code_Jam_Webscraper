#include "stdio.h"
#include <iostream>
#include <fstream>
using namespace std;
void main()
{
	FILE *infile;
	int CaseNum,P,K,L;
	long val[1000];
	int Im;
	long long R,temp;
	ofstream outfile("Output.out");
	if (!outfile)
	{
		cerr<<"cannot open the output file\n";
		exit(-1);
	}
	infile=fopen("d:\\test.in","r");   
	fscanf(infile,"%d",&CaseNum); 
	for (int j=0;j<CaseNum;j++)
	{
		Im = 0;
		fscanf(infile,"%d %d %d",&P,&K,&L);
		if (P*K<L)
		{
			Im = 1;
			goto out;
		}
		for (int i=0;i<L;i++)
		{
			fscanf(infile,"%ld",&val[i]); 
			if (val[i]>1000000)
			{
				Im = 1;
				goto out;
			}
		}
		for (int n=0;n<L;n++)
		{
			for (int m=0;m<L-1;m++)
			{
				if (val[m]<val[m+1])
				{
					temp = val[m];
					val[m] = val[m+1];
					val[m+1] = temp;
				}
			}
		}
		R = 0;
		for (int n=0;n<L;n++)
		{
			R = R + val[n]*(n/K+1);
		}
out:
		if (Im == 1)
		{
			outfile<<"Case #"<<j+1<<":"<<" IMPOSSIBLE"<<endl;
		}
		else
		{
			outfile<<"Case #"<<j+1<<": "<<R<<endl;
		}
	}
}