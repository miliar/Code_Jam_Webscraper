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

int Y,X,res,tmp;
VVI n;

void add(int y, int x, int a) {
  //  printf ("(%i,%i) -> %i\n",y,x,-a);
  FOR(dy,-1,2) FOR(dx,-1,2) {
    int ny=y+dy, nx=x+dx;
    if (ny<0 || ny>=Y || nx<0 || nx>=X) continue;
    n[ny][nx] += a;
  }
}

void go (int y, int x) {

  if (y==Y) {
    //    printf ("ok!\n");
    REP(yy,Y) REP(xx,X) if (n[yy][xx]) return;
    res = max(res,tmp);
    return;
  }

  if (x==X) {
    go(y+1,0);
    return;
  }
  
  if (y>0 && x>0) {
    if (n[y-1][x-1]==1) {
      add(y,x,-1);
      if (y==Y/2) tmp++;
      go(y,x+1);
      if (y==Y/2) tmp--;
      add(y,x,+1);
    }
    if (n[y-1][x-1]==0) {
      go(y,x+1);
    }

    return;
  }

  go(y,x+1);

  add(y,x,-1);
  if (y==Y/2) tmp++;
  go(y,x+1);
  if (y==Y/2) tmp--;
  add(y,x,+1);  
}

void solve () {

  cin>>Y>>X;
  n=VVI(Y,VI(X,0));
  REP(y,Y) REP(x,X) cin>>n[y][x];
  
  res=tmp=0;
  go(0,0);
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
