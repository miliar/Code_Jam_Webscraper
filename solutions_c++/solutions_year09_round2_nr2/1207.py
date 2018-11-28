// B.cpp : main project file.

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

using namespace std;

int main(array<System::String ^> ^args)
{

	FILE * pFile, *pOut;

	int numCases;
	pFile = fopen ("b.in" , "r");
	pOut= fopen("b.out","w");
	char N[21];
	char smaller[21];
	if (pFile == NULL) perror ("Error opening file");
	else
	{
		fscanf(pFile, "%d\n", &numCases);
		for (int num=0;num<numCases;num++)
		{

			fprintf(pOut,"Case #%d: ",num+1);
			
			int numBases=fscanf(pFile, "%s\n",N);
			
			char last=N[0];
			int nlen=strlen(N);
/*			int insert=-1;
			int remove=-1;
			char min=N[nlen-1];
			smaller[0]=0;
			char smallest=nlen-1;
			for (int i=nlen-1;i>=0;i++){
				if (N[i]<min) {smaller[i]=max=N[i]; smaller[i]=0;}
				else if (N[i]<max) {smaller[i]=1; smallest}
			}
*/
			char found=100;
			char found2=100;
			for (int i=nlen-2;i>=0;i--){

				char smallest=100;
				for (int j=i+1;j<nlen;j++){
					if ((N[j]>N[i])&&(N[j]<=smallest)&&((i>0)||(N[j]>'0'))) {found=i;found2=j;smallest=N[j];}
				}
				if (smallest<100) i=0;
			}
			char insert='0';
			char swap='0';
			if (found2!=100) insert=N[found2];
			if (found!=100)

			{
				swap=N[found];


				for (int i=0;i<found;i++) fprintf(pOut,"%c",N[i]);
				fprintf(pOut,"%c",insert);

				for (int i=nlen-1;i>found;i--)
				{
					if (i==found2) fprintf(pOut,"%c",swap);
					else fprintf(pOut,"%c",N[i]);


				}
			}
			else
			{ // swap not found
				int zeros=0;
				int first=-1;
				for (int i=nlen-1;i>=0;i--){
					if (N[i]=='0') zeros++;
					else
					{
						if (first==-1) {fprintf(pOut,"%c",N[i]); first=i;}
					}
				}
				for (int i=0;i<=zeros;i++) fprintf(pOut,"0");
				for (int i=first-1;i>=0;i--) if (N[i]!='0') fprintf(pOut,"%c",N[i]);
			}

			fprintf(pOut,"\n");

		}
		fclose (pFile);
	}
	return 0;
}
