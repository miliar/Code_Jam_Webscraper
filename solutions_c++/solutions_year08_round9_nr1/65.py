#include <stdlib.h>
#include <stdio.h>

const int START = 1;
const int END = 2;

struct Entry
{
	int value;
	int type;
};

int compareEntry (const void *aa, const void *bb)
{
	Entry *a = (Entry*) aa;
	Entry *b = (Entry*) bb;
	if (a->value < b->value)
		return -1;
	if (a->value == b->value && a->type == END)
		return -1;
	return 1;
}

int numCase;
int limits[10000][3];
int numPeople;


Entry eList[15000];
int numEntry;
int maxSatisfy;
	
int main()
{
	scanf("%d", &numCase);
	int i, j, k;
	for (i = 0; i < numCase; i++)
	{
		maxSatisfy = 0;
		scanf("%d", &numPeople);
		for (j = 0; j < numPeople; j++)
		{
			scanf("%d %d %d", &limits[j][0], &limits[j][1], &limits[j][2]);
		}
		for (j = 0; j <= 10000; j++)
		{
			int numSatisfy = 0;
			numEntry = 0;
			for (k = 0; k < numPeople; k++)
			{
				if (j >= limits[k][0] && j + limits[k][1] + limits[k][2] <= 10000)
				{
					eList[numEntry].value = limits[k][1];
					eList[numEntry].type = START;
					numEntry++;
					eList[numEntry].value = 10000 - j - limits[k][2] + 1;
					eList[numEntry].type = END;
					numEntry++;
				}
			}
			qsort(eList, numEntry, sizeof(Entry), compareEntry);
			for (k = 0; k < numEntry; k++)
			{
				if (eList[k].type == END)
					numSatisfy--;
				else
					numSatisfy++;
				if (numSatisfy > maxSatisfy)
					maxSatisfy = numSatisfy;
			}
		}
		printf("Case #%d: %d\n", i+1, maxSatisfy);
	}
	return 0;
}
