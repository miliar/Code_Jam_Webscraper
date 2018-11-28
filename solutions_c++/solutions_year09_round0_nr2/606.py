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

const int dy[4] = {-1,0,0,1};
const int dx[4] = {0,-1,1,0};

void solve () {

  int Y,X;
  cin>>Y>>X;
  VVI h(Y,VI(X));
  REP(y,Y) REP(x,X) cin>>h[y][x];

  VVI to(Y,VI(X,-1));
  REP(y,Y) REP(x,X) {
    int besth=h[y][x];
    REP(d,4) {
      int ny=y+dy[d],nx=x+dx[d];
      if (ny<0 || ny>=Y || nx<0 || nx>=X) continue;
      if (h[ny][nx] < besth) besth=h[ny][nx], to[y][x]=d;
    }
  }

  VVI n(Y,VI(X,-1));
  int num=0;
  
  REP(y,Y) REP(x,X) if (n[y][x]==-1) {
    queue<int> q;
    q.push(y);
    q.push(x);
    n[y][x]=num;
    
    while (!q.empty()) {
      int yy=q.front(); q.pop();
      int xx=q.front(); q.pop();

      REP(d,4) {
	int ny=yy+dy[d],nx=xx+dx[d];
	if (ny<0 || ny>=Y || nx<0 || nx>=X) continue;
	if ((to[ny][nx]==3-d || to[yy][xx]==d) && n[ny][nx]==-1) {
	  n[ny][nx]=num;
	  q.push(ny);
	  q.push(nx);
	}
      }
    }

    num++;
  }

  REP(y,Y) REP(x,X) 
    printf ("%c%c",'a'+n[y][x],x<X-1?' ':'\n');
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i:\n",run);
    solve();
  }

  return 0;
}
