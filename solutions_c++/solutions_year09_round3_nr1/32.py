#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	FILE* input = fopen("input1.txt", "r");
	FILE* output = fopen("output1.txt", "w");
	int t;
	fscanf(input, "%d", &t);
	int i;
	int priority[50];
	priority[0] = 1;
	priority[1] = 0;
	for (i = 2; i < 50; i++)
		priority[i] = i;
	for (i = 0; i < t; i++)
	{
		char word[120];
		fscanf(input, "%s", word);
		int val[256];
		int j;
		int upto = 0;
		int ans[70];
		for (j = 0; j < 256; j++)
			val[j] = -1;
		for (j = 0; j < strlen(word); j++)
		{
			if (val[word[j]] == -1)
			{
				val[word[j]] = priority[upto];
				upto++;
			}
			ans[j] = val[word[j]];
			printf("%d", ans[j]);
		}
		printf("\n");
		long long min = 0;
		long long mult = 1;
		for (j = strlen(word)-1; j >= 0; j--)
		{
			min+=ans[j]*mult;
			mult*=max(2, upto);
		}
		fprintf(output, "Case #%d: %lld\n", i+1, min);
	}
} 