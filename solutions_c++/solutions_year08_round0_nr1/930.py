#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	cin >> testNum;

	char szBuffer[128];

	for (int testId = 0; testId < testNum; testId++)
	{
		int searchEnginesNum;
		set<string> searchEngines;

		scanf("%d\n", &searchEnginesNum);
		
		for (int i = 0; i < searchEnginesNum; i++)
		{
			cin.getline(szBuffer, sizeof(szBuffer));
			searchEngines.insert(szBuffer);
		}

		int queryNum, switchNum = 0;
		set<string> availableEngines(searchEngines);

		scanf("%d\n", &queryNum);

		for (int i = 0; i < queryNum; i++)
		{
			cin.getline(szBuffer, sizeof(szBuffer));

			while (availableEngines.erase(szBuffer) > 0 && availableEngines.size() < 1)
			{
				switchNum++;
				availableEngines = searchEngines;
			}
		}

		cout << "Case #" << testId + 1 << ": " << switchNum << endl;
	}

	return 0;
}