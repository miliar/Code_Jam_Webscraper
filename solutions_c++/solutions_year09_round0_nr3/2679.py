// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TEXT_SIZE 600
#define STACK_SIZE 10000
#define INFILE "C:\\C-small.in"
#define OUTFILE "C:\\C-small.out"
//#define DBG1 
int _tmain(int argc, _TCHAR* argv[])
{
	//variables
	const char wel[] = "welcome to code jam";
	int lev[STACK_SIZE];
	int num[STACK_SIZE];
	int c_lev = 0;
	int c_num = 0;
	int top = 0;
	int result = 0;
	int i = 0;
	int j = 0;
	int n = 0;
	FILE *in, *out;
	char tmp[TEXT_SIZE];
	memset(lev, 0, STACK_SIZE * sizeof(int));
	memset(num, 0, STACK_SIZE * sizeof(int));
	memset(tmp, 0, TEXT_SIZE);

	//open file and get the input
	if((in = fopen(INFILE, "r")) == NULL)
	{
		perror("Fail to open file");
		exit(1);
	}
	if((out = fopen(OUTFILE, "w")) == NULL)
	{
		perror("Fail to open file");
		exit(1);
	}
#ifdef DBG
	fgets(tmp, TEXT_SIZE-1, in);
	n = atoi(tmp);
	printf("N in debug is %d\n", n);
	fgets(tmp, TEXT_SIZE-1, in);
	printf("tmp in debug is %s", tmp);
#endif
	fgets(tmp, TEXT_SIZE - 1, in);
	n = atoi(tmp);
#ifdef DBG1
	printf("N is: %d\n", n);
#endif
	for(i = 0; i < n; i++)
	{
		//init for another line
		c_lev = 0;
		c_num = 0;
		top = 0;
		result = 0;
		memset(lev, 0, STACK_SIZE * sizeof(int));
		memset(num, 0, STACK_SIZE * sizeof(int));
		memset(tmp, 0, TEXT_SIZE);

		//get the data line
		fgets(tmp, TEXT_SIZE, in);
#ifdef DBG1
		printf("The raw input is: %s\n", tmp);
#endif
#ifdef DBG
		printf("Input the string...\n");
		gets(tmp);
		printf("The input is:%s\nThe length of input is %d\n", tmp, strlen(tmp));
#endif
		//push lev20 & num len(tmp) into stacks
		lev[top] = 19;
		num[top++] = strlen(tmp) - 1; 

		//loop, while stack is not empty
		while(top > 0)
		{
#ifdef DBG
			printf("lev is: ");
			for(i = 0; i < top; i++)
			{
				printf("%d ", lev[i]);
			}
			printf("\n");
			printf("num is: ");
			for(i = 0; i < top; i++)
			{
				printf("%d ", num[i]);
			}
			printf("\n");
			printf("top is: %d, c_lev is: %d, c_num is: %d, answer is :%d\n", top, c_lev, c_num, result);
#endif
			//pop
			c_lev = lev[--top];
			c_num = num[top];
#ifdef DBG
			printf("lev is: ");
			for(i = 0; i < top; i++)
			{
				printf("%d ", lev[i]);
			}
			printf("\n");
			printf("num is: ");
			for(i = 0; i < top; i++)
			{
				printf("%d ", num[i]);
			}
			printf("\n");
			printf("top is: %d, c_lev is: %d, c_num is: %d, answer is :%d\n", top, c_lev, c_num, result);
#endif
			//if reached the leaves
			if(c_lev == 0)
			{
				result++;
				continue;
			}

			//scan
			for(j = 0; j <= c_num; j++)
			{
				if(tmp[j] == wel[c_lev -1])
				{
					lev[top] = c_lev -1;
					num[top++] = j;
				}
			}

		}
		
		//output the result
		//result = result%10000;
		fprintf(out, "Case #%d: %.4d\n", i+1, result%10000);
	}
	fclose(in);
	fclose(out);
	return 0;
}

