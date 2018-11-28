// QuestionA.cpp : main project file.

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

char engname[10][100];
int engnum;

int getindex(char* str)
{
	int i;
	for(i=0;i<engnum;i++)
		if(!strcmp(str,engname[i]))
			return i;


return 0;
}

int zero(int* list)
{
	int i;
	for(i=0;i<engnum;i++)
		list[i] = 0;
return 0;
}

int mult(int* list)
{
	int i,mult=1;
	for(i=0;i<engnum;i++)
		mult = mult*list[i];
return mult;
}

int main()
{
	
	int i,j,q,end=0;
	int cases;
	char qname[100];
	int counts[100] = {0};
	FILE* in;
	FILE* out;
	
	in = fopen("in.txt","r");
	out = fopen("out.txt","w");
	if (in == NULL ) exit(-1);
	fscanf(in,"%d",&cases);
	for(j=0;j<cases ; j++ )
	{
		end = 0; //Intialize for round
		fscanf(in,"%d",&engnum);
		for(i=0;i<engnum;i++)
		{
			fgets(engname[i],100,in);
			if (strcmp("\n",engname[i])==0)
			{ i--; continue; }
			//----engname[i][strlen(engname[i])-1]=NULL;
			//fscanf(in,"%s",engname[i]);
			//printf("%s",engname[i]);
		}
	
		fscanf(in,"%d",&q);
		zero(counts);
		end = 0;
			for(i=0;i<q;i++)
			{
				fgets(qname,100,in);
				if (strcmp("\n",qname)==0)
				{ i--; continue; }
				//----qname[strlen(qname)-1]=NULL;
				counts[getindex(qname)]++;
				//printf("Mullt : %d \n ", mult(counts) );
				if (mult(counts))
				{
					end++;
					zero(counts);
					counts[getindex(qname)]++;
				}
				
			}	
	
		for(i=0;i<engnum;i++)
			printf("%s : %d\n", engname[i] , counts[i] );
		//printf("%d",getindex("Googol"));	
		//printf("\n END : %d ",end);
		fprintf(out,"Case #%d: %d\n",j+1,end);
	}
fclose(in);
fclose(out);
system("pause");
return 0;
}