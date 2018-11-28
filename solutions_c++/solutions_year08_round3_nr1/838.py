// google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
#include <math.h>

#define FILENAME    "A-small-attempt0"
#define LEN_NAME	8*1000
#define DES_STRING "Case #"

void getNum(int *numArr,char *str,int n)
{
	char *pTail = str;
	char *pHead = pTail;
	int  index = 0;
	int loop;
	int loopInner;
	
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
}
void getNum2(int *numArr,char *str,int n)
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
			if(numArr[loopInner] < numArr[loopInner+1])
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
	int  n;
	int keyLeft;
	int control[3];
	int freq[1000];
	int tmp;


	// get the file
	fpIn = fopen(FILENAME".in","r");
	if(NULL == fpIn)
	{
		printf("File open error");
		return 0;
	}

	fpOut = fopen(FILENAME".out","w");

	//get N
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
		//get control
		memset((void*)line,0,leng);
		fgets(line,leng,fpIn);
		getNum(control,line,3);

		//get freq
		memset((void*)line,0,leng);
		fgets(line,leng,fpIn);
		getNum2(freq,line,control[2]);

		//result
		numRes = 0;
		keyLeft = 0;

		tmp = 1/3;
		printf("tmp %d\n",tmp);

		//calculate
		for(loop=0;loop<control[2];loop++)
		{
			numRes = numRes + freq[loop] * (keyLeft/control[1] + 1);
			keyLeft++;
		}

		printf("##%d : %d\n",loopSuper+1,(int)numRes);
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

