// codejam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>



int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
	fout = fopen("d:\\B-large.txt","w+b");
	std::string str_in = "d:\\B-large.in";
	std::ifstream is(str_in.c_str());
	std::string line,s1,s2;

	int N,T,NA,NB;
	int A,B;

	int depA[100];
	int arrA[100];
	int depB[100];
	int arrB[100];
	
	int h1,m1,h2,m2;
	is >> N;//number of cases
	
	for (int i=0; i<N; i++)
	{
		is >> T; // turn around time
		is >> NA;
		is >> NB;
		for (int j=0; j<100; j++)
		{
			arrA[j]=1500;
			arrB[j]=1500;
		}
		//std::getline(is,line); 
		for (int j=0; j<NA; j++)
		{			
			is >> s1 >> s2;	
			h1 = atoi(s1.substr(0,2).c_str());
			m1 = atoi(s1.substr(3,2).c_str());
			depA[j]=h1*60+m1;
			h2 = atoi(s2.substr(0,2).c_str());
			m2 = atoi(s2.substr(3,2).c_str());
			arrB[j]=h2*60+m2+T;
			/*std::getline(is,line); 	// read A				
			h1 = h1*60+m1;*/
		}
		for (int j=0; j<NB; j++)
		{
			is >> s1 >> s2;	
			h1 = atoi(s1.substr(0,2).c_str());
			m1 = atoi(s1.substr(3,2).c_str());
			depB[j]=h1*60+m1;
			h2 = atoi(s2.substr(0,2).c_str());
			m2 = atoi(s2.substr(3,2).c_str());
			arrA[j]=h2*60+m2+T;
		}
		
		// sort
		int tmp;
		
		for (int j=0; j<NA-1; j++)
		{
			for(int k=j+1; k<NA; k++)
			{
				if (depA[k]<depA[j])
				{
					tmp = depA[k];
					depA[k] = depA[j];
					depA[j] = tmp;
				}
				if (arrB[k]<arrB[j])
				{
					tmp = arrB[k];
					arrB[k] = arrB[j];
					arrB[j] = tmp;
				}
			}
		}
		
		for (int j=0; j<NB-1; j++)
		{
			for(int k=j+1; k<NB; k++)
			{
				if (depB[k]<depB[j])
				{
					tmp = depB[k];
					depB[k] = depB[j];
					depB[j] = tmp;
				}
				if (arrA[k]<arrA[j])
				{
					tmp = arrA[k];
					arrA[k] = arrA[j];
					arrA[j] = tmp;
				}
			}
		}


		//solve;
		A=0;
		int maxA = 0;
		B=0;
		int Atime=0;
		int dep=0;
		int arr=0;
		while (dep<NA)
		{	
			if (dep==0 && arr==0) A++;
			if (depA[dep]<arrA[arr])
			{
				dep++;			
				if (A>maxA) maxA=A;
				A++;
			}
			else
			{
				arr++;
				A--;
			}			
		}
		//if (A>maxA) maxA=A;
		
		int maxB = 0;
		dep=0;
		arr=0;
		while (dep<NB)
		{	
			
			if (dep==0 && arr==0) B++;
			if (depB[dep]<arrB[arr])
			{
				dep++;
				if (B>maxB) maxB=B;
				B++;
			}
			else
			{
				arr++;
				B--;
			}			
		}
		//if (B>maxB) maxB=B;
		fprintf(fout,"Case #%d: %d %d\r\n",i+1,maxA,maxB);

	}
	
	fclose(fout);

	return 0;
}

