// GCJ_Train.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>

struct TTimeTraval
{
	int iDeparture;
	int iArrival;
	int iUsed;
};

int StrTimeToInt(char* aTime)
{
	int result = ((aTime[0]-'0')*10 + (aTime[1]-'0')) * 60;
	result += (aTime[3]-'0')*10 + (aTime[4]-'0');
	return result;
}

void SortByDepartureTime(TTimeTraval* a_Arr, int aArrCount)
{
	for (int i = 0; i < aArrCount-1; i++)
	{
		int tMin = i;
		for (int j = i+1; j < aArrCount; j++)
			if (a_Arr[j].iDeparture < a_Arr[tMin].iDeparture)
				tMin = j;
		TTimeTraval tmp = a_Arr[tMin];
		a_Arr[tMin] = a_Arr[i];
		a_Arr[i] = tmp;
	}
}

void RemoveUsedEntries(TTimeTraval* a_Arr, int& aArrCount)
{
	for (int i = 0; i < aArrCount-1; i++)
	{
		if (!a_Arr[i].iUsed)
			continue;
		int tUnusedIndex = -1;
		for (int j = i+1; j < aArrCount && tUnusedIndex == -1; j++)
			if (!a_Arr[j].iUsed)
				tUnusedIndex = j;
		if (tUnusedIndex != -1)
		{
			TTimeTraval tmp = a_Arr[tUnusedIndex];
			a_Arr[tUnusedIndex] = a_Arr[i];
			a_Arr[i] = tmp;
		}
	}
	int tNewArrCount = 0;
	for (int i = 0; i < aArrCount; i++)
		if (!a_Arr[i].iUsed)
			tNewArrCount++;
	aArrCount = tNewArrCount;
}

int _tmain(int argc, _TCHAR* argv[])
{
	// Get N value
	int g_N;
	scanf("%d", &g_N);

	int resultArrA[100];
	int resultArrB[100];

	for (int c = 0; c < g_N; c++)
	{
		resultArrA[c] = 0;
		resultArrB[c] = 0;

		// Get Tunraround Time value
		int g_T;
		scanf("%d", &g_T);

		int g_NA;
		int g_NB;
		scanf("%d", &g_NA);
		scanf("%d", &g_NB);

		char str[100];

		// Construct A to B Array
		TTimeTraval* g_AtoB = new TTimeTraval[g_NA];
		// Get A to B Array
		for (int i = 0; i < g_NA; i++)
		{
			scanf("%s", str);
			g_AtoB[i].iDeparture = StrTimeToInt(str);
			scanf("%s", str);
			g_AtoB[i].iArrival = StrTimeToInt(str) + g_T;
			g_AtoB[i].iUsed = false;
		}

		SortByDepartureTime(g_AtoB, g_NA);

		// Construct B to A Array
		TTimeTraval* g_BtoA = new TTimeTraval[g_NB];
		// Get B to A Array
		for (int i = 0; i < g_NB; i++)
		{
			scanf("%s", str);
			g_BtoA[i].iDeparture = StrTimeToInt(str);
			scanf("%s", str);
			g_BtoA[i].iArrival = StrTimeToInt(str) + g_T;
			g_BtoA[i].iUsed = false;
		}

		SortByDepartureTime(g_BtoA, g_NB);

		// Quick Answer
		if (g_NA == 0 || g_NB == 0)
		{
			resultArrA[c] = g_NA;
			resultArrB[c] = g_NB;
		}
		else
		{
			while (g_NA > 0 || g_NB > 0)
			{
				if (g_NA == 0 || g_NB == 0)
				{
					resultArrA[c] += g_NA;
					resultArrB[c] += g_NB;
					g_NA = 0;
					g_NB = 0;
					break;
				}
				int tNowAtoB = false;
				if (g_AtoB[0].iDeparture < g_BtoA[0].iDeparture)
					tNowAtoB = true;
				int tStartFromA = tNowAtoB;
				// Greedy Algorithm
				int tLastArrival;
				if (tNowAtoB)
				{
					g_AtoB[0].iUsed = true;
					tLastArrival = g_AtoB[0].iArrival;
				}
				else
				{
					g_BtoA[0].iUsed = true;
					tLastArrival = g_BtoA[0].iArrival;
				}
				// Find Next Nearest Timeline in oppisite way
				int HasNext = true;
				while (HasNext)
				{
					if (tNowAtoB)
					{
						// Find in B way
						HasNext = false;
						for (int i = 0; i < g_NB; i++)
							if (g_BtoA[i].iDeparture >= tLastArrival && !g_BtoA[i].iUsed)
							{
								g_BtoA[i].iUsed = true;
								tLastArrival = g_BtoA[i].iArrival;
								tNowAtoB = !tNowAtoB;
								HasNext = true;
								i = g_NB;
							}
					}
					else
					{
						// Find in A way
						HasNext = false;
						for (int i = 0; i < g_NA; i++)
							if (g_AtoB[i].iDeparture >= tLastArrival && !g_AtoB[i].iUsed)
							{
								g_AtoB[i].iUsed = true;
								tLastArrival = g_AtoB[i].iArrival;
								tNowAtoB = !tNowAtoB;
								HasNext = true;
								i = g_NA;
							}
					}
				}
				if (tStartFromA)
					resultArrA[c]++;
				else
					resultArrB[c]++;
				RemoveUsedEntries(g_AtoB, g_NA);
				RemoveUsedEntries(g_BtoA, g_NB);
			}
		}

		delete [] g_AtoB;
		delete [] g_BtoA;
	}

	// Print out the result
	for (int c = 0; c < g_N; c++)
		printf("Case #%d: %d %d\r\n", c+1, resultArrA[c], resultArrB[c]);

	return 0;
}

