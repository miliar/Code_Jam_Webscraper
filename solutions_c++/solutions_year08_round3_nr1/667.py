#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

long solveTestCase(FILE* fin)
{
	long maxKeyLetters, keyCount, letterCount;
	
	fscanf(fin, "%ld", &maxKeyLetters);
	fscanf(fin, "%ld", &keyCount);
	fscanf(fin, "%ld", &letterCount);

	long* letterFrequencies = (long*)malloc(letterCount * sizeof(long));
		
	for(long i = 0; i < letterCount; i++)
	{
		fscanf(fin, "%ld", &letterFrequencies[i]);
		/*
		if(letterFrequencies[i] == 0)
		{
			letterCount--;
			i--;
		}
		*/
	}

	if(maxKeyLetters * keyCount < letterCount)
	{
		free(letterFrequencies);
		return -1;
	}
		
	//sort them by freq
	for(long i = 0; i < letterCount; i++)
		for(long j = i; j < letterCount; j++)
		{
			if(letterFrequencies[i] < letterFrequencies[j])
			{
				long tmp = letterFrequencies[i];
				
				letterFrequencies[i] = letterFrequencies[j];
				
				letterFrequencies[j] = tmp;
			}
		}
		
//	for(long i = 0; i < letterCount; i++)
//		printf("\n### %ld", letterFrequencies[i]);
		
	long keyPresses = 0;

	long usedKeyCount = 0;
	long letterPosition = 1;
	for(long i = 0; i < letterCount; i++)
	{
		usedKeyCount++;
		
		if(usedKeyCount > keyCount)
		{
			usedKeyCount = 1;
			letterPosition++;
		}
		
		keyPresses += letterPosition * letterFrequencies[i];
	}
		
	free(letterFrequencies);
	
	return keyPresses;
}

int main()
{
	FILE* fin = fopen("a.in.txt", "rb");
	FILE* fout = fopen("a.out.txt", "wb");

	long testCaseCount;
	
	fscanf(fin, "%ld", &testCaseCount);
	
	for(long i = 0; i < testCaseCount; i++)
	{
		long result = solveTestCase(fin);

		if(result == -1)
			fprintf(fout, "Case #%ld: impossible\n", i + 1);
		else
			fprintf(fout, "Case #%ld: %ld\n", i + 1, result);
	}
	
	printf("press any key");
	getch();
	
	return 0;
}
