// Saving the Universe.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void)
{
	char              query[150]        = {0};
	char              searchEngine[150] = {0};
	int               caseCount         = 0;
	int               i                 = 0;
	int               j                 = 0;
	int               k                 = 0;
	int               newJ              = 0;
	int               queryCount        = 0;
	int               searchEngineCount = 0;
	int               switches          = 0;
	int               table[101][1001]  = {0};
	ifstream          input;
	ofstream          output;
	vector < string > queries;
	vector < string > searchEngines;

	input.open("SavingTheUniverse.in", ios_base::in);
	output.open("SavingTheUniverse.out", ios_base::out);

	input >> caseCount;

	for (i = 0; i < caseCount; i++)
	{
		//
		//  Initialize
		//
		memset(table, 0, sizeof (table));
		queries.erase(queries.begin(), queries.end());
		searchEngines.erase(searchEngines.begin(), searchEngines.end());

		input >> searchEngineCount;
		while (searchEngineCount > 0)
		{
			memset(searchEngine, 0, sizeof (searchEngine));
			input.getline(searchEngine, sizeof (searchEngine));
			if (0 == searchEngine[0])
				continue;
			searchEngines.push_back(searchEngine);
			searchEngineCount--;
		}

		input >> queryCount;
		while (queryCount > 0)
		{
			memset(query, 0, sizeof (query));
			input.getline(query, sizeof (query));
			if (0 == query[0])
				continue;
			queries.push_back(query);
			queryCount--;
		}

		for (j = queries.size() - 1; j >= 0; j--)
		{
			for (k = 0; k < searchEngines.size(); k++)
			{
				if (0 == strcmp(searchEngines[k].c_str(), queries[j].c_str()))
				{
					table[k][j] = 0;
					continue;
				}

				if (queries.size() - 1 == j)
				{
					table[k][j] = 1;
					continue;
				}

				table[k][j] = table[k][j + 1] + 1;
			}
		}

		//
		//  Calculate the minimum switches required.
		//
		switches = -1;
		for (j = 0; j < queries.size(); j += newJ)
		{
			newJ = 0;
			for (k = 0; k < searchEngines.size(); k++)
			{
				if (table[k][j] > newJ)
					newJ = table[k][j];
			}
			if (0 == newJ)
				break;
			switches++;
		}
		if (-1 == switches)
			switches = 0;

		output << "Case #" << i + 1 << ": " << switches << endl;
	}

	input.close();
	output.close();

	return 0;
}

