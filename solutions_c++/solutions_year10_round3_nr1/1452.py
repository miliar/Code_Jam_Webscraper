#include <iostream.h>
#include <fstream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
void main()
{
	int T;
	int N;
	long K,temp;
	long count=0;
	int* left;
	int* right;	
	char* infile="A-small-attempt0.in";
	char* outfile="A-large.out";
	fstream fin;
	fstream	fout;
	fin.open(infile, ios::in);
	fout.open(outfile,ios::out);
	fin>>T;
	
	for(int i=1;i<=T;i++)
	{
		count=0;
		fin>>N;
		left=new int[N];
		right=new int[N];
		for(int j=0;j<N;j++)
		{
			fin>>left[j];
			fin>>right[j];
		}
		for(int j=0;j<N-1;j++)
		{
			for(int k=j+1;k<N;k++)
			{
				if(left[k]<0) continue;
				if(((left[k]-left[j])*(right[k]-right[j]))<0) {count++;left[k]=-1;} 
			}
		}
		
		fout<<"Case #"<<i<<": "<<count;
		
		
		if(i<T) fout<<"\n";
	}
	
	fin.close();
	fout.close();

	
     
}

