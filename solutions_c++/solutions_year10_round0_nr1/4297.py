// CJ1F2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int func(int N, int K)
{
	int state[15] = {0};
	int power[15] = {0};
	power[0] = 1;

	for(int i = 0; i < K; i ++)
	{
		for(int j = 0; j < N; j ++)
		{
			if(power[j])
			{
				state[j]==0?(state[j]=1):(state[j]=0);
			}
		}

		for(int x = 1; x < N; x ++)
		{
			state[x-1]==1?(power[x]=1):(power[x]=0);
		}
	}

	if(state[N-1] == 1)
	{
		return 1;
	}

	return 0;
}


int main()
{
	int T, N, K;

	FILE *ip;
	FILE *op;
	ip = fopen("A-small-attempt7.in", "r");
	op = fopen("op.txt","w");

	fscanf(ip, "%d", &T);

	for(int i = 0; i < T; i ++)
	{
		fscanf(ip, "%d %d", &N, &K);
		if(func(N, K))
		{
			fprintf(op, "Case #%d: ON\n", i+1, N, K);
		}
		else
		{
			fprintf(op, "Case #%d: OFF\n", i+1, N, K);
		}
	}

	fclose(ip);
	fclose(op);

	return 0;
}

