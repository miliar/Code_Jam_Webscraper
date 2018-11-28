using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define REP(v, hi) for (int v=0; v<(hi); v++)
#define REPD(v, hi) for (int v=((hi)-1); v>=0; v--)
#define FOR(v, lo, hi) for (int v=(lo); v<(hi); v++)
#define FORD(v, lo, hi) for (int v=((hi)-1); v>=(lo); v--)
#define FORALL(it,x) for (typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector <string> VS;

const int dx[4] = {-1,0,1,0};
const int dy[4] = {0,1,0,-1};

const int MAX = 17;

struct state {
  int x,y,dist;
  int x1,y1,d1;
  int x2,y2,d2;
};

bool operator < (state a, state b) {
  return a.dist > b.dist;
}

char seen[MAX][MAX][MAX][MAX][5][MAX][MAX][5];

void solve () {

  int Y,X;
  scanf ("%i %i\n",&Y,&X);

  VS m(Y+2, string(X+2, '#'));
  REP(y,Y) {
    char t[X+10];
    scanf ("%s\n",t);
    m[y+1] = string("#") + t + "#";
  }

  X+=2;
  Y+=2;
  
  //  cout<<endl;
  //  REP(y,Y) cout<<m[y]<<endl;

  state start;
  start.x1 = 0;
  start.y1 = 0;
  start.d1 = 4;
  start.x2 = 0;
  start.y2 = 0;
  start.d2 = 4;
  start.dist = 0;

  memset(seen,0,sizeof(seen));
  REP(y,Y) REP(x,X) if (m[y][x]=='O') { start.y=y; start.x=x; }

  priority_queue<state> q;
  q.push(start);

  while (!q.empty()) {

    state s = q.top();
    q.pop();

    if (seen[s.y][s.x][s.y1][s.x1][s.d1][s.y2][s.x2][s.d2]) continue;
    seen[s.y][s.x][s.y1][s.x1][s.d1][s.y2][s.x2][s.d2] = 1;

    //    printf ("(%i,%i) (%i,%i/%i) (%i,%i/%i) : %i\n",s.y,s.x,s.y1,s.x1,s.d1,s.y2,s.x2,s.d2,s.dist);
    
    if (m[s.y][s.x] == 'X') {
      printf ("%i",s.dist);
      return;
    }

    REP(d1,4) {
      // shoot 1
      int ny=s.y, nx=s.x;
      while (m[ny][nx] != '#') ny+=dy[d1], nx+=dx[d1];
      if (ny!=s.y2 || nx!=s.x2 || d1!=s.d2) {
	state ns=s;
	ns.x1 = nx;
	ns.y1 = ny;
	ns.d1 = d1;
	q.push(ns);
      }
    }

    REP(d2,4) {
      // shoot 2
      int ny=s.y, nx=s.x;
      while (m[ny][nx] != '#') ny+=dy[d2], nx+=dx[d2];
      if (ny!=s.y1 || nx!=s.x1 || d2!=s.d1) {
	state ns=s;
	ns.x2 = nx;
	ns.y2 = ny;
	ns.d2 = d2;
	q.push(ns);
      }
    }

    REP(d,4) {
      //move
      int ny=s.y+dy[d], nx=s.x+dx[d];
      if (m[ny][nx] != '#') {
	state ns = s;
	ns.dist++;
	ns.x += dx[d];
	ns.y += dy[d];
	q.push(ns);
      }
      if (m[ny][nx] == '#') {
	if (s.d1==4 || s.d2==4) continue;
	
	if (ny==s.y1 && nx==s.x1 && d==s.d1) {
	  state ns = s;
	  ns.y = s.y2 + dy[(s.d2+2)%4];
	  ns.x = s.x2 + dx[(s.d2+2)%4];
	  ns.dist++;
	  q.push(ns);
	}

      	if (ny==s.y2 && nx==s.x2 && d==s.d2) {
	  state ns = s;
	  ns.y = s.y1 + dy[(s.d1+2)%4];
	  ns.x = s.x1 + dx[(s.d1+2)%4];
	  ns.dist++;
	  q.push(ns);
	}
      }
    }
  }
  
  printf ("THE CAKE IS A LIE");
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i: ",run);
    solve();
    printf ("\n");
  }

  return 0;
}
