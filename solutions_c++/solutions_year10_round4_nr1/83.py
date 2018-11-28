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

int k;
VS diamond;

int xy2k(int x, int y, int x0, int y0)
{
	return abs(x-x0) + abs(y-y0) + 1;
}

int symm(int x0, int y0)
{
	int res = k;
	REP(y,diamond.size()) {
		REP(x,diamond[y].size()) {
			if ( diamond[y][x]==' ' ) continue;
			int x1, y1;
			x1 = 2*x0 - x;
			y1 = y;
			if ( y1<0 || y1>=diamond.size() ||
			     x1<0 || x1>=diamond[y1].size() ||
			     diamond[y1][x1]==' ' ) {
				res = max(res,xy2k(x1,y1,x0,y0));
			} else {
				if ( diamond[y1][x1]!=diamond[y][x] ) return -1;
			}
			x1 = x;
			y1 = 2*y0 - y;
			if ( y1<0 || y1>=diamond.size() ||
			     x1<0 || x1>=diamond[y1].size() ||
			     diamond[y1][x1]==' ' ) {
				res = max(res,xy2k(x1,y1,x0,y0));
			} else {
				if ( diamond[y1][x1]!=diamond[y][x] ) return -1;
			}
		}
	}
	return res;
}

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {
		scanf("%d",&k);
		while ( getc(stdin)!='\n' );

		char buff[1024];
		diamond = VS(2*k-1);

		REP(i,2*k-1) {
			gets(buff);
			diamond[i] = buff;
//			debug("'%s'\n",diamond[i].c_str());
		}

		int best = infty;
		REP(y0,2*k-1) REP(x0,2*k-1) {
			int curr = symm(x0,y0);
//			debug("k = %d at %d,%d\n",curr,x0,y0);
			if ( curr>=0 && curr<best ) {
				best = curr;
			}
		}

		printf("Case #%d: %d\n",run,best*best - k*k);
	}

	return 0;
}
