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
int iCase = 1;
int N;
int k;
char S[5001];
char T[5001];
vector<int> per(16);
//////////////////////////
int ReadFile(FILE *file)
{
	fscanf(file, "%d", &k);
	fscanf(file, "%s", S);
	//printf("%s\n", S);

	per.clear();
	per.resize(k);
	int i, j;
	for(i = 1; i <= k; ++i)
	{
		per[i - 1] = i;
	}

	int minGroups = 999999;

	bool isContinue = true;
	while(isContinue)
	{
		//for(j = 0; j < k; ++j)
		//{
		//	printf("%d, ", per[j]);
		//}
		//printf("\n");

		int len = strlen(S);
		int times = len / k;
		int begin = 0;
		for(i = 0; i < times; ++i)
		{			
			for(j = 0; j < k; ++j)
			{
				T[begin + j] = S[begin + per[j] - 1];
			}
			begin += k;
		}

		int groups = 0;
		char last = 0;
		for(i = 0; i < len; ++i)
		{
			if (T[i] != last)
			{
				++ groups;
				last = T[i];
			}
		}

		if (groups < minGroups)
		{
			minGroups = groups;
		}

		isContinue = next_permutation(per.begin(), per.end());
	}

	return minGroups;
}


int main()
{
	char *InName = "D-small-attempt0.in";
	char *OutName = "D-small-attempt0.out";

	FILE *file = fopen(InName, "r");
	if (0 == file)
	{
		printf("File can't be opened!\n");
		exit(-1);
	}
	out = fopen(OutName, "w");


	fscanf(file, "%d", &N);

	for(iCase = 1; iCase <= N; ++ iCase)
	{

		fprintf(out, "Case #%d: %d\n", iCase, ReadFile(file));
	}

	fclose(out);
	fclose(file);
	
	return 0;
}