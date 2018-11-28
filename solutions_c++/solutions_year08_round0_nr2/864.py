#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int rotateTime, aLineCount, bLineCount;
vector<int> aDeparture, aArrival, bDeparture, bArrival;
vector<pair<int, int> > aLines, bLines;

int transfomTime(string s)
{
	return atoi(s.substr(0,2).c_str())*60 + atoi(s.substr(3,2).c_str());
}

int solve(vector<int> &arrived, vector<int> &departure)
{
	int departuredTrains = 0;
	
	for(int i = 0; i < departure.size(); i++)
	{
		if((upper_bound(arrived.begin(), arrived.end(), departure[i]) - arrived.begin()) + departuredTrains <= i)
		{
			departuredTrains++;
		}
	}

	return departuredTrains;
}
int main()
{
	int tests;
	char tmp[50];
	freopen("input.in","r", stdin);
	freopen("output.out","w", stdout);
	scanf("%d", &tests);
	for(int test = 0; test < tests; test++)
	{
		scanf("%d\n", &rotateTime);
		scanf("%d %d\n", &aLineCount, &bLineCount);
		aLines.clear();
		bLines.clear();
		aArrival.clear();
		bArrival.clear();
		aDeparture.clear();
		bDeparture.clear();

		for(int i = 0; i < aLineCount; i++)
		{
			gets(tmp);
			aLines.push_back(make_pair(transfomTime(tmp), transfomTime(&(tmp[6]))+rotateTime));
		}
		
		for(int i = 0; i < bLineCount; i++)
		{
			gets(tmp);
			bLines.push_back(make_pair(transfomTime(tmp), transfomTime(&(tmp[6]))+rotateTime));
		}

		for(int i = 0; i < aLines.size(); i++)
		{
			aDeparture.push_back(aLines[i].first);
			bArrival.push_back(aLines[i].second);
		}
		
		for(int i = 0; i < bLines.size(); i++)
		{
			bDeparture.push_back(bLines[i].first);
			aArrival.push_back(bLines[i].second);
		}

		sort(aDeparture.begin(), aDeparture.end());
		sort(aArrival.begin(), aArrival.end());
		sort(bDeparture.begin(), bDeparture.end());
		sort(bArrival.begin(), bArrival.end());
		printf("Case #%d: %d %d\n", test + 1, solve(aArrival, aDeparture), solve(bArrival, bDeparture));
	}
	return 0;
}