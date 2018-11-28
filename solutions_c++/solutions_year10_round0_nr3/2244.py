#include <iostream.h>
#include <fstream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
void main()
{
	int T;
	double sumg;
	long R,tempR;
	long k,tempk,tryk;
	int N,count,numgroup;
	long* garray;
	char* infile="C-small-attempt0.in";
	char* outfile="C-small-attempt0.out";
	fstream fin;
	fstream	fout;
	fin.open(infile, ios::in);
	fout.open(outfile,ios::out);
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		fin>>R;
		fin>>k;
		fin>>N;
		garray=new long[N];
		for(int j=0;j<N;j++)
		{
			fin>>garray[j];
		}
		tempR=0;
		count=0;
		sumg=0;
		do
		{
			tempk=0;
			numgroup=0;
			while(true)
			{
				tryk=tempk+garray[count];
				if(tryk>k) break;
				else 
				{
					numgroup++;
					if(numgroup>N) break;
					tempk=tryk;
					count=(count+1)%N;
				}
				
			}		
			sumg+=tempk;
			tempR++;				
		}
		while(tempR<R);
		fout<<"Case #"<<i<<": "<<sumg;
		if(i<T) fout<<"\n";
	}
	
	fin.close();
	fout.close();

	
     
}

