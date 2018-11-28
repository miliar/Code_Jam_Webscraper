#include <iostream>
#include <set>

using namespace std;

struct TrainInfo
{
	int departureHour, departureMinute;
	int arriveHour, arriveMinute;

	int DepartureTime2Int()const
	{
		return departureHour*60 + departureMinute;
	}

	int ArriveTime2Int()const
	{
		return arriveHour*60 + arriveMinute;
	}

	int index;
};

int cmpTrainInfo(const TrainInfo &lhs, const TrainInfo &rhs)
{
	if(lhs.departureHour != rhs.departureHour)
	{
		return lhs.departureHour < rhs.departureHour;
	}

	return lhs.departureMinute < rhs.departureMinute;
}

int main()
{
	int testCaseCount;
	int turnaroundTime;
	int a2bCount, b2aCount;
	TrainInfo trainInfo[101];

	enum
	{
		A2B_index, B2A_index
	};

	cin >> testCaseCount;
	//cout << testCaseCount << endl;
	for(int i = 0; i < testCaseCount; i++)
	{
		cin >> turnaroundTime;
		//cout << turnaroundTime << endl;

		//searchEngineNames.clear();
		//cin.ignore();
		cin >> a2bCount >> b2aCount;

		//cout << a2bCount << " " << b2aCount << endl;

		for(int j = 0; j < a2bCount+b2aCount; j++)
		{
			char colon;
			cin >> trainInfo[j].departureHour >> colon
				>> trainInfo[j].departureMinute
				>> trainInfo[j].arriveHour >> colon
				>> trainInfo[j].arriveMinute;

			trainInfo[j].index = j < a2bCount ? A2B_index : B2A_index;

/*
			cout << trainInfo[j].departureHour << ":"
				 << trainInfo[j].departureMinute << " "
				 << trainInfo[j].arriveHour << ":"
				 << trainInfo[j].arriveMinute << endl;
*/
		}

		sort(trainInfo, &trainInfo[a2bCount+b2aCount], cmpTrainInfo);

		int count[2] = {0};
		multiset <int> waitTrain[2];

		for(int j = 0; j < a2bCount+b2aCount; j++)
		{
/*
			cout << trainInfo[j].departureHour << ":"
				 << trainInfo[j].departureMinute << " "
				 << trainInfo[j].arriveHour << ":"
				 << trainInfo[j].arriveMinute << endl;
*/
			const int idx = trainInfo[j].index;

			waitTrain[1-idx].insert(trainInfo[j].ArriveTime2Int());
			if(waitTrain[idx].empty())
			{
				count[idx]++;
				continue;
			}

			set <int>::const_iterator iter = waitTrain[idx].begin();
			//cout << "iter:" << (*iter) << endl;

			if(*iter+turnaroundTime <= trainInfo[j].DepartureTime2Int())
			{
				waitTrain[idx].erase(iter);
			}
			else
			{
				count[idx]++;
			}
		}

		cout << "Case #" << (i+1) << ": " << count[A2B_index] << " " << count[B2A_index] << endl;
	}

	return 0;
}
