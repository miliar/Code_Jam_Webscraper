#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

const int MAX = 10;
const int MAXX = 10000;

char mat[MAX][MAX];
int matt[MAX][MAX];
int anig[MAX][MAX];
char row[MAXX];

int which(char c)
{
	switch(c)
	{
		case 'Q':
			return 1;
		case 'W':
			return 2;
		case 'E':
			return 3;
		case 'R':
			return 4;
		case 'A':
			return 5;
		case 'S':
			return 6;
		case 'D':
			return 7;
		case 'F':
			return 8;
		default:
			return 0;
	}
	return -1;
}

int main()
{
	int t, i, n, k, z, j, lenght;
	char a, b, c;
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for(i = 1; i <= t; i++)
	{
		for(j = 0; j < MAX; j++)
			for(k = 0; k < MAX; k++)
				anig[j][k] = 0;
		for(j = 0; j < MAX; j++)
			for(k = 0; k < MAX; k++)
				matt[j][k] = 0;
		scanf("%d", &n);
		for(j = 0; j < n; j++)
		{
			scanf("%c", &a);
			while(which(a) < 1) scanf("%c", &a);
			scanf("%c", &b);
			scanf("%c", &c);
			mat[which(a)][which(b)] = c;
			mat[which(b)][which(a)] = c;
			matt[which(b)][which(a)] = 1;
			matt[which(a)][which(b)] = 1;
		}
		scanf("%d", &n);
		for(j = 0; j < n; j++)
		{
			scanf("%c", &a);
			while(which(a) < 1) scanf("%c", &a);
			scanf("%c", &b);
			scanf("%c", &c);
			anig[which(a)][which(b)] = 1;
			anig[which(b)][which(a)] = 1;
		}
		scanf("%d", &n);
		lenght = 1;
		scanf("%c", &a);
		while(which(a) < 1) scanf("%c", &a);
		row[lenght] = a;
		for(j = 0; j < n - 1; j++)
		{
			scanf("%c", &a);
			if(lenght == 0)
				row[++lenght] = a;
			else
			{
				if(matt[which(a)][which(row[lenght])] == 1)
				{
					row[lenght] = mat[which(a)][which(row[lenght])];
				}
				else
				{
					for(k = 1; k <= lenght; k++)
					{
						if(anig[which(row[k])][which(a)] == 1)
						{
							lenght = 0;
						}
					}
					if(lenght != 0)
					{
						row[++lenght] = a;
					}
				}
			}
		}
		if(lenght != 0)
		{
			printf("Case #%d: [", i);
			for(j = 1; j < lenght; j++)
			{
				printf("%c, ", row[j]);
			}
			printf("%c]\n", row[lenght]);
		}
		else
		{
			printf("Case #%d: []\n", i);
		}
	}
    return 0;
}
