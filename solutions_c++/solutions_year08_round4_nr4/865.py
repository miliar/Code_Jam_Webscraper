#include <stdio.h>
#include <memory.h>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_SIZE 256
#define MAX_LENGTH 5001
FILE *out;

char S[MAX_LENGTH];
char T[MAX_LENGTH];
int iCase = 1;
int N;
int k;
vector<int> permutation(16);
//////////////////////////
int ReadFile(FILE *file)
{
	int i, j;
	int minGroups = 999999;
	bool isContinue = true;


	fscanf(file, "%d", &k);
		fscanf(file, "%s", S);
	permutation.clear();
	permutation.resize(k);



	for(i = 1; i <= k; ++i)
	{
		permutation[i - 1] = i;
	}

	while(isContinue)
	{

		int len = strlen(S);
		int times = len / k;
		int begin = 0;
		for(i = 0; i < times; ++i)
		{			
			for(j = 0; j < k; ++j)
			{
				T[begin + j] = S[begin + permutation[j] - 1];
			}
			begin += k;
		}

		int groups = 0;
		char last = 0;
		for(i = 0; i < len; ++i)
		{
			if (T[i] != last)
			{
				groups++;
				last = T[i];
			}
		}

		if (groups < minGroups)
		{
			minGroups = groups;
		}

		isContinue = next_permutation(permutation.begin(), permutation.end());
	}

	return minGroups;
}


int main()
{
	char *filenamein = "D-small-attempt0.in";
//	char *filenamein = "input.txt";
	char *filenameout = "output.txt";   

	FILE *file = fopen(filenamein, "r");

	FILE *out = fopen(filenameout, "w");


	fscanf(file, "%d", &N);
	for(iCase = 1; iCase <= N; ++ iCase)
	{

		fprintf(out, "Case #%d: %d\n", iCase, ReadFile(file));
	}
	fclose(out);
	fclose(file);
	return 0;
}