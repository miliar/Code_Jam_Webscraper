// GoogleCodeJam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include "ctype.h"
#include <deque>
#include "assert.h"

#define MAX_STR_LENGTH 10240
using namespace std;

typedef deque<long int> LINTQ;

LINTQ coasters, waittingQ;
long int R, K, N;
long int money;

void LoadPeople()
{
	long int available = K;
	for(int i=0; i<N; i++)
	{
		long int groupSize=waittingQ.front();
		if(groupSize<=available)
		{
			available-=groupSize;
			waittingQ.pop_front();
			coasters.push_back(groupSize);
			money += groupSize;
		}
	}
}

void ReleasePeople()
{
	int size = coasters.size();
	long int value;
	for(int i=0; i<size; i++)
	{
		value=coasters.front();
		coasters.pop_front();
		waittingQ.push_back(value);
	}
}

void processData(char* data)
{
	long int offset = 0;
	long int value;
	while(offset < 10240)
	{
		if(data[offset]=='\0')
			break;
		if(isdigit(data[offset]))
		{
			value = atoi(&data[offset]);
			waittingQ.push_back(value);
			while(isdigit(data[offset]))
				offset ++;
		}
		//else if(data[offset]!= ' ')
		//	break;
		offset ++;
	}
	money=0;
	for(long int i=0; i<R; i ++)
	{
		LoadPeople();
		ReleasePeople();
	}

}


int _tmain(int argc, _TCHAR* argv[])
{
	
	int T;
	FILE* fp =fopen("C-small-attempt0.in", "r");
	assert(fp!=NULL);
	FILE* fpResult =fopen("result.txt", "w");
	assert(fpResult!=NULL);
	char tmp[MAX_STR_LENGTH];
	fgets(tmp, MAX_STR_LENGTH, fp);
	sscanf(tmp, "%d", &T);
	for(long int i=0; i<T; i++)
	{
		fgets(tmp, MAX_STR_LENGTH, fp);
		sscanf(tmp, "%d %d %d", &R, &K, &N);
		memset(tmp, 0, MAX_STR_LENGTH*sizeof(char));
		fgets(tmp, MAX_STR_LENGTH, fp);
		processData(tmp);
		fprintf(fpResult, "Case #%d: %ld\n", i+1, money);
		printf("Case #%d: %ld\n", i, money);
		coasters.clear();
		waittingQ.clear();
	}
	
	

	fclose(fp);
	fclose(fpResult);
	return 0;
}

