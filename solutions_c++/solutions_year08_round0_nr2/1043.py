#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <algorithm>
#include <cmath>

#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;

#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define FORI(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define mp make_pair

multiset<int> available[2];
vector< pair<pair<int, int>, int> > events;

inline int getTime( int hour, int min )
{
	return hour * 60 + min;
}

int main()
{
//	freopen("B.in", "rt", stdin);
//	freopen("B.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int TIME, Na, Nb;
		scanf("%d %d %d", &TIME, &Na, &Nb);
		events.clear(); available[0].clear(); available[1].clear();
		for (int i = 0; i < Na; i++)
		{
			int hourS, minS, hourD, minD;
			scanf("%d:%d %d:%d", &hourS, &minS, &hourD, &minD);
			events.push_back( make_pair( make_pair( getTime(hourS, minS), getTime(hourD, minD) ), 0 ) );
		}
		for (int i = 0; i < Nb; i++)
		{
			int hourS, minS, hourD, minD;
			scanf("%d:%d %d:%d", &hourS, &minS, &hourD, &minD);
			events.push_back( make_pair( make_pair( getTime(hourS, minS), getTime(hourD, minD) ), 1 ) );
		}

		sort( ALL(events) );
		int NR[2] = {0, 0};
		for (size_t k = 0; k < events.size(); k++)
		{
			int place = events[k].second, time = events[k].first.first, arrivalTime = events[k].first.second;

			if (available[place].empty() || (*available[place].begin()) > time)
				NR[place]++;
			else
				available[place].erase( available[place].begin() );

			available[1 ^ place].insert( arrivalTime + TIME );
		}

		printf("Case #%d: %d %d\n", t, NR[0], NR[1]);
	}

	return 0;
}


