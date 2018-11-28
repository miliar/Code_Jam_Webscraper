#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <set>

#define MAX_BUFFER_LENGTH 256

typedef std::vector<char*> STRPARAMS;

void ClearStr(char* str)
{
	while (*str != '\r' && *str != '\n' && *str != '\0')
		str++;
	*str = '\0';
}

void Search(STRPARAMS& vecEngines, int curEngine, STRPARAMS& vecQueries, int curQuery, int nSwitches, int& nMinSwitches)
{
	while (!strstr(vecQueries[curQuery], vecEngines[curEngine]))
	{
		// Can proceed to the next query
		curQuery++;
		if (curQuery >= vecQueries.size())
		{
			if (nMinSwitches < 0 || nSwitches < nMinSwitches)
				nMinSwitches = nSwitches;
			return;
		}
	}

	nSwitches++;
	if (nMinSwitches >= 0 && nSwitches >= nMinSwitches)
		return;

	std::set<int> eng;
	for (int nEngine = 0; nEngine < vecEngines.size(); nEngine++)
	{
		if (nEngine != curEngine)
			eng.insert(nEngine);
	}

	for (int i = curQuery; i < vecQueries.size(); i++)
	{
		for (int nEngine = 0; nEngine < vecEngines.size(); nEngine++)
		{
			if (!strstr(vecQueries[i], vecEngines[nEngine]))
				continue;

			std::set<int>::iterator itr = eng.find(nEngine);
			if (itr != eng.end())
			{
				if (eng.size() > 1)
					eng.erase(itr);
				break;
			}
		}
		if (eng.size() == 1)
			break;
	}

	std::set<int>::iterator itr = eng.begin();
	int nEngine = *itr;
	Search(vecEngines, nEngine, vecQueries, curQuery, nSwitches, nMinSwitches);
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 0;

	FILE* hFile = fopen(argv[1], "r");
	if (!hFile)
		return 0;

	char buf[MAX_BUFFER_LENGTH];

	// Get number of cases
	if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
		return 0;
	int nCount = atoi(buf);

	int numCase = 1;
	while (numCase <= nCount)
	{
		// Get number of search engines
		if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
			return 0;

		int nEngines = atoi(buf);

		// Load search engines
		STRPARAMS vecEngines;

		for (int i = 0; i < nEngines; i++)
		{
			if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
				return 0;
			ClearStr(buf);
			int len = strlen(buf) + 1;
			char* ps = new char[len];
			if (!ps)
				return 0;
			strcpy(ps, buf);
			vecEngines.push_back(ps);
		}

		// Get number of queries
		if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
			return 0;

		int nQueries = atoi(buf);

		// Load queries
		STRPARAMS vecQueries;

		for (int i = 0; i < nQueries; i++)
		{
			if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
				return 0;
			ClearStr(buf);
			int len = strlen(buf) + 1;
			char* ps = new char[len];
			if (!ps)
				return 0;
			strcpy(ps, buf);
			vecQueries.push_back(ps);
		}

		int nMinSwitches = -1;

		if (nQueries <= 0 || nEngines <= 0)
			nMinSwitches = 0;
		else
		{
			for (int nEngine = 0; nEngine < vecEngines.size(); nEngine++)
				Search(vecEngines, nEngine, vecQueries, 0, 0, nMinSwitches);
		}

		printf("Case #%d: %d\n", numCase, nMinSwitches);

		for (STRPARAMS::iterator itr = vecEngines.begin(); itr != vecEngines.end(); itr++)
			delete *itr;
		vecEngines.clear();
		for (STRPARAMS::iterator itr = vecQueries.begin(); itr != vecQueries.end(); itr++)
			delete *itr;
		vecQueries.clear();

		numCase++;
	}
	return 0;
}
