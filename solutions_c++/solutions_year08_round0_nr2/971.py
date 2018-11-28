#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
using namespace std;
struct train
{
	int startHour, startMin;
	int endHour, endMin;
	bool operator < (const train& rhs)const
	{
		if(startHour != rhs.startHour)
			return startHour < rhs.startHour;
		if(startMin != rhs.startMin)
			return startMin < rhs.startMin;
		if(endHour != rhs.endHour)
			return endHour < rhs.endHour;
		return endMin < rhs.endMin;
	}
};

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int o = 0; o  < numTests; o++)
	{
		printf("Case #%d: ", o + 1);
		int t, na, nb;
		cin >> t >> na >> nb;
		vector<train> aTrains;
		vector<train> bTrains;
		for(int i = 0; i < na; i++)
		{
			train temp;
			scanf("%d:%d", &temp.startHour, &temp.startMin);
			scanf("%d:%d", &temp.endHour, &temp.endMin);
			temp.endMin += t;
			temp.endHour += temp.endMin / 60;
			temp.endMin %= 60;
			aTrains.push_back(temp);
		}

		for(int i = 0; i < nb; i++)
		{
			train temp;
			scanf("%d:%d", &temp.startHour, &temp.startMin);
			scanf("%d:%d", &temp.endHour, &temp.endMin);
			temp.endMin += t;
			temp.endHour += temp.endMin / 60;
			temp.endMin %= 60;
			bTrains.push_back(temp);
		}

		train large;
		large.startHour = large.endHour = large.startMin = large.endMin = 1000;
		aTrains.push_back(large);
		bTrains.push_back(large);

		sort(aTrains.begin(), aTrains.end());
		sort(bTrains.begin(), bTrains.end());

		priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > availableA, availableB;
		//priority_queue<pair<int, int> >::iterator itr;
		pair<int, int> tempP;
		int aIdx = 0, bIdx = 0;
		int numA = 0, numB = 0;
		for(int i = 0; i < na + nb; i++)
		{
			if(aTrains[aIdx] < bTrains[bIdx])
			{
				if(!availableA.empty() && availableA.top() <= make_pair(aTrains[aIdx].startHour, aTrains[aIdx].startMin))
				{
					availableA.pop();
					availableB.push(make_pair(aTrains[aIdx].endHour, aTrains[aIdx].endMin));
				}
				else
				{
					availableB.push(make_pair(aTrains[aIdx].endHour, aTrains[aIdx].endMin));
					numA++;
				}
				aIdx++;
			}
			else
			{
				if(!availableB.empty() && availableB.top() <= make_pair(bTrains[bIdx].startHour, bTrains[bIdx].startMin))
				{
					availableB.pop();
					availableA.push(make_pair(bTrains[bIdx].endHour, bTrains[bIdx].endMin));
				}
				else
				{
					availableA.push(make_pair(bTrains[bIdx].endHour, bTrains[bIdx].endMin));
					numB++;
				}
				bIdx++;
			}
		}
		cout << numA << " " << numB << endl;
	}
	return 0;
}