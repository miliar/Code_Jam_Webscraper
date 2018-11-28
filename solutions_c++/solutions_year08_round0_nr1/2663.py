// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"

void ReadString(FILE *f, char *str) {
	char c;
	int p=0;
	do {
		c = fgetc(f);
		str[p++] = c;
	} while (!feof(f) && c!=0 && c!='\n'/* && c!=' '*/);
	str[p-1] = 0;
}

void ReadNumber(FILE *f, int &num) {
	char txt[100];
	ReadString(f,txt);
	num = atoi(txt);
}

long long Pow(int a, int b) {
	long long v = 1;
	for (int i=0; i<b; i++) 
		v *= a;
	return v;
}

int FindChar(char item, char* str) {
	int len = strlen(str);
	for (int i=0; i<len; i++)
		if (item==str[i]) 
			return i;
	return 0;
}

void Run(char engine[150][100], char query[150][1000], int numE, int numQ) {
	int i,j,current = -1, find, result = 0;
	bool found[100], start = true;
	
	for (i=0; i<numQ; i++) {
		if (start) {
			start = false;
			find = numE;
			for (j=0; j<numE; j++)
				if (j==current) {
					found[j] = true;
					find--;
				}
				else
					found[j] = false;
		}

		for (j=0; j<numE; j++)  {
			if (strcmp(query[i],engine[j])==0) {
				if (found[j]==false) {
					found[j]=true;
					find--;
					if (find==0) {
						current = j;
						result++;					
						start = true;
					}
				}
				break;
		}	}
	}

	printf("%d",result);
}

int _tmain(int argc, _TCHAR* argv[])
{
	char engine[150][100];
	char query[150][1000];
	int i, j, num, numE, numQ;
	FILE *f;
	f = fopen("A-small.in","r");
	if (!f) return 0;
	ReadNumber(f,num);
	for (i=0; i<num; i++) {
		////////////////
		// Read datas //
		////////////////
		ReadNumber(f,numE);
		for (j=0; j<numE; j++)
			ReadString(f,engine[j]);
		ReadNumber(f,numQ);
		for (j=0; j<numQ; j++)
			ReadString(f,query[j]);
		/////////////////
		// Show result //
		/////////////////
		printf("Case #%d: ",i+1);
		Run(engine, query, numE, numQ);
		printf("\n");
	}
	fclose(f);
	return 0;
}

