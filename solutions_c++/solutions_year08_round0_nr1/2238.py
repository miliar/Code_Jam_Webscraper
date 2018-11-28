// SavingTheUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *input = fopen("c:\\A-large.in", "r+");

	char s[10000];
	
	fgets(s, 10000, input);
	//printf("Count: %d\n", atoi(s));

	int count = 1;
	while(!feof(input))
	{
		fgets(s, 10000, input);
		int S = atoi(s); // the number of search engines
		char engines[100][100];
		for(int i = 0; i < S; i++)
			fgets(engines[i], 100, input);
		
		fgets(s, 10000, input);
		int Q = atoi(s); //the number of incoming queries
		char queries[1000][100];
		for(int i = 0; i < Q; i++)
			fgets(queries[i], 100, input);
				

		int Y = 0;

		int deep = 0;
		int querie_start = 0;

		bool done = false;

		while(!done)
		{
			querie_start = deep;

			for(int i = 0; i < S; i++)
			{
				bool ideal = true;
					
				int j;
				for(j = querie_start; j < Q; j++)
				{
					if(strcmp(queries[j], engines[i]) == 0)
					{	
						ideal = false;
						break;
					}
				}
	
				if(ideal)
				{
					done = true;
					break;
				}
				
				if(deep < j)
					deep = j;
			}

			if(!done)
				Y++;
		}

		printf("Case #%d: %d\n", count, Y);
		count++;
	}
	fclose(input);

	return 0;
}

