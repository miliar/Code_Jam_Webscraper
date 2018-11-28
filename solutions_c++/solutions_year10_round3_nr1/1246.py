// Rounnd1C1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <string.h>

#define TEMP_LIST_LEN 11
//functions declaration

//////////////////////////
int _tmain(int argc, _TCHAR* argv[])
{
	FILE*   inFileHandle;
	FILE*   outFileHandle;
	int  i,j,inFileLen,outLen=0,T=0,k=0,count=0,x=0,sol=0;
	int hArr[1001][2];
	memset(hArr,0,2002);
	char *pInFile,*pInFile1,*pInFile2;
	outFileHandle = fopen("A-large.out","w+");//Prepare output file
	char pOutFile[50]="Case #";
	char tmpList[TEMP_LIST_LEN];//Temp list for reading and decoding the input file
	memset(tmpList,0,TEMP_LIST_LEN);
	char tmpList1[TEMP_LIST_LEN];//Temp list for reading and decoding the input file
	memset(tmpList1,0,TEMP_LIST_LEN);
//////    Read input file    //////////////////////////////////////////////
	inFileHandle = fopen("A-large.in","r");//Open input file 
	fseek (inFileHandle , 0 , SEEK_END);// seek to end of file
	inFileLen = ftell (inFileHandle);// get current file pointer
	fseek(inFileHandle, 0, SEEK_SET); // seek back to beginning of file
	pInFile = new char[inFileLen+1];
	memset(pInFile,0,inFileLen+1);
	fread(pInFile,sizeof(char),inFileLen,inFileHandle);//Read input file
	pInFile1 = pInFile;
	pInFile2 = pInFile; 
//////////////////////////////////////////////////////////////////////////
	T = atoi(pInFile);// T cases

	for(i=0;i<T;i++)
	{
		memset(tmpList,0,TEMP_LIST_LEN);
		pInFile1 = strstr(pInFile1,"\n")+1;
		pInFile2 = strstr(pInFile1,"\n");
		strncpy(tmpList,pInFile1,pInFile2-pInFile1);
		x = atoi(tmpList);
		for(j=0;j<x;j++)
		{
			memset(tmpList,0,TEMP_LIST_LEN);
			pInFile1 = pInFile2+1;
			pInFile2 = strstr(pInFile1," ");
			strncpy(tmpList,pInFile1,pInFile2-pInFile1);
			hArr[j][1] = atoi(tmpList);//Ai

			memset(tmpList,0,TEMP_LIST_LEN);
			pInFile1 = pInFile2+1;
			if(j==x-1 && i==T-1)
			{
				pInFile2 = inFileLen+pInFile;
			}
			else
				pInFile2 = strstr(pInFile1,"\n");
			strncpy(tmpList,pInFile1,pInFile2-pInFile1);
			hArr[j][2] = atoi(tmpList);//Bi
		}
		count=0;sol=0;
		for(j=0;j<x;j++)
		{
			for(k=j;k<x;k++)
			{
				if((sol=hArr[j][1]-hArr[k][1])*(hArr[j][2]-hArr[k][2])<0)
					count++;
			}

		}
		//Write solution to output file
		memset(pOutFile,0,50);
		outLen = sprintf(pOutFile,"Case #%d: %d\n",i+1,count);
		fwrite(pOutFile,sizeof(char),outLen,outFileHandle);

		
	}



	return 0;
}

//functions implementation
