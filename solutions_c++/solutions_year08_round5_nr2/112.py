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
#define REP(i,n)  for(int i=0; i<(n); i++)
#define REPD(i,n) for(int i=(n)-1; i>=0; i--)

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const int infty = 999999999;

const int dx[8] = { 0, 1, 0,-1, 1, 1,-1,-1};
const int dy[8] = {-1, 0, 1, 0,-1, 1, 1,-1};

struct pos {
	int x,y;
};

struct portal {
	int x,y,d;
};

struct state {
	pos you;
	portal port[2];
	int d;
};

int operator ==(portal a, portal b) { return a.x==b.x && a.y==b.y && a.d==b.d; }

int operator <(state a, state b)
{
	if ( a.d!=b.d ) return a.d>b.d;
	if ( a.you.x!=b.you.x ) return a.you.x<b.you.x;
	if ( a.you.y!=b.you.y ) return a.you.y<b.you.y;
	REP(i,2) {
		if ( a.port[i].x!=b.port[i].x ) return a.port[i].x<b.port[i].x;
		if ( a.port[i].y!=b.port[i].y ) return a.port[i].y<b.port[i].y;
		if ( a.port[i].d!=b.port[i].d ) return a.port[i].d<b.port[i].d;
	}
	return 0;
}

int X,Y;
VS mp;
pos cake;

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {
		scanf("%d %d\n",&Y,&X);

		mp = VS(Y+2,string(X+2,'#'));

		state start;
		REP(i,2) {
			start.port[i].x = 0;
			start.port[i].y = 0;
			start.port[i].d = -1;
		}
		start.d = 0;
		
		REP(y,Y) {
			REP(x,X) {
				scanf("%c",&mp[y+1][x+1]);
				if ( mp[y+1][x+1]=='O' ) {
					start.you.x = x+1;
					start.you.y = y+1;
				}
				if ( mp[y+1][x+1]=='X' ) {
					cake.x = x+1;
					cake.y = y+1;
				}
			}
			scanf("\n");
		}

		X += 2;
		Y += 2;

//		REP(y,Y) debug("%s\n",mp[y].c_str());
//		debug("cake: %d,%d  you = %d,%d\n",cake.x,cake.y,start.you.x,start.you.y);

		priority_queue<state> que;
		que.push(start);
		map<state,int> dist;
//		dist[start] = 0;
		int res = infty;
		
		while ( !que.empty() ) {
			state curr = que.top(); que.pop();

			state tmp = curr;
			tmp.d = 0;
			if ( dist.count(tmp) && dist[tmp]<=curr.d ) continue;
			dist[tmp] = curr.d;
			
//			debug("@ %d,%d, dist = %d\n",curr.you.x,curr.you.y,dist[tmp]);
			
			if ( curr.you.x==cake.x && curr.you.y==cake.y ) {
				res = curr.d;
				break;
			}
			
			REP(d,4) { // walk
				state next = curr;
				next.d = curr.d + 1;
				next.you.x += dx[d];
				next.you.y += dy[d];
				REP(i,2) {
					if ( curr.you.x==curr.port[i].x &&
						 curr.you.y==curr.port[i].y &&
						 d==curr.port[i].d && curr.port[1-i].d>=0 ) {
						next.you.x = curr.port[1-i].x;
						next.you.y = curr.port[1-i].y;
						que.push(next);
					}
				}
				if ( mp[next.you.y][next.you.x]=='#' ) continue;
				que.push(next);
			}

			REP(d,4) { // shoot
				portal newp;
				newp.x = curr.you.x;
				newp.y = curr.you.y;
				newp.d = d;
				while ( mp[newp.y+dy[d]][newp.x+dx[d]]!='#' ) {
					newp.x += dx[d];
					newp.y += dy[d];
				}
				REP(i,2) {
					if ( !(newp==curr.port[1-i]) ) {
						state next = curr;
						next.port[i] = newp;
						que.push(next);
					}
				}
			}
		}

		if ( res==infty )
			printf("Case #%d: THE CAKE IS A LIE\n",run+1);
		else
			printf("Case #%d: %d\n",run+1,res);
	}

	return 0;
}
