#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

struct Train {
	int time;
	bool arrive;

	Train() {}
	Train(int h, int m, bool ar) : time(h*60 + m), arrive(ar) {}
	bool operator<(const Train& rhs) {
		if (time == rhs.time)
			return (arrive?0:1) < (rhs.arrive?0:1);
		return time < rhs.time;
	}
};

int num_of_start(const vector<Train>& v)
{
	int start=0;
	int wait=0;
	for(int j=0;j<v.size();j++)
	{
		if (v[j].arrive)
		{
			wait++;
		}
		else if (wait > 0)
		{
			wait--;
		}
		else
		{
			start++;
		}
	}
	return start;
}

int main()
{
	int N;
	cin>>N;
	for (int i = 0;i<N;i++)
	{
		int T, NA, NB;
		cin>>T>>NA>>NB;
		vector<Train> station_a, station_b;
		for(int j=0;j<NA;j++)
		{
			int lh,lm,ah,am;
			scanf("%d:%d %d:%d", &lh, &lm, &ah, &am);
			station_a.push_back(Train(lh,lm, false));
			station_b.push_back(Train(ah,am+T, true));
		}

		for(int j=0;j<NB;j++)
		{
			int lh,lm,ah,am;
			scanf("%d:%d %d:%d", &lh, &lm, &ah, &am);
			station_b.push_back(Train(lh,lm, false));
			station_a.push_back(Train(ah,am+T, true));
		}
		std::sort(station_a.begin(), station_a.end());
		std::sort(station_b.begin(), station_b.end());

		int start_a = num_of_start(station_a);
		int start_b = num_of_start(station_b);
		printf("Case #%d: %d %d\n", i+1, start_a, start_b);
	}

	return 0;
}
