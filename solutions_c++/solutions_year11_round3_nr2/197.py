#include <iostream>
#include <xutility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

#define EPSILON 0.01;

long long SolveTest();

void main()
{
	long long numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		long long result = SolveTest();
		cout << result << endl;
	}
}

long long SolveTest()
{
	long long numBoosters, boosterTime, N, C;
	vector<long long> cArray;

	cin >> numBoosters;
	cin >> boosterTime;
	cin >> N;
	cin >> C;
	for(int i = 0; i < C; ++i)
	{
		long long next;
		cin >> next;
		cArray.push_back(next);
	}

	vector<long long> times; ///Time to travel between each star - without booster
	for(int i = 0; i < N; ++i)
	{
		times.push_back(cArray[i%C] * 2);
	}

	long long curTime = 0;
	int curStar = 0;

	//Find out how long to travel without any boosters
	long long timeWithoutBoosters = 0;
	for(std::vector<long long>::iterator iter = times.begin(); iter != times.end(); ++iter)
		timeWithoutBoosters += *iter;

	//If we can never build it before we arrive.. then this is the answer
	if(timeWithoutBoosters <= boosterTime)
		return timeWithoutBoosters;

	//Travel up until the point where boosters can be completed
	long long timeLeft = boosterTime;
	while(timeLeft > 0)
	{
		if(times[curStar] <= timeLeft) //Can reach next star
		{
			timeLeft -= times[curStar];
			times[curStar] = 0;
			++curStar;
		}
		else
		{
			//Can't reach next star. Update distance remaining in vector
			times[curStar] = times[curStar] - timeLeft;
			timeLeft = 0;
		}
	}

	curTime = boosterTime;

	//Vector now has all remaining times yet to travel. APply boosters on longest time by first sorting vector
	sort(times.begin(), times.end(), std::greater<long long>());
	for(int i = 0; i < numBoosters; ++i)
	{
		times[i] = times[i] / 2;
	}

	//Now add all remaining times to curTime to get answer
	for(std::vector<long long>::iterator iter = times.begin(); iter != times.end(); ++iter)
	{
		curTime += *iter;
	}

	return curTime;
}
