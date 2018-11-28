#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <stdio.h>
using namespace std;
#define NODES_COUNT 50


int LeastGoOn = NODES_COUNT;
int CalculateNodes[NODES_COUNT];
int Circles[NODES_COUNT];
int node[NODES_COUNT];
int FlexNodes[NODES_COUNT];
int m, v;

void main()
{
	int CaseCount;
	int ci, tx, ty;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &CaseCount);
	for(int cases = 0; cases < CaseCount; cases++)
	{
		scanf("%d%d", &m, &v);
		for(ci = 1; ci <= m / 2; ci++)
		{
			scanf("%d%d", &tx, &ty);
			node[ci] = tx;
			FlexNodes[ci] = ty;
		}
		for(ci = m / 2 + 1; ci <= m; ci++)
		{
			scanf("%d", &tx);
			node[ci] = tx;
			CalculateNodes[ci] = tx;
		}
		
		for(ci = 1; ci <= m / 2; ci++)
		{
			if(FlexNodes[ci] == 1)
			{
				Circles[ci] = 0;
			}
			else
			{
				Circles[ci] = node[ci];
			}
		}
		LeastGoOn = NODES_COUNT;
		while(true)
		{
			for(ci = m / 2; ci >= 1; ci--)
			{
				if(Circles[ci] == 1)
				{
					CalculateNodes[ci] = CalculateNodes[ci * 2] 
				& CalculateNodes[ci * 2 + 1];
				}
				else
				{
					CalculateNodes[ci] = CalculateNodes[ci * 2] 
				| CalculateNodes[ci * 2 + 1];
				}
			}
			if(CalculateNodes[1] == v)
			{
				tx = 0;
				for(ci = 1; ci <= m / 2; ci++)
				{
					if(Circles[ci] != node[ci])
					{
						tx++;
					}
				}
				if(tx < LeastGoOn)
				{
					LeastGoOn = tx;
				}
			}

			for(ci = m / 2; ci >= 1; ci--)
			{
				if(1 == FlexNodes[ci])
				{
					++ Circles[ci];
					if(Circles[ci] < 2)
					{
						break;
					}
					Circles[ci] = 0;
				}
			}
			if(ci < 1)
			{
				break;
			}
		}
		
		if(LeastGoOn < 50)
		{
			printf("Case #%d: %d\n", cases + 1, LeastGoOn);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", cases + 1);
		}
	}

	return;
}