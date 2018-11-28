// Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <string.h>

bool checkonOff(int N,int K);
int _tmain(int argc, _TCHAR* argv[])
{
	FILE*   inFileHandle;
	FILE*   outFileHandle;

	int  i,T=0,K=0,N=0;
	inFileHandle = fopen("A-large.in","r"); 
	fseek (inFileHandle , 0 , SEEK_END);
	int	len = ftell (inFileHandle);
	char *inList = new char[len+1];
	memset(inList,0,len+1);
	fclose(inFileHandle);
	inFileHandle = fopen("A-large.in","r"); 
	outFileHandle = fopen("A-large.out","w+"); 

	fread(inList,sizeof(char),len,inFileHandle);
	char *pInList1 = inList;
	char *pInList2 = inList;
	char tmpList[10];
	char outList[20]="Case #";
	bool onOff = true;
	memset(tmpList,0,10);
	T = atoi(inList);
	int outLen = 0;

	for(i=0;i<T-1;i++)
	{
		pInList1 = strstr(pInList1,"\n")+1;
		pInList2 = strstr(pInList1," ");
		strncpy(tmpList,pInList1,pInList2-pInList1);
		N = atoi(tmpList);
		memset(tmpList,0,10);

		pInList1 = strstr(pInList1," ")+1;
		pInList2 = strstr(pInList1,"\n");
		strncpy(tmpList,pInList1,pInList2-pInList1);
		K = atoi(tmpList);
		memset(tmpList,0,10);

		onOff = checkonOff(N,K);
		if(onOff==true)
		{
			outLen = sprintf(outList,"Case #%d: ON\n",i+1);
			fwrite(outList,sizeof(char),outLen,outFileHandle);
		}
		else
		{
			outLen = sprintf(outList,"Case #%d: OFF\n",i+1);
			fwrite(outList,sizeof(char),outLen,outFileHandle);
		}
	}
	pInList1 = strstr(pInList1,"\n")+1;
	pInList2 = strstr(pInList1," ");
	strncpy(tmpList,pInList1,pInList2-pInList1);
	N = atoi(tmpList);
	memset(tmpList,0,10);

	pInList1 = strstr(pInList1," ")+1;

	strncpy(tmpList,pInList1,(inList+len)-pInList1);
	K = atoi(tmpList);
	memset(tmpList,0,10);

	onOff = checkonOff(N,K);
	if(onOff==true)
	{
		outLen = sprintf(outList,"Case #%d: ON\n",T);
		fwrite(outList,sizeof(char),outLen,outFileHandle);
	}
	else
	{
		outLen = sprintf(outList,"Case #%d: OFF\n",T);
		fwrite(outList,sizeof(char),outLen,outFileHandle);
	}


	//////////////////////////////////////////
	fclose(outFileHandle); 
	fclose(inFileHandle); 

	return 0;
}
bool checkonOff(int N,int K)
{
	bool onOff=false;int a=0;
	switch(N)
	{
	case 1:
		if((K&1)==1)
			onOff=true;
		break;
	case 2:
		if((K&3)==3)
			onOff=true;
		break;
	case 3:
		if((K&7)==7)
			onOff=true;
		break;
	case 4:
		if((K&15)==15)
			onOff=true;
		break;
	case 5:
		if((K&31)==31)
			onOff=true;
		break;
	case 6:
		if((K&63)==63)
			onOff=true;
		break;
	case 7:
		if((K&127)==127)
			onOff=true;
		break;
	case 8:
		if((K&255)==255)
			onOff=true;
		break;
	case 9:
		if((K&511)==511)
			onOff=true;
		break;
	case 10:
		if((K&1023)==1023)
			onOff=true;
		break;
	case 11:
		if((K&0x7ff)==0x7ff)
			onOff=true;
		break;
	case 12:
		if((K&0xfff)==0xfff)
			onOff=true;
		break;
	case 13:
		if((K&0x1fff)==0x1fff)
			onOff=true;
		break;
	case 14:
		if((K&0x3fff)==0x3fff)
			onOff=true;
		break;
	case 15:
		if((K&0x7fff)==0x7fff)
			onOff=true;
		break;
	case 16:
		if((K&0xffff)==0xffff)
			onOff=true;
		break;
	case 17:
		if((K&0x1ffff)==0x1ffff)
			onOff=true;
		break;
	case 18:
		if((K&0x3ffff)==0x3ffff)
			onOff=true;
		break;
	case 19:
		if((K&0x7ffff)==0x7ffff)
			onOff=true;
		break;
	case 20:
		if((K&0xfffff)==0xfffff)
			onOff=true;
		break;
	case 21:
		if((K&0x1fffff)==0x1fffff)
			onOff=true;
		break;
	case 22:
		if((K&0x3fffff)==0x3fffff)
			onOff=true;
		break;
	case 23:
		if((K&0x7fffff)==0x7fffff)
			onOff=true;
		break;
	case 24:
		if((K&0xffffff)==0xffffff)
			onOff=true;
		break;
	case 25:
		if((K&0x1ffffff)==0x1ffffff)
			onOff=true;
		break;
	case 26:
		if((K&0x3ffffff)==0x3ffffff)
			onOff=true;
		break;
	case 27:
		if((K&0x7ffffff)==0x7ffffff)
			onOff=true;
		break;
	case 28:
		if((K&0xfffffff)==0xfffffff)
			onOff=true;
		break;
	case 29:
		if((K&0x1fffffff)==0x1fffffff)
			onOff=true;
		break;
	case 30:
		if((K&0x3fffffff)==0x3fffffff)
			onOff=true;
		break;

	}
	return onOff;
}
