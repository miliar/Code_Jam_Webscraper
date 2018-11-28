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

const int dx[4] = {0,1,1,1};
const int dy[4] = {1,0,-1,1};

int N,K;
VS s;

int go (char c) {
  int res=0;
  REP(y0,N) REP(x0,N) REP(d,4) {
    int i=0,y=y0,x=x0;
    while (y>=0 && y<N && x>=0 && x<N && s[y][x]==c) {
      i++;
      y+=dy[d];
      x+=dx[d];
    }
    res >?= i;	   
  }
  return res;
}

void solve () {
  cin>>N>>K;

  s=VS(N);
  REP(i,N) {
    cin>>s[i];
    int j=N;
    REPD(k,N) if (s[i][k]!='.') s[i][--j]=s[i][k];
    while(j) s[i][--j]='.';
  }

  int maxb = go('B');
  int maxr = go('R');

  if (maxb>=K && maxr>=K)
    printf ("Both");
  else if (maxb>=K)
    printf ("Blue");
  else if (maxr>=K)
    printf ("Red");
  else
    printf ("Neither");
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
