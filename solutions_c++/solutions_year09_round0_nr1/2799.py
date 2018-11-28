// baidutime.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include <iostream>
#include <string>
using namespace std;

#define MAXDICTLENGTH 20
#define MAXWORDLENGTH 200000
#define MAXDICT 5001
#define MAXWORD 501

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
	int L,D,N;
	fscanf(pfileread,"%d %d %d\n",&L,&D,&N);

	char dict[MAXDICT][MAXDICTLENGTH],word[MAXWORDLENGTH];

	int i,j;

	for(i=0;i<D;i++)
	{
		fscanf(pfileread,"%s\n",dict[i]);
	}

	int result,k,m,p;
	bool found,found2;

	for(i=0;i<N;i++)	
	{
		result=0;
		fscanf(pfileread,"%s\n",word);
		for(j=0;j<D;j++)
		{
			p=0;
			found=true;
			for(k=0;k<L&&found;k++)
			{
				found2=false;
				if(word[p]=='(')
				{
					m=p+1;
					do
					{
						if(!found2&&word[m]==dict[j][k])
						{
							found2=true;
						}
						m++;
					}while(word[m]!=')');
					p=m+1;
				}
				else
				{
					if(word[p]==dict[j][k])
					{
						found2=true;
					}
					p++;
				}
				if(!found2)
				{
					found=false;
				}
			}
			if(found) result++;
		}
		fprintf(pfilewrite,"Case #%d: %d\n",i+1,result);
	}
	
	fclose(pfileread);
	fclose(pfilewrite);
	return;
}
