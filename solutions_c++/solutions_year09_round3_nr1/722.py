// A.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
#include <stdio.h>
#include <assert.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
#include <set>

#define ll long long

using namespace std;

int main(array<System::String ^> ^args)
{

	FILE * pFile, *pOut;


	int order[37]={1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36};
	int value[37];
	int numCases;
	char buffer[62];
	pFile = fopen ("a.in" , "r");
	pOut= fopen("a.out","w");
	if (pFile == NULL) perror ("Error opening file");
	else
	{
		fscanf(pFile, "%d\n", &numCases);
		for (int num=0;num<numCases;num++)
		{
			for (int i=0;i<37;i++) value[i]=-1;
			fprintf(pOut,"Case #%d: ",num+1);
			fscanf(pFile,"%s\n",&buffer);
			int buflen=strlen(buffer);
			for (int i=0;i<buflen;i++){
				if ((buffer[i]>='0')&&(buffer[i]<='9')) buffer[i]-='0';
				else buffer[i]-='a'-10;
			}
			ll result=0;
			int numDig=0;

			for (int i=0;i<buflen;i++){
				if (value[buffer[i]]==-1){
					value[buffer[i]]=order[numDig];
					numDig++;
				}
			}

			if (numDig<2) numDig=2;
			for (int i=0;i<buflen;i++){
				result*=numDig;
				result+=value[buffer[i]];
			}
			fprintf(pOut,"%lld\n",result);
		}
		fclose (pFile);
	}
	return 0;
}
