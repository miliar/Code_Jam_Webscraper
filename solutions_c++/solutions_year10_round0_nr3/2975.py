#include <iostream>
#include <vector>
using namespace std;

int main()
{
	unsigned int numCases;

	cin >> numCases;

	for(unsigned int i=0;i<numCases;i++)
	{
		vector<unsigned int> gsize;
		unsigned int limitPerTrip;
		unsigned int numTrips;
		unsigned int numGroups;
		cin >> numTrips;
		cin >> limitPerTrip;
		cin >> numGroups;
		for(unsigned int j=0;j<numGroups;j++)
		{
			unsigned int g;
			cin >> g;
			gsize.push_back(g);
		}

		// precompute what happens if a particular group comes first
		vector<unsigned int> groupsToSkip;
		vector<unsigned int> batchIncome;
		for(unsigned int gi=0;gi<numGroups;gi++)
		{
			unsigned int income=0;
			unsigned int currentGroupIndex = gi;
			unsigned int startGroupIndex = currentGroupIndex;
			unsigned int currentBatchSize = 0;
			unsigned int numSkipped = 0;
			do
			{
				if((currentBatchSize+gsize[currentGroupIndex])<=limitPerTrip)
				{
					income += gsize[currentGroupIndex];
					currentBatchSize += gsize[currentGroupIndex];
					currentGroupIndex = (currentGroupIndex+1)%numGroups;
					numSkipped++;
				}
				else
					break;
			} while(currentGroupIndex!=startGroupIndex);
			batchIncome.push_back(income);
			groupsToSkip.push_back(numSkipped);
		}
		
		unsigned int income = 0;
		unsigned int currentGroupIndex = 0;
		for(unsigned int tripIndex = 0;tripIndex <numTrips;tripIndex++)
		{
			income +=batchIncome[currentGroupIndex];
			currentGroupIndex = (currentGroupIndex+groupsToSkip[currentGroupIndex])%numGroups;
		}
		cout << "Case #"<<i+1<<": "<<income<<endl;
	}
	return 0;
}
