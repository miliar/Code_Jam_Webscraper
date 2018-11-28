#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
using namespace std;
#define MAX 200

struct Train
{
	bool directiveB;
	int tstart, tend;
	Train(){directiveB = false; tstart = tend = 0; }
	bool operator < (const Train& T) const
	{
		return tstart < T.tstart;
	}
};

int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int N;
	scanf("%d", &N);
	int i, j, k;
	for(k = 0 ; k < N ; ++k)
	{
		Train trains[MAX + 1];
		int NA, NB, TT;
		scanf("%d\n", &TT);
		scanf("%d %d\n", &NA, &NB);
		for(i = 0 ; i < NA ; ++i)
		{
			char buff[20];
			int ms, hs, me, he;
			gets(buff);
			sscanf(buff, "%d:%d %d:%d", &hs, &ms, &he, &me);
			trains[i].tstart = hs*60 + ms;
			trains[i].tend = he*60 + me;
			trains[i].directiveB = true;
			assert(trains[i].tstart >= 0 && trains[i].tstart < 1440 && trains[i].tend > 0 && trains[i].tend < 1440);
		}
		for(i = NA ; i < NB + NA ; ++i)
		{
			char buff[20];
			int ms, hs, me, he;
			gets(buff);
			sscanf(buff, "%d:%d %d:%d", &hs, &ms, &he, &me);
			trains[i].tstart = hs*60 + ms;
			trains[i].tend = he*60 + me;
			trains[i].directiveB = false;
			assert(trains[i].tstart >= 0 && trains[i].tstart < 1440 && trains[i].tend > 0 && trains[i].tend < 1440);
		}
		sort(trains, trains + (NA + NB));
		int AB[2][1500] = {0};
		int time, ansAB[2] = {0};
		for(i = 0 ; i < NA + NB ; ++i)
		{
			time = trains[i].tstart;
			assert(time >= 0 && time < 1440);
			if(AB[trains[i].directiveB][time] > 0)
			{
                for(j = time ; j < 1440 ; ++j)AB[trains[i].directiveB][j]--;
			}
			else
			{
				ansAB[trains[i].directiveB]++;
			}
			assert(AB[trains[i].directiveB][time] >= 0);
			for(j = trains[i].tend + TT ; j < 1440 ; ++j)AB[!trains[i].directiveB][j]++;
		}
		printf("Case #%d: %d %d\n", k + 1, ansAB[1], ansAB[0]);
	}
	return 0;
}


