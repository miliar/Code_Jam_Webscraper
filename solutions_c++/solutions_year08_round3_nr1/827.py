// TextMessagingOutrage.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int freaq[1001];

int compare( const void *arg1, const void *arg2 )
{
	int *a = (int *)arg1;
	int *b = (int *)arg2;
	int c = *a;
	int d = *b;

	if(c > d)
		return -1;
	if(c < d)
		return 1;

	return 0;
}

char s[10000000];

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *input = fopen("c:\\A-small-attempt1.in", "r+");


	fgets(s, 10000, input);
	int N = atoi(s);
	//printf("Count: %d\n", atoi(s));

	int count = 1;
	while(!feof(input))
	{
		if(N == (count - 1))
			break;

		fgets(s, 1000000, input);
		int P = atoi(s); // the maximum number of letters to place on a key
		char *temp = strchr(s, ' ');
		int K = atoi(temp); // the number of keys available 
		temp++;
		temp = strchr(temp, ' ');
		int L = atoi(temp); // the number of letters in our alphabet


		fgets(s, 10000000, input);

		freaq[0] = atoi(s);
		temp = s;

		for(int i = 1; i < L; i++)
		{
			temp = strchr(temp, ' ');
			freaq[i] = atoi(temp);
			temp++;
		}

		qsort(freaq, L, sizeof(int), compare);

		long long number = 0; int index = 0;

		for(int i = 0; i < P; i++)
		{
			for(int j = 0; j < K; j++)
			{
				number += (long long)freaq[index] * (i + 1);
				index++;
				if(index == L)
					break;
			}
			if(index == L)
					break;
		}

		if(index != L)
			printf("Case #%d: impossible\n", count, number);
		else
			printf("Case #%d: %d\n", count, number);

		count++;
	}
	fclose(input);

	return 0;
}
