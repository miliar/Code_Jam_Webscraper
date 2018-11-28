// google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
#include <math.h>

#define FILENAME    "A-small-attempt0"
#define LEN_NAME	800*7
#define DES_STRING "Case #"

void getNum(int *numArr,char *str,int n)
{
	char *pTail = str;
	char *pHead = pTail;
	int  index = 0;
	int loop;
	int loopInner;
	int tmp;
	
	while(*pTail!=0)
	{
		if(*pTail==' '||*pTail == 10)
		{
			*pTail = 0;
			numArr[index] = atoi(pHead);
			index++;
			pHead = pTail+1;
		}
		pTail++;

	}

	for(loop = n-1;loop>0;loop--)
	{
		for(loopInner = 0;loopInner<loop;loopInner++)
		{
			if(numArr[loopInner] > numArr[loopInner+1])
			{
				tmp = numArr[loopInner];
				numArr[loopInner] = numArr[loopInner+1];
				numArr[loopInner+1] = tmp;
			}
		}
	}
}

int main(int argc, char* argv[])
{

	FILE *fpIn,*fpOut;
	char line[LEN_NAME+1];
	const int leng = LEN_NAME+1;
	int numLine; // value of N
	int loop;
	int loopInner;
	int loopSuper;
	int numRes;
	char n;
	int a1[800];
	int a2[800];

	// get the file
	fpIn = fopen(FILENAME".in","r");
	if(NULL == fpIn)
	{
		printf("File open error");
		return 0;
	}

	fpOut = fopen(FILENAME".out","w");

	//get T
	memset((void*)line,0,leng);
	fgets(line,leng,fpIn);
	numLine = atoi(line);
	if(0 == numLine)
	{
		printf("Error,numLine");
		return 0;
	}
	
	//main process
	for(loopSuper = 0;loopSuper<numLine; loopSuper++)
	{
		//get n
		memset((void*)line,0,leng);
		fgets(line,leng,fpIn);
		n = atoi(line);
		if(0 == numLine)
		{
			printf("Error,n\n");
			return 0;
		}

		//get a1
		memset((void*)line,0,leng);
		fgets(line,leng,fpIn);
		getNum(a1,line,n);
		//get a2
		memset((void*)line,0,leng);
		fgets(line,leng,fpIn);
		getNum(a2,line,n);

		//result
		numRes = 0;

		//calculate
		for(loop=0;loop<n;loop++)
		{
			if(a1[loop]<0)
			{
				numRes = numRes + a1[loop] * a2[n-loop-1];
			}
			else
				break;
		}
		for(loopInner = n;loopInner>loop;loopInner--)
		{
			numRes = numRes + a1[loopInner-1] * a2[n-loopInner];
		}

		printf("##%d : %d\n",loopSuper+1,numRes);
		//output
		sprintf(line,"%s%d: %d\n",DES_STRING,loopSuper+1,numRes);
		fputs(line,fpOut);
	}

	// close the files
	printf("close the file");
	fclose(fpIn);
	fclose(fpOut);
	return 0;
}

