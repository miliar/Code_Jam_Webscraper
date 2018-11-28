#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>

#define MAX 1024
#define EPS 0.00000001

using namespace std;
FILE *in; FILE *out;

struct Walkway
{
	double start, end, speed;
	bool operator < (const Walkway& r) const
	{
		return start != r.start ? start < r.start : end < r.end;
	}
};

int n;
Walkway a[MAX];
double len, walk, run, tt;

double calc(double walkDist, vector < pair <double, double> > v, double t)
{
	double totalTime = 0;
	double curTime = walkDist / run;

	// Running the whole time
	if (t + EPS > curTime)
	{
		t -= curTime;
		totalTime += curTime;
	}
	// Running only some of the time
	else
	{
		totalTime += (walkDist - t * run) / walk + t;
		t = 0;
	}

	sort(v.begin(), v.end());
	for (int i = 0; i < (int)v.size(); i++)
	{
		if (t < EPS)
		{
			totalTime += v[i].second / (walk + v[i].first);
		}
		else
		{
			if (t + EPS > v[i].second / (run + v[i].first))
			{
				t -= v[i].second / (run + v[i].first);
				totalTime += v[i].second / (run + v[i].first);
			}
			else
			{
				totalTime += (v[i].second - t * (run + v[i].first)) / (walk + v[i].first) + t;
				t = 0;
			}
		}
	}
	return totalTime;
}

void doWork(int testNum)
{
	fscanf(in, "%lf %lf %lf %lf", &len, &walk, &run, &tt);
	fscanf(in, "%d", &n);
	for (int i = 0; i < n; i++)
		fscanf(in, "%lf %lf %lf", &a[i].start, &a[i].end, &a[i].speed);
	sort(a, a + n);
	
	int idx = 0;
	double ans = 0;
	double totalWalk = 0;
	double totalTime = 0, pos = 0;
	
	vector < pair <double, double> > v;
	while (idx < n)
	{
		if (a[idx].end + EPS > len)
			break;
		
		totalWalk += a[idx].start - pos;
		v.push_back(make_pair(a[idx].speed, a[idx].end - a[idx].start));
		pos = a[idx++].end;
	}
	// Do not use last walkway (if it exists)
	ans = calc(totalWalk + len - pos, v, tt);
	
	// Use kast walkway
	if (idx < n)
	{
		v.push_back(make_pair(a[idx].speed, a[idx].end - a[idx].start));
		ans = min(ans, calc(totalWalk + a[idx].start - pos + a[idx].end - len, v, tt));
	}
	fprintf(out, "%.9lf\n", ans);
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("AirportWalkways.in", "rt");
	out = fopen("AirportWalkways.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
