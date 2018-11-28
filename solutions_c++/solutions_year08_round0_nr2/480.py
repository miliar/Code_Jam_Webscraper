#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 1024

using namespace std;
FILE *in; FILE *out;

struct TrainTime
{
	int depart, arrive;
	
	bool operator < (TrainTime const& right) const
	{
		if (depart != right.depart) return depart > right.depart;
		else return arrive > right.arrive;
	}

	bool operator <= (TrainTime const& right) const
	{
		if (depart != right.depart) return depart < right.depart;
		return arrive <= right.arrive;
	}
};

int n1, n2;
priority_queue < TrainTime > d1, d2;
priority_queue < int > a1, a2;


int convTime(string curTime)
{
	int hour, mins;	
	sscanf(curTime.c_str(), "%d:%d", &hour, &mins);
	return hour * 60 + mins;
}

void trainTimetable(int testCase)
{
	int i, c;
	int addTime;
	int trainsAtA = 0, ansA = 0;
	int trainsAtB = 0, ansB = 0;

	char curTime[32];
	TrainTime curTrain;

	
	while (!d1.empty()) d1.pop(); while (!a1.empty()) a1.pop();
	while (!d2.empty()) d2.pop(); while (!a2.empty()) a2.pop();
	
	fscanf(in, "%d", &addTime);
	fscanf(in, "%d %d", &n1, &n2);
	for (i=0; i<n1; i++)
	{
		fscanf(in, "%s", curTime); curTrain.depart = convTime(curTime);
		fscanf(in, "%s", curTime); curTrain.arrive = convTime(curTime);
		d1.push(curTrain);
	}
	for (i=0; i<n2; i++)
	{
		fscanf(in, "%s", curTime); curTrain.depart = convTime(curTime);
		fscanf(in, "%s", curTime); curTrain.arrive = convTime(curTime);
		d2.push(curTrain);
	}
	
	for (i=0; i<n1 + n2; i++)
	{
		int nextTrain = -1;
		if (!d1.empty() && !d2.empty())
			nextTrain = d1.top() < d2.top() ? 2 : 1;
		else nextTrain = d1.empty() ? 2 : 1;
		
		if (nextTrain == 1)
		{
			curTrain = d1.top(); d1.pop();

			while (!a1.empty())
			{
				if (-a1.top() <= curTrain.depart) {trainsAtA++; a1.pop();}
				else break;
			}
			
			a2.push(-(curTrain.arrive + addTime));
			trainsAtA ? trainsAtA-- : ansA++;
		}
		else
		{
			curTrain = d2.top(); d2.pop();

			while (!a2.empty())
			{
				if (-a2.top() <= curTrain.depart) {trainsAtB++; a2.pop();}
				else break;
			}
			
			a1.push(-(curTrain.arrive + addTime));
			trainsAtB ? trainsAtB-- : ansB++;
		}
	}
	
	fprintf(out, "Case #%d: %d %d\n", testCase, ansA, ansB);
	return;
}

int main(void)
{
	int i, tests;

	in = fopen("TrainTimetable.in", "rt");
	out = fopen("TrainTimetable.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++) trainTimetable(i + 1);
	return 0;
}
