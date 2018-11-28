// GCJ_SavingTheUniverse.cpp
//

#include <string.h>

int g_MinimumVal;
int** g_MinimumNodeArr;

int QuickReject(char** a_SearchEngine, int a_S, char** a_Keyword, int a_Q)
{
	if (a_Q == 0)
		return 1;
	if (a_S == 0)
		return 1;
	for (int i = 0; i < a_S; i++)
	{
		int flag = false;
		for (int j = 0; j < a_Q; j++)
			if (strcmp(a_SearchEngine[i], a_Keyword[j]) == 0)
				flag = true;
		if (!flag)
			return 1;
	}
	return 0;
}

int DoFindMinimum(char** a_SearchEngine, int a_S, int a_CurrentSearchEngineIndex, char** a_Keyword, int a_Q, int a_CurrentKeywordIndex, int a_SwitchCount)
{
	if (a_CurrentKeywordIndex == a_Q)
		return 0;

	if (a_SwitchCount > g_MinimumVal)
		return 0;

	if (g_MinimumNodeArr[a_CurrentSearchEngineIndex][a_CurrentKeywordIndex] != -1)
		return g_MinimumNodeArr[a_CurrentSearchEngineIndex][a_CurrentKeywordIndex];

	while (a_CurrentKeywordIndex < a_Q && strcmp(a_SearchEngine[a_CurrentSearchEngineIndex], a_Keyword[a_CurrentKeywordIndex]) != 0)
		a_CurrentKeywordIndex++;

	int tNewMinimum = -1;
	if (a_CurrentKeywordIndex < a_Q)
	{
		for (int i = 0; i < a_S; i++)
			if (i != a_CurrentSearchEngineIndex)
			{
				g_MinimumNodeArr[i][a_CurrentKeywordIndex] = DoFindMinimum(a_SearchEngine, a_S, i, a_Keyword, a_Q, a_CurrentKeywordIndex, /*a_SwitchCount+1*/0);
				if (tNewMinimum == -1)
					tNewMinimum = g_MinimumNodeArr[i][a_CurrentKeywordIndex];
				else if (g_MinimumNodeArr[i][a_CurrentKeywordIndex] < tNewMinimum)
					tNewMinimum = g_MinimumNodeArr[i][a_CurrentKeywordIndex];
			}
		return tNewMinimum + 1;
	}
	else
	{
		if (a_SwitchCount < g_MinimumNodeArr[a_CurrentSearchEngineIndex][a_CurrentKeywordIndex])
			return a_SwitchCount;
		else
			return g_MinimumNodeArr[a_CurrentSearchEngineIndex][a_CurrentKeywordIndex];
	}

	return 0;
}

int FindMinimum(char** a_SearchEngine, int a_S, int a_CurrentSearchEngineIndex, char** a_Keyword, int a_Q, int a_CurrentKeywordIndex)
{
	g_MinimumNodeArr = new int*[a_S];
	for (int i = 0; i < a_S; i++)
		g_MinimumNodeArr[i] = new int[a_Q];

	for (int i = 0; i < a_S; i++)
		for (int j = 0; j < a_Q; j++)
			g_MinimumNodeArr[i][j] = -1;

	g_MinimumVal = a_Q;
	for (int i = 0; i < a_S; i++)
	{
		int tmp = DoFindMinimum(a_SearchEngine, a_S, i, a_Keyword, a_Q, a_CurrentKeywordIndex, 0);
		if (tmp < g_MinimumVal)
			g_MinimumVal = tmp;
	}

	for (int i = 0; i < a_S; i++)
		delete g_MinimumNodeArr[i];
	delete [] g_MinimumNodeArr;

	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	// Get N value
	int g_N;
	scanf("%d", &g_N);

	int resultArr[20];

	for (int c = 0; c < g_N; c++)
	{
		resultArr[c] = 0;

		// Get S value
		int g_S;
		scanf("%d", &g_S);

		char junk[10];
		gets(junk);

		// Construct Search Engine Array
		char** g_SearchEngine = new char*[g_S];
		for (int i = 0; i < g_S; i++)
			g_SearchEngine[i] = new char[120];
		// Get Search Engine Array
		for (int i = 0; i < g_S; i++)
			gets(g_SearchEngine[i]);

		// Get Q value
		int g_Q;
		scanf("%d", &g_Q);

		gets(junk);

		// Construct Keyword Array
		char** g_Keyword = new char*[g_Q];
		for (int i = 0; i < g_Q; i++)
			g_Keyword[i] = new char[120];
		// Get Keyword Array
		for (int i = 0; i < g_Q; i++)
			gets(g_Keyword[i]);



		if (!QuickReject(g_SearchEngine, g_S, g_Keyword, g_Q))
		{
			FindMinimum(g_SearchEngine, g_S, 0, g_Keyword, g_Q, 0);
			resultArr[c] = g_MinimumVal;
		}
		else
		{
			resultArr[c] = 0;
		}



		// Destroy Search Engine Array
		for (int i = 0; i < g_Q; i++)
			delete g_Keyword[i];
		delete [] g_Keyword;

		// Destroy Search Engine Array
		for (int i = 0; i < g_S; i++)
			delete g_SearchEngine[i];
		delete [] g_SearchEngine;
	}

	// Print out the result
	for (int c = 0; c < g_N; c++)
		printf("Case #%d: %d\r\n", c+1, resultArr[c]);

	return 0;
}

