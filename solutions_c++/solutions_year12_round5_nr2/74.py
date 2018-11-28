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
#define REP(i,n) for(typeof(n) i=0; i<(n); ++i)

const int infty = 999999999;

template<class T> void minimize(T &a, T b) { a = min(a,b); }
template<class T> void maximize(T &a, T b) { a = max(a,b); }

//#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

const int dx[6] = {-1, 0, 1, 1, 0, -1};
const int dy[6] = { 0, 1, 1, 0,-1, -1};

int S, M;

int onboard(int x, int y)
{
	if ( x<=0 || y<=0 ||
	     x>=2*S || y>=2*S ) return 0;
	if ( (x>=S && y<=x-S) ||
	     (y>=S && x<=y-S) ) return 0;
	return 1;
}

int corner(int x, int y)
{
	if ( x==1     && y==1     ) return 0;
	if ( x==1     && y==S     ) return 1;
	if ( x==S     && y==2*S-1 ) return 2;
	if ( x==2*S-1 && y==2*S-1 ) return 3;
	if ( x==2*S-1 && y==S     ) return 4;
	if ( x==S     && y==1     ) return 5;
	return -1;
}

int edge(int x, int y)
{
	if ( corner(x,y)>=0 ) return -1;
	if ( x==1 ) return 0;
	if ( x==y-S+1 ) return 1;
	if ( y==2*S-1 ) return 2;
	if ( x==2*S-1 ) return 3;
	if ( y==x-S+1 ) return 4;
	if ( y==1     ) return 5;
	return -1;
}

struct comp {
	set< pair<int,int> > pos;
	set< int > edges, corners;
};

VVI used, filled;
vector<comp> comps;

int edgefill(int x, int y, int c)
{
	debug("fill %d,%d = %d",x,y,c);
	int border = 0;
	filled[x][y] = c;
	if ( edge(x,y)>=0 || corner(x,y)>=0 ) { border = 1; debug("  border"); }
	debug("\n");

	REP(d,6) {
		int x1 = x + dx[d];
		int y1 = y + dy[d];
		if ( onboard(x1,y1) && !used[x1][y1] && filled[x1][y1]==0 ) {
			border |= edgefill(x1,y1,c);
		}
	}

	return border;
}

int main()
{
	int run, nruns;

	cin >> nruns;

	for(run=1; run<=nruns; run++) {

		cin >> S >> M;

		debug("run %d: S = %d, M = %d\n",run,S,M);

		comps.clear();
		used = VVI(2*S,VI(2*S,0));

		int bridge = 0;
		int fork = 0;
		int ring = 0;

		int i;
		for(i=1; i<=M; i++) {
			int x, y;
			cin >> x >> y;
			pair<int,int> p(x,y);

			debug("move %d: %d,%d\n",i,x,y);
			used[x][y] = 1;

			comp tmp;
			tmp.pos.insert(p);
			int e;
			if ( (e=corner(x,y))>=0 ) tmp.corners.insert(e);
			if ( (e=edge(x,y))  >=0 ) tmp.edges.insert(e);

			REP(d,6) {
				int x1 = x + dx[d];
				int y1 = y + dy[d];
				pair<int,int> p1(x1,y1);
				if ( !onboard(x1,y1) ) continue;
				REP(j,comps.size()) {
					if ( comps[j].pos.count(p1) ) {
						tmp.pos.insert(ALL(comps[j].pos));
						tmp.corners.insert(ALL(comps[j].corners));
						tmp.edges.insert(ALL(comps[j].edges));
						comps.erase(comps.begin()+j);
						break;
					}
				}
			}
			comps.push_back(tmp);

			/*
			REP(j,comps.size()) {
				debug("comp %d has %d elements:\n",j,comps[j].pos.size());
				FOR(it,comps[j].pos) debug("%d,%d ",it->first,it->second); debug("\n");
				debug("edges:");
				FOR(it,comps[j].edges) debug(" %d",*it); debug("\n");
				debug("corners:");
				FOR(it,comps[j].corners) debug(" %d",*it); debug("\n");
			}
			*/

			REP(j,comps.size()) {
				if ( comps[j].corners.size()>=2 ) bridge = 1;
				if ( comps[j].edges.size()  >=3 ) fork = 1;
			}

			filled = VVI(2*S,VI(2*S,0));
			int c = 0;
			for(x=1; x<2*S; x++) {
				for(y=max(1,x-S+1); y<min(2*S-1,x+S); y++) {
					if ( filled[x][y]==0 && !used[x][y] ) {
						if ( !edgefill(x,y,++c) ) {
							ring = 1;
							goto ringfound;
						}
					}
				}
			}
		  ringfound:

			for(int y1=2*S-1; y1>=1; y1--) {
				for(int x1=2*S-1; x1>=1; x1--) {
					char c = ' ';
					if ( onboard(x1,y1) ) {
						if ( used[x1][y1] ) { c = '#'; } else { c = '0'+filled[x1][y1]; }
					}
					debug("%c",c);
				}
			    debug("\n");
			}

			if ( bridge || fork || ring ) break;
		}

		cout << "Case #" << run << ": ";
		if ( i>M ) {
			cout << "none" << endl;
		} else {
			string what;
			if ( bridge ) what = "bridge";
			if ( fork ) what += ( what.length()>0 ? "-" : "" ) + string("fork");
			if ( ring ) what += ( what.length()>0 ? "-" : "" ) + string("ring");
			cout << what << " in move " << i << endl;

		}

		for(i++; i<=M; i++) {
			int x, y;
			cin >> x >> y;
		}
	}

	return 0;
}
