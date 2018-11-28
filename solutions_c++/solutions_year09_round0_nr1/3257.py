// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

typedef struct _node
{
	char *chs;
	struct _node *next;
}node;

#define INFILE "c:\\A-small.in"
#define OUTFILE "c:\\A-small.out"
#define PT_SIZE 30
#define TEXT_SIZE 1000
#define L_SIZE 15
#define ALPHA 26
//#define DBG
int _tmain(int argc, _TCHAR* argv[])
{
	node *head, *rear, *temp;
	char *strD[PT_SIZE];
	char *strN[TEXT_SIZE];
	char garbg[TEXT_SIZE];
	int result[L_SIZE];
	char set[L_SIZE][ALPHA];
	memset(result, 0, L_SIZE*sizeof(int));
	int equal;
	int ok;
	int inParent;
	int L, D, N;
	FILE *in, *out;
	int i, j, k, m, p;
	//node charlist[15];

	if((in = fopen(INFILE, "r")) == NULL)
	{
		perror("Fail to open file.");
		exit(-1);
	}
	if((out = fopen(OUTFILE, "a")) == NULL)
	{
		perror("Fail to open file.");
		exit(-1);
	}
	fscanf(in, "%d%d%d", &L, &D, &N);
#ifdef DBG
	printf("L:%d, D:%d, N:%d\n", L, D, N);
#endif
	fgets(garbg, TEXT_SIZE, in);
	for(i = 0; i < D; i++)
	{
		strD[i] = (char*)malloc(TEXT_SIZE);
		fgets(strD[i], TEXT_SIZE, in);
#ifdef DBG
		if(i >= 0)
			printf("strD[%d] is: %s, and its length is %d\n", i, strD[i], strlen(strD[i]));
#endif
	}
	for(i = 0; i < N; i++)
	{
		strN[i] = (char*)malloc(TEXT_SIZE);
		fgets(strN[i], TEXT_SIZE, in);
#ifdef DBG
		printf("strN[%d] is: %s, and its length is %d\n", i, strN[i], strlen(strN[i]));
#endif
	}

	for(i = 0; i < N; i++)
	{
		p = 0;
		memset(set, 0, L_SIZE*ALPHA);
		inParent = 0;
		for(j = 0; j < strlen(strN[i]) -1; j++)
		{
			if(strN[i][j] == '(')
			{
#ifdef DBG
				printf("(\n");
#endif
				inParent = 1;
			}
			else if(strN[i][j] == ')')
			{
#ifdef DBG
				printf(")\n");
#endif
				inParent = 0;
				p++;
			}
			else if (islower(strN[i][j]) && inParent)
			{
#ifdef DBG
				printf("position:%d,%d, content:%c\n", p, (int)strN[i][j]-97, strN[i][j]);
#endif
				set[p][((int)strN[i][j]-97)] = strN[i][j];
			}
			else if(islower(strN[i][j]) && !inParent)
			{
#ifdef DBG
				printf("position:%d,%d, content:%c\n", p, (int)strN[i][j]-97, strN[i][j]);
#endif
				set[p][((int)strN[i][j]-97)] = strN[i][j];
				p++;
			}
			else
			{}
#ifdef DBG
				perror("ri...\n");
#endif
		}
#ifdef DBG
		printf("set is:\n");
		for(j = 0; j < L; j++)
		{
			for(k = 0; k < ALPHA; k++)
				printf("%c ", set[j][k]);
			printf("\n");
		}
#endif

		for(k = 0; k < D; k++)
		{
			ok = 1;
			for(m = 0; m < strlen(strD[k]) - 1; m++)
			{
				equal = 0;
				for(j = 0; j < ALPHA; j++)
				{
					if(strD[k][m] == set[m][j])
					{
						equal = 1;
						break;
					}
				}
				if(!equal)
				{
					ok = 0;
					break;
				}
			}
			if(ok)
			{
				result[i] ++;
#ifdef DBG
				printf("#%d is ok once\n", i);
#endif
			}
		}
		
	}
	for(i = 0; i < N; i++)
		fprintf(out, "Case #%d: %d\n", i+1, result[i]);
	fclose(in);
	fclose(out);


	return 0;
}

