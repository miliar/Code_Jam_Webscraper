// GCJ 2011 R2
// wookayin

#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

#define problem "A"
#define testset "-large"

static int __threads = 4, __threadId = 0;

#define infile problem testset ".in"
#define outfile problem testset ".out"

#define REP(i, n) for(int i=0; i<(int)(n); ++i)
#define all(x) (x).begin(), (x).end()
using namespace std;

int X, S, R, t, N;
vector< pair<int, int> > walkway;

double go()
{
	int walkway_length = 0;

	double total_time = 0;
	double used_time = 0;

	for(int i = 0; i < N; ++ i)
	{
		walkway_length += walkway[i].second;	
	}

	walkway.push_back( make_pair(0, X - walkway_length) );
	sort(walkway.begin(), walkway.end(), less< pair<int, int> >());

	for(int i = 0; i < walkway.size(); ++ i)
	{
		if(used_time >= t)
		{
			total_time += walkway[i].second / (double)(S + walkway[i].first);
			continue;
		}

		int spd = walkway[i].first + R;
		double time = walkway[i].second / (double)spd;
		if(used_time + time > t)
		{
			// use less
			time = (t - used_time);
			used_time += time ;
			total_time += time ;
			// the rest
			double rem_length = (walkway[i].second - time * spd);
			total_time += rem_length / (S + walkway[i].first);
		}
		else
		{
			used_time += time;
			total_time += time;
		}
	}

	return total_time ;

}

int main(int argc, char *argv[])
{
	if(argc == 2) __threadId = atoi(argv[1]);
	else __threads = 1;

	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++tt) if(tt % __threads == __threadId)
	{
		scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
		walkway.clear();
		for(int i = 0; i < N; ++ i) {
			int b, e, spd;
			scanf("%d %d %d", &b, &e, &spd);
			walkway.push_back( make_pair(spd, e - b) );
		}

		printf("Case #%d: %.7lf \n", tt, go());
	}
	return 0;
}