using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
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

void solve () {
  int X,Y,dx1,dy1,dx2,dy2,x0,y0;
  cin>>X>>Y>>dx1>>dy1>>dx2>>dy2>>x0>>y0;

  int res=0;
  queue<int> q;
  q.push(x0);
  q.push(y0);

  VVI u(Y,VI(X,0));
  while (!q.empty()) {
    int x = q.front(); q.pop();
    int y = q.front(); q.pop();
    if (x<0||x>=X||y<0||y>=Y) continue;
    if (u[y][x]) continue;
    u[y][x]=1;
    res++;

    q.push(x+dx1);
    q.push(y+dy1);
    q.push(x+dx2);
    q.push(y+dy2);
  }

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
