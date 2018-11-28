#include<iostream>
#include<vector>
#include<cstring>
#include<stdio.h>
#include<string>
#include<cassert>
#include<algorithm>
#include<iomanip>
using namespace std;

#define forn(i,n) for (int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 1010

// We have exactly one option of where we will end up
// Calculate the least amount of time you need to get the target
// A bunch of pairs (diatance, speed) pairs
// Sort them by speed
// Run at the slower places

// 10 ^ 10 should work in time. But TEST is first. 

int corridor_length, walk_speed, run_speed, max_run_time, n;
int begin[sz], end[sz], walkway_speed[sz];

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
		// input
		scanf("%d %d %d %d %d", &corridor_length, &walk_speed, &run_speed, &max_run_time, &n);
		run_speed -= walk_speed; 
		for (int i = 0; i < n; i++) scanf("%d %d %d", &begin[i], &end[i], &walkway_speed[i]);
		
		// make speed, distance pairs
		vector < pair < int, int > > pairs;
		int sum = 0; 
		for (int i = 0; i < n; i++) {
			pairs.push_back(make_pair(walkway_speed[i] + walk_speed, end[i] - begin[i]));
			sum += end[i] - begin[i];
		} sum = corridor_length - sum;
		pairs.push_back(make_pair(walk_speed, sum));
		sort(pairs.begin(), pairs.end());

		// Run for as long as you can!!
		double time = 0.0;
		double run_time_remaining = double(max_run_time);
		double run_for, walk_distance, walk_for; 
		for (int i = 0; i < pairs.size(); i++) {
			run_for = min(run_time_remaining, double ( pairs[i].second ) / double ( pairs[i].first + run_speed ) );
			run_time_remaining -= run_for;
			walk_distance = pairs[i].second - run_for * double ( pairs[i].first + run_speed );
			walk_for = walk_distance / double( pairs[i].first );
			time += run_for + walk_for;

// 			cout << pairs[i].first << ' ' << pairs[i].second << ' ' << run_for << ' ' << walk_for << endl; 
		}

		// output
        cout << setprecision(8) << "Case #" << test+1 << ": " << time << endl;
    }
    return 0;
}
