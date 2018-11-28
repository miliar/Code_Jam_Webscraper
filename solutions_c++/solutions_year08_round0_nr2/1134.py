using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define PB push_back
#define ALL(x) ((x).begin()),((x).end())
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)

const int infty = 999999999;

//#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

const int maxN = 110;

int T, NA, NB;

struct trip {
	int loc;
	int dep, arr;
};

int operator <(trip a, trip b)
{
	if ( a.dep!=b.dep ) return a.dep<b.dep;
	return a.arr<b.arr;
}

struct train {
	int loc; // 0 = A, 1 = B
	int dep; // earliest ready for departure
};

int operator <(train a, train b)
{
	return a.dep>b.dep;
}


vector<trip> trips;

int main()
{
	int run, nruns;

	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {
		scanf("%d\n",&T);
		scanf("%d %d\n",&NA,&NB);

		int h1,m1,h2,m2;
		trips = vector<trip>(NA+NB);
		for(int i=0; i<NA; i++) {
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			trips[i].loc = 0;
			trips[i].dep = h1*60+m1;
			trips[i].arr = h2*60+m2;
		}
		for(int i=NA; i<NA+NB; i++) {
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			trips[i].loc = 1;
			trips[i].dep = h1*60+m1;
			trips[i].arr = h2*60+m2;
		}

		sort(ALL(trips));

		priority_queue<train> trains[2];

		VI res(2,0);
		for(int i=0; i<trips.size(); i++) {
			int l = trips[i].loc;
			if ( trains[l].empty() || trains[l].top().dep>trips[i].dep ) {
				res[l]++;
				debug("new train: %d at %02d:%02d\n",
					  l,trips[i].dep/60,trips[i].dep%60);
			} else {
				debug("old train: %d at %02d:%02d ready %02d:%02d\n",
					  l,trips[i].dep/60,trips[i].dep%60,
					  trains[l].top().dep/60,trains[l].top().dep%60);
				trains[l].pop();
			}
			train tmp;
			tmp.loc = 1-l;
			tmp.dep = trips[i].arr + T;
			debug("train ready loc = %d at %02d:%02d\n",
				  tmp.loc,tmp.dep/60,tmp.dep%60);
			trains[tmp.loc].push(tmp);
		}

		printf("Case #%d: %d %d\n",run+1,res[0],res[1]);
	}

	return 0;
}
