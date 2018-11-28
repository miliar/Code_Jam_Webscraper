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

void solve () {
  int N;
  cin>>N;
  int S=2*N-1;
  
  VS a(S);
  getline(cin,a[0]);
  REP(i,S) {
    getline(cin,a[i]);
    while (a[i].SZ < S) a[i]+=" ";
  }
  
  int res=inf;
  
  REP(y0,S) REP(x0,S) {

    int err=0;
    int sz=0;
    
    REP(y,S) REP(x,S) if (isdigit(a[y][x])) {

      VI nxs,nys;
      nxs.PB(x);
      nxs.PB(2*x0-x);
      nys.PB(y);
      nys.PB(2*y0-y);

      REP(xi,nxs.SZ) REP(yi,nys.SZ) {
	int nx=nxs[xi], ny=nys[yi];
	sz >?= abs(nx-x0) + abs(ny-y0);
	
	if (ny>=0 && ny<S && nx>=0 && nx<S && isdigit(a[ny][nx]) && a[ny][nx]!=a[y][x]) err=1;
      }
    }
      
    if (!err) {
      res <?= (sz+1)*(sz+1);
    }
  }

  cout << res - N*N;
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
