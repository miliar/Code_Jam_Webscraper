#include <cstdio>
#include <iostream>

#include <vector>
#include <string>

using namespace std;

int Name2Index(const vector <string> &searchEngineNames, const string &query, const int max_idx)
{
	for(int i = 0; i < max_idx; i++)
	{
		if(searchEngineNames[i] == query)
		{
			return i;
		}
	}
	return -1;
}

int main()
{
	int testCaseCount;
	int searchEngineCount;
	int queryCount;
	vector <string> searchEngineNames(101);
	string query;
	int searchEngineUsedCount;
	bool flag[101];
	int changeCount;

	cin >> testCaseCount;
	//cout << testCaseCount << endl;
	for(int i = 0; i < testCaseCount; i++)
	{
		cin >> searchEngineCount;
		//cout << searchEngineCount << endl;

		//searchEngineNames.clear();
		cin.ignore();
		for(int j = 0; j < searchEngineCount; j++)
		{
			getline(cin, searchEngineNames[j]);
//			cin >> ;
			//cout << searchEngineNames[j] << endl;
			flag[j] = false;
		}

		cin >> queryCount;
		//cout << queryCount << endl;
		cin.ignore();

		changeCount = 0;
		searchEngineUsedCount = 0;
		for(int j = 0; j < queryCount; j++)
		{
			getline(cin, query);
			//cout << query << endl;

			const int index = Name2Index(searchEngineNames, query, searchEngineCount);

			if(!flag[index])
			{
				searchEngineUsedCount++;

				if(searchEngineUsedCount >= searchEngineCount)
				{
					searchEngineUsedCount = 1;
					for(int k = 0; k < searchEngineCount; k++)
					{
						flag[k] = false;
					}

					changeCount++;
				}

				flag[index] = true;
			}
		}

		cout << "Case #" << (i+1) << ": " << changeCount << endl;
	}

	return 0;
}
