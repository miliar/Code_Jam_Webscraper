// baidutime.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include <iostream>
#include <string>
using namespace std;

#define MAXLENGTH 101

void main(int argc, char* argv[])
{
	FILE *pfileread,*pfilewrite;
	if((pfileread=fopen("input.txt","r"))==NULL)
	{
		printf("error reading\n");
		return;
	}
	if((pfilewrite=fopen("output.txt","w"))==NULL)
	{
		printf("error writing\n");
		return;
	}

	int i,j,k;
	int T,A,m;
	int dig[10],dig2[10];
	fscanf(pfileread,"%d\n",&T);
	int curr;
	bool found;
	for(i=0;i<T;i++)
	{
		fscanf(pfileread,"%d\n",&A);

		for(j=0;j<10;j++)
		{
			dig[j]=0;
			dig2[j]=0;
		}

		m=A;
		do
		{
			dig[m%10]++;
			m/=10;
		}while(m>0);

		found=false;
		do
		{
			A++;
			for(j=0;j<10;j++)
			{
				dig2[j]=0;
			}
			m=A;
			do
			{
				dig2[m%10]++;
				m/=10;
			}while(m>0);
			found=true;
			for(j=1;j<10;j++)
			{
				if(dig[j]!=dig2[j])
					found=false;
			}

		}while(!found);



		fprintf(pfilewrite,"Case #%d: %d\n",i+1,A);

	}
	
	fclose(pfileread);
	fclose(pfilewrite);
	return;
}
