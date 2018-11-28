#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int NumberOfTests;
	cin >> NumberOfTests;
	for (int Test = 0; Test < NumberOfTests; ++Test)
	{
		int Times, Size, NumberOfGroups;
		cin >> Times >> Size >> NumberOfGroups;
		vector <int> Groups(NumberOfGroups);
		for (int i = 0; i < NumberOfGroups; ++i)
		{
			cin >> Groups[i];
		}
		long long int profit = 0;
		if (Times < 1001)
		{
			int current = 0;
			for (int i = 0; i < Times; ++i)
			{
				int localprofit = 0;
				for (int j = 0; ((j < NumberOfGroups) && (localprofit + Groups[current] <= Size)); ++j)
				{
					localprofit += Groups[current];
					current = (current + 1) % NumberOfGroups;
				}
				profit += localprofit;
			}
		}
		else
		{
			vector <bool> was(NumberOfGroups, false);
			int CircleBegin = 0;
			while (!was[CircleBegin])
			{
				was[CircleBegin] = true;
				long long int localprofit = 0;
				for (int j = 0; ((j < NumberOfGroups) && (localprofit + Groups[CircleBegin] <= Size)); ++j)
				{
					localprofit += Groups[CircleBegin];
					CircleBegin = (CircleBegin + 1) % NumberOfGroups;
				}
			}
			long long int TimesForCircle = 0;
			long long int ProfitForCircle = 0;
			int current = NumberOfGroups;
			while (current != CircleBegin)
			{
				if (current == NumberOfGroups)
				{
					current = CircleBegin;
				}
				long long int localprofit = 0;
				for (int j = 0; ((j < NumberOfGroups) && (localprofit + Groups[current] <= Size)); ++j)
				{
					localprofit += Groups[current];
					current = (current + 1) % NumberOfGroups;
				}
				ProfitForCircle += localprofit;
				++TimesForCircle;
			}
			current = 0;
			while (current != CircleBegin)
			{
				long long int localprofit = 0;
				for (int j = 0; ((j < NumberOfGroups) && (localprofit + Groups[current] <= Size)); ++j)
				{
					localprofit += Groups[current];
					current = (current + 1) % NumberOfGroups;
				}
				profit += localprofit;
				--Times;
			}
			int NumberOfCircles = Times / TimesForCircle;
			profit += NumberOfCircles * ProfitForCircle;
			Times = Times % TimesForCircle;
			current = CircleBegin;
			for (int i = 0; i < Times; ++i)
			{
				long long int localprofit = 0;
				for (int j = 0; ((j < NumberOfGroups) && (localprofit + Groups[current] <= Size)); ++j)
				{
					localprofit += Groups[current];
					current = (current + 1) % NumberOfGroups;
				}
				profit += localprofit;
			}
		}
		cout << "Case #" << Test + 1 << ": " << profit << endl;	
	}
	return 0;
}
