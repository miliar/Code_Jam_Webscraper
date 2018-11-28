// GoogleCodeJam1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include "assert.h"
#include <string.h>

typedef struct _item
{
	int bPower;
	int status;
}item;

item Snapper[30];
int nCase, N;
long int K;

#define MAX_STR_LENGTH 102400
void initArray()
{
	for(int i=0; i<N; i++)
	{
		Snapper[i].bPower=0;
		Snapper[i].status=0;
	}
}

void checkArray()
{
	Snapper[0].bPower=1;
	Snapper[0].status = (Snapper[0].status+1)%2;
	for(int i=1; i<N; i++)
	{
		if(Snapper[i].bPower==1)
		{
			Snapper[i].status = (Snapper[i].status+1)%2;
		}
	}
	for(int i=1; i<N; i++)
	{
		if((Snapper[i-1].bPower==0)||(Snapper[i-1].status==0))
		{
			Snapper[i].bPower=0;
		}
		else
			Snapper[i].bPower=1;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fp =fopen("A-small-attempt0.in", "r");
	FILE* fpResult =fopen("result.txt", "w");
	assert(fp!=NULL);
	char tmp[MAX_STR_LENGTH];
	memset(tmp, 0, MAX_STR_LENGTH*sizeof(char));
	fgets(tmp, MAX_STR_LENGTH, fp);
	sscanf(tmp, "%d", &nCase);
	for(int i=0; i<nCase; i++)
	{
		initArray();
		memset(tmp, 0, MAX_STR_LENGTH*sizeof(char));
		fgets(tmp, MAX_STR_LENGTH, fp);
		sscanf(tmp, "%d %ld", &N, &K);
		char * result;
		for(long int j=0; j<K; j++)
		{
			checkArray();
		}
		if((Snapper[N-1].bPower==1)&&(Snapper[N-1].status==1))
			result="ON";
		else
			result="OFF";
		printf("Case #%d: %s\n", i+1, result);
		fprintf(fpResult,"Case #%d: %s\n", i+1, result);
	}
	fclose(fp);
	fclose(fpResult);
	return 0;
}

