// Space.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <cassert>

using namespace std;

const int MaxC = 1000;

bool debug = false;

int _tmain(int argc, _TCHAR* argv[])
{

	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int L, N, C;
		int distance[MaxC];
		long long buildTime;

		scanf("%d %lld %d %d", &L, &buildTime, &N, &C);

		for (int c = 0; c < C; c++)
		{
			scanf("%d", &distance[c]);
		}

		long long time = 0;
		int c = 0;
	    int firstBuildPos;
		int totalDist = 0;
		multiset<int> boostDist;
		
		// find which start we will be at when boosters are complete
		for (int i = 0; i < N; i++)
		{
			long long dt;
			dt = buildTime - time;
			assert(dt % 2 == 0);

			int dist = distance[c];
			totalDist += dist;
			int remDist;
			
			if (time >= buildTime)
			{
				boostDist.insert(dist);
			}
			else if (time + dist * 2 > buildTime)
			{
				remDist = dist - dt / 2;
				assert(remDist > 0);
				boostDist.insert(remDist);
				time = buildTime;

				if (debug)
				{
					printf("completed star %d dist %d remDist %d\n", i, dist, remDist);
				}
			}
			else
			{
  			  time += dist * 2;
			}

			c++;
			if (c == C)
				c = 0;
		}

		int totalBoostDist = 0;
		int l = 0;

		for (multiset<int>::reverse_iterator iter = boostDist.rbegin();
			 iter != boostDist.rend(); iter++)
		{
			if (l >= L)
				break;
			l++;
			totalBoostDist += *iter;
		}
	    
		int unboostDist = totalDist - totalBoostDist;
		int totalTime = unboostDist *2 + totalBoostDist;

		if (debug)
			printf("unboostDist %d boostDist %d totalDist %d\n",
			       unboostDist, totalBoostDist, totalDist);
		printf("Case #%d: %d\n", t, totalTime);
	}

	return 0;
}