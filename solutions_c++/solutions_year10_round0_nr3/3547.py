// CJ3F.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int func(int R, int k, int N, int g[20])
{
	int flag;
	int cost = 0;
	int rides = 0;
	int people, groups;

	while(rides < R)
	{
		people = 0;
		groups = 0;
		while(1)
		{
			if((people + g[1] <= k) && (groups++ < N))
			{
				people += g[1];
				cost += g[1];
				int temp = g[1];
				for(int j = 1; j < N; j ++)
				{
					g[j] = g[j + 1];
				}
				g[N] = temp;
			}
			else
			{
				rides++;
				break;
			}
		}
	}
	return cost;
}

int main()
{
	int T, R, k, N;
	int g[20] = {0};
	int EURO;
	FILE *ip;
	FILE *op;

	ip = fopen("C-small-attempt1.in", "r");
	op = fopen("op.txt", "w");

	fscanf(ip, "%d", &T);

	for(int i = 1; i <= T; i ++)
	{
		fscanf(ip, "%d %d %d", &R, &k, &N);
		for(int j = 1; j <= N; j ++)
		{
			fscanf(ip, "%d", &g[j]);
		}

		EURO = func(R, k, N, g);
		fprintf(op, "Case #%d: %d\n", i, EURO);
	}

	return 0;
}