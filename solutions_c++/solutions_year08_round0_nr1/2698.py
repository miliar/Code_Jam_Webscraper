// Test_google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include <string.h>

int nTestCase,nSearchEngine[100],nQuery[1000];
char ***SrchEngList,***QueryList;

int GetMinSwitch(int );
int GetMaxPossibleEngine(int TstCaseN,int startindex);

int main(int argc, char* argv[])
{
	
	char mystring [100];
	
	FILE *f,*fw;
	f=fopen("D:\\downloads\\A-small-attempt9.in", "rb");
	if( f==NULL )
	{
      printf("File not found\r\n");
	  return 0;
	}
	fw=fopen("C:\\Documents and Settings\\parthasarathy\\Desktop\\result.out", "rb");
	if( f==NULL )
	{
      printf("File not found\r\n");
	  return 0;
	}
	SrchEngList=(char***)malloc(20* sizeof(char **));
	QueryList=(char***)malloc(20*sizeof(char **));
	
	for(int i=0;i<20;i++)
	{
		SrchEngList[i]=(char**)malloc(100* sizeof(char *));
		QueryList[i]=(char**)malloc(1000*sizeof(char *));
	}
	for(int j=0;j<20;j++)
	{
	for(int i=0;i<100;i++)
	{
		SrchEngList[j][i]=(char*)malloc(100* sizeof(char ));
	}
	for(int i=0;i<1000;i++)
	{
		QueryList[j][i]=(char*)malloc(1000*sizeof(char ));
	}
	}
	//SrchEngList=(char***)malloc(20*100*100);
	//QueryList=(char***)malloc(20*1000*100);

	fgets(mystring , 100 , f);
	nTestCase=atoi(mystring);

	for(int i=0;i<nTestCase;i++)
	{
		fgets(mystring , 100 , f);
		nSearchEngine[i]=atoi(mystring);
		for(int j=0;j<nSearchEngine[i];j++)
		{
			fgets(mystring , 100 , f);
			memcpy(SrchEngList[i][j],mystring,100);
		}

		fgets(mystring , 100 , f);
		nQuery[i]=atoi(mystring);
		for(int j=0;j<nQuery[i];j++)
		{
			fgets(mystring , 100 , f);
			memcpy(QueryList[i][j],mystring,100);
		}
	}
	for(int i=0;i<nTestCase;i++)
	{
		printf("Case #%d: %d\r\n",i+1,GetMinSwitch(i));
	}
	free(QueryList);
	free(SrchEngList);
	return 0;
}

int GetMinSwitch(int TstCaseN)
{
	int nFinished=0,nSwitch=0,MaxPosble;
	while(1)
	{
		if((MaxPosble=GetMaxPossibleEngine(TstCaseN,nFinished))==0)
		{
			return nSwitch;
		}
		else
		{
			nSwitch++;
			nFinished+=MaxPosble;
		}
	}
	return -1;
}

int GetMaxPossibleEngine(int TstCaseN,int startindex)
{
	int Max=0,temp;
	int i,j;
	for(i=0;i<nSearchEngine[TstCaseN];i++)
	{
		temp=0;
		for(j=startindex;j<nQuery[TstCaseN];j++)
		{
			if(strcmp(SrchEngList[TstCaseN][i],QueryList[TstCaseN][j])!=0)
			{
				temp++;
			}
			else
			{
				if(Max<temp)
				{
					Max=temp;
					
				}
				break;
			}

		}
		if(j==nQuery[TstCaseN])
				return 0;
	}

	//if((startindex+Max+1)>=nQuery[TstCaseN])
	//	return 0;
	return Max;
}