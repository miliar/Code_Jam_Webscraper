#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

char text[2000];
char newText[2000];
int sLen;

typedef vector<int> VI;

int getRun()
{
	int i;
	int counter = 0;
	for (i = 1; i < sLen; i++)
		if (newText[i] != newText[i-1])
			counter++;
	return counter+1;
}

int main()
{
	int numCase;
	scanf("%d", &numCase);
	int i, j, len;
	for (i = 0; i < numCase; i++)
	{
		scanf("%d", &len);
		scanf("%s", text);
		sLen = strlen(text);
		VI perm = VI(len);
		int minNumRun = 2000;
		for (j = 0; j < len; j++) perm[j] = j;
		do
		{
			int start = 0;
			while (true)
			{
				if (text[start] == '\0') break;
				for (j = 0; j < len; j++)
				{
					newText[start+j] = text[start+perm[j]];
				}
				start += len;
			}
			int numRun = getRun();
			if (numRun < minNumRun)
				minNumRun = numRun;
		} while (next_permutation(perm.begin(), perm.end()));
		printf("Case #%d: %d\n", i+1, minNumRun);
	}
	return 0;
}
