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
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define UNIQUE(x) x.erase(unique(ALL(x)),x.end())
#define REP(x, hi) for (int x=0; x<(hi); x++)
#define REPD(x, hi) for (int x=((hi)-1); x>=0; x--)
#define FOR(x, lo, hi) for (int x=(lo); x<(hi); x++)
#define FORD(x, lo, hi) for (int x=((hi)-1); x>=(lo); x--)
#define FORALL(it,x) for (typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<string> VS;

const int inf = 999999999;

/////////////////////////////////////////////////////////////////////////////////////////////////

const int dy[4] = {-1,1,0,0};
const int dx[4] = {0,0,-1,1};

int Y,X;
VS m;

VVI bfs (int y0, int x0) {

  VVI dist(Y, VI(X,inf));
  queue<int> q;
  q.push(y0);
  q.push(x0);
  q.push(0);
  
  while (!q.empty()) {
    int y=q.front(); q.pop();
    int x=q.front(); q.pop();
    int d=q.front(); q.pop();
    if (dist[y][x]!=inf) continue;
    dist[y][x]=d;
    REP(dd,4) {
      int ny=y+dy[dd], nx=x+dx[dd];
      if (ny<0 || ny>=Y || nx<0 || nx>=X) continue;
      if (m[ny][nx] == '.') continue;
      q.push(ny);
      q.push(nx);
      q.push(d+1);
    }
  }

  return dist;
}
  
void solve () {

  cin>>Y>>X;
  m=VS(Y);
  REP(y,Y) cin>>m[y];
  
  VVI d=bfs(0,0);

  int ty=0,tx=0;
  int res=0;
  VVI u(Y, VI(X, 0));

  REP(y2,Y) REP(x2,X) if (m[y2][x2]=='T') {
    int y=ty=y2;
    int x=tx=x2;
    
    while (d[y][x]>0) {
      u[y][x] = 1;
      res += d[y][x];
      
      REP(dd,4) {
	int ny=y+dy[dd], nx=x+dx[dd];
	if (ny<0 || ny>=Y || nx<0 || nx>=X) continue;
	if (d[ny][nx] < d[y][x]) {
	  y=ny;
	  x=nx;
	  break;
	}
      }
    }
  }

  VVI d1 = bfs(0,0);
  VVI d2 = bfs(ty,tx);

  //  printf("tree = %i,%i (res=%i)\n",ty,tx,res);
  
  REP(y,Y) REP(x,X) d[y][x] = min(d1[y][x], d2[y][x]);
  //  REP(y,Y) { REP(x,X) printf ("%i(%i) ",d[y][x],u[y][x]); printf ("\n"); }
  
  REP(y,Y) REP(x,X) if (!u[y][x] && m[y][x]!='.') res += d[y][x];

  cout<<res;
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
