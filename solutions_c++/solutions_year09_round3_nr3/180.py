//============================================================================
// Name        : gcj-1.cpp
// Author      : Thomas 'nickers' Wsuł
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int **mapa = NULL;
int mapaW = 0;
vector<unsigned long> Q;

void newMap(int w)
{
	mapa = new int*[w];
	for (int i = 0; i < w; i++)
	{
		mapa[i] = new int[w];
		memset(mapa[i], -1, w * sizeof(mapa[i][0]));
	}
	mapaW = w;
}

void delMap()
{
	for (int i = 0; i < mapaW; i++)
		delete[] mapa[i];
	delete[] mapa;
	mapa = NULL;
	mapaW = 0;
}

unsigned long calc(int b, int e, int lev = 0)
{
	//for (int i = 0; i < lev; i++)printf("  "); printf("Start: <%d, %d> == %d\n", b, e, mapa[b][e]);

	if (e-b<=0) return 0;

	if (mapa[b][e] == -1)
	{
		unsigned long min = 1000000;

		for (int i = 0; i < Q.size() && Q[i] <= e; i++)
		{
			if (Q[i] >= b)
			{
				unsigned long a = calc(b, Q[i] - 1) + calc(Q[i] + 1, e, lev + 1) + e - b;
				if (a < min)
					min = a;
				//if (b == 0 && e == 19) printf("MM: %d >> %d\n", Q[i], a);
			}
		}

		if (min == 1000000)
			min = 0;

		//printf("[%d:%d]=%d\n", b, e, min);
		mapa[b][e] = min;
	}
	return mapa[b][e];
}

void dp()
{
	puts("--");
	for (int x = -1; x < mapaW; x++) printf("%2d|", x);puts("");
	for (int x = -1; x < mapaW; x++) printf("---");puts("");

	for (int y = 0; y < mapaW; y++)
	{
		printf("%2d|", y);

		for (int x = 0; x < mapaW; x++)
			printf("%3d", mapa[y][x]);
		puts("");
	}
	puts("--");
}

int main()
{
	int N, W, qLen;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		scanf("%d %d", &W, &qLen);

		Q.clear();
		for (int j = 0; j < qLen; j++)
		{
			int prisoner;
			scanf("%d", &prisoner);
			Q.push_back(prisoner - 1);
		}

		newMap(W);
		printf("Case #%d: %lld\n", i, calc(0, W - 1));
//		dp();
		delMap();
	}

	return 0;
}
