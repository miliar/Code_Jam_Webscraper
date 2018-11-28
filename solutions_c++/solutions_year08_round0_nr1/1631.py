
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAX_ENGINES = 128;
const int MAX_QUERIES = 1024;
const int MAX_LEN = 1024;

int enginesCount, queriesCount;
char engineName[MAX_ENGINES][MAX_LEN];
char queryName[MAX_QUERIES][MAX_LEN];

int GetEngineNum(int q)
{
	if (q >= queriesCount)
		return -1;

	for (int e=0; e<enginesCount; e++)
	{
		if (strcmp(engineName[e], queryName[q]) == 0)
			return e;
	}

	return -1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int caseCount;
	cin >> caseCount;

	for (int caseNum = 1; caseNum <= caseCount; caseNum++)
	{
		cin >> enginesCount;
		cin.getline(engineName[0], MAX_LEN);
		for (int i=0; i < enginesCount; i++)
			cin.getline(engineName[i], MAX_LEN);

		cin >> queriesCount;
		cin.getline(queryName[0], MAX_LEN);
		for (int i=0; i < queriesCount; i++)
			cin.getline(queryName[i], MAX_LEN);

		int res = 0;
		int engineUsed[MAX_ENGINES];
		for (int i=0; i < queriesCount; )
		{
			int usedCount = 0;
			memset(engineUsed, 0, sizeof engineUsed);
			i--;

			while (i < queriesCount && usedCount < enginesCount)
			{
				i++;
				const int engineNum = GetEngineNum(i);
				if (engineNum >= 0 && !engineUsed[engineNum])
				{
					engineUsed[engineNum] = 1;
					usedCount++;
				}
			}

			if (usedCount >= enginesCount)
				res++;		
		}

		cout << "Case #" << caseNum << ": " << res << endl;
	}

	return 0;
}

