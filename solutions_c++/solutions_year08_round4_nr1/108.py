#include <stdlib.h>
#include <stdio.h>

int gateVal[15000];
int gateType[15000];
int canChange[15000];
int numToChange[15000];

const int ANDGATE = 1;
const int ORGATE = 0;

int doOp(int gate, int a, int b)
{
	if (gate == ANDGATE)
	{
		if (a == 1 && b == 1) return 1;
		return 0;
	}
	else
	{
		if (a == 1 || b == 1) return 1;
		return 0;
	}
}

int opp(int a)
{
	if (a == 0) return 1;
	return 0;
}

const int MAXCHANGE = 100000;

int update(int j, int change1, int change2, int newType)
{
	int toChange1 = numToChange[2*j];
	int toChange2 = numToChange[2*j+1];
	int curType = gateType[j];
	if (change1 == 1 && toChange1 == MAXCHANGE) return MAXCHANGE;
	if (change2 == 1 && toChange2 == MAXCHANGE) return MAXCHANGE;
	int curVal = gateVal[j];
	int left = gateVal[2*j];
	if (change1 == 1) left = opp(left);
	int right = gateVal[2*j+1];
	if (change2 == 1) right = opp(right);
	if (doOp(newType, left, right) != curVal)
	{
		int used = 0;
		if (curType != newType) used = 1;
		if (change1 == 1) used += toChange1;
		if (change2 == 1) used += toChange2;
		return used;
	}
	return MAXCHANGE;
}

int min(int a, int b)
{
	if (a < b) return a;
	return b;
}


int main()
{
	int numCase;
	scanf("%d", &numCase);
	int i, j, k, M, v;
	for (i = 0; i < numCase; i++)
	{
		printf("Case #%d: ", i+1);

		scanf("%d %d", &M, &v);
		for (j = 1; j <= (M-1)/2; j++)
			scanf("%d %d", &gateType[j], &canChange[j]);
		for (j = (M+1)/2; j <= M; j++)
			scanf("%d", &gateVal[j]);
		for (j = (M-1)/2; j > 0; j--)
		{
			gateVal[j] = doOp(gateType[j], gateVal[2*j], gateVal[2*j+1]);
		}

		if (gateVal[1] == v)
		{
			printf("0\n");
			continue;
		}

		for (j = (M+1)/2; j <= M; j++)
			numToChange[j] = MAXCHANGE;

		for (j = (M-1)/2; j > 0; j--)
		{
			numToChange[j] = MAXCHANGE;
			for (int change1 = 0; change1 < 2; change1++)
				for (int change2 = 0; change2 < 2; change2++)
				{
					if (canChange[j])
						for (int newType = 0; newType < 2; newType++)
							numToChange[j] = min(numToChange[j], update(j, change1, change2, newType));
					else
						numToChange[j] = min(numToChange[j], update(j, change1, change2, gateType[j]));
				}
		}
		if (numToChange[1] == MAXCHANGE)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", numToChange[1]);
		}
	}
	return 0;
}
