#include <iostream>
#include <xutility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

void SolveTest();

void main()
{
	cout.precision(10);

	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		SolveTest();
		cout << endl;
	}
}

bool sortBySecond(pair<double, int> i, pair<double, int> j) { return i.second < j.second; }

void SolveTest()
{
	int X, S, R, t, N;
	cin >> X >> S >> R >> t >> N;
	double runningTimeLeft = t;

	vector<pair<double, int>> distSpeeds;
	int curLoc = 0;

	for(int i = 0; i < N; ++i)
	{
		int start, end, speed;
		cin >> start >> end >> speed;

		if(curLoc < start)
		{
			//not yet at walkway
			distSpeeds.push_back(pair<int, int>(start - curLoc, S));
			curLoc = start;
		}

		distSpeeds.push_back(pair<int, int>(end - start, S + speed));
		curLoc = end;
	}

	//Get to end if any remaining
	if(curLoc < X)
	{
		distSpeeds.push_back(pair<int, int>(X - curLoc, S));
		curLoc = X;
	}

	//Now convert slowest parts to running, after sorting
	sort(distSpeeds.begin(), distSpeeds.end(), sortBySecond);

	vector<pair<double, int> >::iterator iter = distSpeeds.begin();
	while(runningTimeLeft > 0)
	{
		if(iter == distSpeeds.end())
			break; //All segments run

		double& distance = iter->first;
		int& speed = iter->second;

		//Caclulate time to run this segment
		double timeToRunSegment = distance / (speed - S + R);

		//Convert this to running
		if(timeToRunSegment <= runningTimeLeft)
		{
			//Convert entire section
			speed = speed - S + R;
			runningTimeLeft -= timeToRunSegment;
			++iter;
		}
		else
		{
			//Convert part of this section, and stop
			double distanceRan = runningTimeLeft / timeToRunSegment * distance;
			double distanceWalked = distance - distanceRan;

			distance = distanceWalked;
			distSpeeds.push_back(pair<double, int>(distanceRan, speed - S + R));
			runningTimeLeft = 0;
		}
	}
	

	//Combine all bits together to get time
	double result = 0;
	for(std::vector<pair<double, int>>::iterator iter = distSpeeds.begin(); iter != distSpeeds.end(); ++iter)
	{
		result += double(iter->first) / double(iter->second);
	}
	
	cout << result;
}

