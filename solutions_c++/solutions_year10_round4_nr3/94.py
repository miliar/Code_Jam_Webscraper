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
#define REP(i,n) for(int i=0; i<(n); ++i)

const int infty = 999999999;

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

VVI bact;

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {
		int r;
		cin >> r;
		int x1, y1, x2, y2;

		bact = VVI(110,VI(110,0));
		REP(i,r) {
			cin >> x1 >> y1 >> x2 >> y2;
			for(int x = x1; x<=x2; x++)
				for(int y = y1; y<=y2; y++)
					bact[y][x] = 1;
		}

		int t = 0;
		int nbact;
		do {
			nbact = 0;
			VVI newbact = bact;
			REP(y,bact.size()) REP(x,bact[0].size()) {
				int haveN = (y>0 && bact[y-1][x]);
				int haveW = (x>0 && bact[y][x-1]);
				if ( haveN && haveW ) newbact[y][x] = 1;
				if ( !(haveN || haveW) ) newbact[y][x] = 0;
				nbact += newbact[y][x];
			}

			bact = newbact;
			t++;
		} while ( nbact>0 );

		printf("Case #%d: %d\n",run,t);
	}

	return 0;
}
