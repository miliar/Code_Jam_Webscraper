#include <stdio.h>
#include <memory.h>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#pragma warning(disable:4996)
//////////////////////////
// #define SMALL
#ifdef SMALL

#else

#endif

#define MAX_SIZE 256

//////////////////////////
FILE *out;
unsigned int iCase = 1;
unsigned int N;
unsigned int P, K, L;
vector<unsigned int> freqs;
//////////////////////////
unsigned int ReadFile(FILE *file)
{
	freqs.clear();
	fscanf(file, "%d", &P);
	fscanf(file, "%d", &K);
	fscanf(file, "%d", &L);
	if (P * K < L)
	{
		return -1;
	}
	unsigned int i;
	unsigned int f;
	for(i = 1; i <= L; ++i)
	{
		fscanf(file, "%d", &f);
		freqs.push_back(f);
	}

	sort<vector<unsigned int>::iterator>(freqs.begin(), freqs.end());	
	unsigned int value = 0;
	unsigned int pushes = 0;
	while(true)
	{
		++ pushes;
		for(i = 1; i <= K; ++i)
		{
			value += pushes * freqs.back();
			freqs.pop_back();
			if (freqs.size() == 0)
			{
				return value;
			}
		}
	}
}


int main()
{
	char *InName = "A-large.in";
	char *OutName = "A-large.out";

	FILE *file = fopen(InName, "r");
	if (0 == file)
	{
		printf("File can't be opened!\n");
		exit(-1);
	}
	out = fopen(OutName, "w");


	fscanf(file, "%d", &N);

	unsigned int result;
	for(iCase = 1; iCase <= N; ++ iCase)
	{
		result = ReadFile(file);

		if (result > 0)
		{
			fprintf(out, "Case #%d: %d\n", iCase, result);
		}
		else
		{
			fprintf(out, "Case #%d: Impossible\n", iCase);
		}
	}

	fclose(out);
	fclose(file);
	
	return 0;
}