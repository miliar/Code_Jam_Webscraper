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
typedef vector<VVI> VVVI;
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

int X, Y, F;

struct pos {
	int x,y;
	int d;

	VS cave;
};

int operator <(pos a, pos b)
{
	if ( a.x!=b.x ) return a.x<b.x;
	if ( a.y!=b.y ) return a.y<b.y;
	return a.cave < b.cave;
}

int best;

int main()
{
	int nruns;

	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		cin >> Y >> X >> F;

		pos s;
		s.cave = VS(Y);
		REP(y,Y) cin >> s.cave[y];

		best = infty;

		s.x = s.y = 0;
		s.d = 0;
		queue<pos> que;
		que.push(s);

		set<pos> visited;
		while ( !que.empty() ) {
			pos q, p = que.front(); que.pop();

			if ( visited.count(p) || p.d>=best ) continue;
			visited.insert(p);
			if ( p.y==Y-1 && p.d<best ) best = p.d;

// 			debug("%d %d\n",p.x,p.y);
// 			REP(i,Y) debug("%s\n",p.cave[i].c_str());
// 			debug("d = %d, best = %d\n",p.d,best);

			for(int s=-1; s<=1; s+=2) {
				if ( p.x+s>=0 && p.x+s<X && p.cave[p.y][p.x+s]=='.' ) {
					q = p;
					q.x += s;
					while ( q.y<Y-1 && q.cave[q.y+1][q.x]=='.' ) q.y++;
					if ( q.y - p.y <= F ) que.push(q);

					if ( p.y<Y-1 && p.cave[p.y+1][p.x+s]=='#' ) {
						q = p;
						q.d++;
						q.cave[p.y+1][p.x+s] = '.';
						que.push(q);
					}
				}
			}
		}

		if ( best==infty ) {
			printf("Case #%d: No\n",run,best);
		} else {
			printf("Case #%d: Yes %d\n",run,best);
		}

	}

	return 0;
}
