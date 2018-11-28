//============================================================================
// Name        : bribe_the_prisoners.cpp
// Author      : Kinshul Verma
// Version     :
// Copyright   : !!!MIT License!!!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
#include <limits.h>
using namespace std;

int cells[100], num_cells, prisoners, cases, max_coins = INT_MAX, permut[100],
		inside[100];
int holes[100];

void genPermut(int pos)
{
	if (pos == num_cells)
	{
		int count = 0;
		memset(holes, 0, 100* sizeof (int));
		for (int i = 0; i < num_cells; i++)
		{
			holes[permut[i]]=-1;
			for (int j = permut[i] + 1; j < prisoners; j++)
			{
				if (holes[j] == -1)
					break;
				else
					++count;
			}
			for (int j = permut[i] - 1; j >= 0; j--)
			{
				if (holes[j] == -1)
					break;
				else
					++count;
			}
		}
		if(count<max_coins)max_coins = count;
	}
	else
	{
		for(int i=0; i<num_cells; i++)
		{
			if(inside[cells[i]]!=1)
			{
				permut[pos]=cells[i];
				inside[cells[i]]=1;
				genPermut(pos+1);
				inside[cells[i]]=0;
			}
		}
	}
}

int main()
{
	int temp;
	scanf("%d", &cases);
	for (int var = 1; var <= cases; var++)
	{
		scanf("%d%d", &prisoners, &num_cells);
		memset(cells, 0, sizeof(int) * 100);
		memset(inside, 0, sizeof(int) * 100);
		memset(permut, 0, sizeof(int) * 100);
		max_coins = INT_MAX;
		for (int i = 0; i < num_cells; i++)
		{
			scanf("%d", &temp);
			cells[i]=temp-1;
		}
		/*
		printf("Cells: ");
		for (int i = 0; i < num_cells; i++)
			printf("%d ", cells[i]);
		printf("\n");
		*/
		genPermut(0);
		printf("Case #%d: %d\n", var, max_coins);
	}
	return 0;
}
