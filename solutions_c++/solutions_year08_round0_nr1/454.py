#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	string line;
	map<string, bool> searchEngines;
	int a, numCases, numSearchEngines, queries, switches, count;
	
	cin >> numCases;
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		cin >> numSearchEngines;
		getline(cin, line);
		for (a = 0; a < numSearchEngines; a++)
		{
			getline(cin, line);
			searchEngines[line] = true;
		}
		count = 0;
		switches = 0;
		cin >> queries;
		getline(cin, line);
		for (a = 0; a < queries; a++)
		{
			getline(cin, line);
			if (searchEngines[line])
			{
				// Mark search engine
				count++;
				if (count == numSearchEngines)
				{
					switches++;
					// Reset map
					map<string, bool>::iterator p;
					for (p = searchEngines.begin(); p != searchEngines.end(); ++p)
					{
						(*p).second = true;
					}
					count = 1;
				}
				searchEngines[line] = false;
			}
		}
		cout << "Case #" << curCase << ": " << switches << endl;
		searchEngines.clear();
	}
	return 0;
}
