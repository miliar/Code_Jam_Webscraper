// Google01.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
bool CheckArray(int * arr,int arrlen,int dest)
{
	for(int i=0;i<arrlen;i++)
	{
		if(arr[i]==dest)
			return true;
	}
	return false;
}
int process(int start,int end)
{
	int count = 0, rc = 0;
	int cpLen = 0, cpStart = 0;
	char szNum[10]={0};
	char szRec[10]={0};
	int processed[1024] = {0};
	int proccount =0 ;
	for(int i=start;i<=end;i++)
	{
		memset(szNum,0,10);
		itoa(i,szNum,10);
		for(int j=1;j<strlen(szNum);j++)
		{
			memset(szRec,0,10);
			cpStart = j;
			cpLen = strlen(szNum)-cpStart;
			memcpy(szRec,&szNum[cpStart],cpLen);
			memcpy(&szRec[cpLen],szNum,cpStart);
			if(szRec[0]=='0')continue;
			rc = atoi(szRec);
			if(rc>i && rc<=end && (!CheckArray(processed,proccount,rc)))
			{
				processed[proccount]=rc;
				proccount++;
				count++;
			}
		}
		memset(processed,0,sizeof(processed));
		proccount = 0;
	}
	return count;
}

int main(int argc, char* argv[])
{
	char cLetter = 0;
	FILE * fp = fopen("C-small-attempt1.in","r");
	fseek(fp,0,0);
	int lines = 0;
	int iStart = 0,iEnd = 0;
	fscanf(fp,"%d",&lines);
	for(int i=0;i<lines;i++)
	{
		fscanf(fp,"%d %d",&iStart,&iEnd);
		printf("Case #%d: %d\n",i+1,process(iStart,iEnd));
	}
	fclose(fp);
	getchar();
	return 0;
}
