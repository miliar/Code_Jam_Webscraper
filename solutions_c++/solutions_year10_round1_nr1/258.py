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

const int dx[8] = { 0, 1, 1, 1};
const int dy[8] = { 1, 0, 1,-1};

VS board, newboard;
int n, k, who;

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		string tmp;
		board = VS();
		cin >> n >> k;
		REP(i,n) { cin >> tmp; board.PB(tmp); }

		newboard = VS(n,string(n,'.'));

		REP(x,n) {
			int y1 = 0;
			for(int y=n-1; y>=0; y--) {
// 				debug("%d %d\n",x,y);
				if ( board[x][y]!='.' ) {
					newboard[n-1-y1][n-1-x] = board[x][y];
					y1++;
				}
			}
		}

//		REP(i,n) cout << newboard[i] << endl;

		who = 0;

		REP(x,n) REP(y,n) REP(d,4) {
			if ( newboard[y][x]=='.' ) continue;
			int i;
			for(i=1; i<k; i++) {
				int x1 = x+dx[d]*i;
				int y1 = y+dy[d]*i;
				if ( x1<0 || x1>=n ||
				     y1<0 || y1>=n || newboard[y1][x1]!=newboard[y][x] ) break;
			}
			if ( i>=k ) who |= (newboard[y][x]=='R' ? 1 : 2);
		}

		printf("Case #%d: ",run);
		switch ( who ) {
		case 0: printf("Neither\n"); break;
		case 1: printf("Red\n"); break;
		case 2: printf("Blue\n"); break;
		case 3: printf("Both\n"); break;
		}
	}

	return 0;
}
