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
  scanf ("%d",&N);
  VI x(N+2),r(N+1);
  x[0]=r[0]=0;
  REP(i,N) scanf ("%d %d",&x[i+1],&r[i+1]);
  scanf ("%d",&x[N+1]);
  N+=2;
  
  VI p(N,-1);
  p[1] = 0;

  FOR(i,2,N) {
    FOR(j,p[i-1],i) {
      if (p[j]==-1) continue;
      int R = min(r[j], x[j]-x[p[j]]);
      if (x[j] + R >= x[i]) {
	p[i] = j;
	//	printf ("prev[%d]=%d\n",i,j);
	break;
      }
    }

    if (p[i]==-1) break;
  }

  if (p[N-1]==-1)
    printf ("NO");
  else
    printf ("YES");
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
