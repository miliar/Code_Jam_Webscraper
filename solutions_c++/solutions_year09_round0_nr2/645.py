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

const int dx[8] = { 0,-1, 1, 0};
const int dy[8] = {-1, 0, 0, 1};

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

VVI h;
VVI basin;
int X, Y, nbasin;

map<int,char> label;
char lastlabel;

int dfs(int x, int y) {

	if ( basin[y][x]>=0 ) return basin[y][x];

	int xn = x, yn = y;
	REP(d,4) {
		int x1 = x + dx[d];
		int y1 = y + dy[d];

		if ( x1<0 || x1>=X ||
		     y1<0 || y1>=Y ) continue;

		if ( h[y1][x1]<h[yn][xn] ) {
			xn = x1;
			yn = y1;
		}
	}
	if ( xn==x && yn==y ) return basin[y][x] = nbasin++;

	return basin[y][x] = dfs(xn,yn);
}

int main()
{
	int nruns;

	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		cin >> Y >> X;
		h = VVI(Y,VI(X));
		nbasin = 0;
		basin = VVI(Y,VI(X,-1));
		REP(y,Y) REP(x,X) cin >> h[y][x];

		REP(y,Y) REP(x,X) dfs(x,y);

		printf("Case #%d:\n",run);
		label.clear();
		lastlabel = 'a';
		REP(y,Y) {
			REP(x,X) {
				if ( !label.count(basin[y][x]) ) label[basin[y][x]] = lastlabel++;
				printf("%c%c",label[basin[y][x]],(x==X-1 ? '\n' : ' '));
			}
		}
	}

	return 0;
}
