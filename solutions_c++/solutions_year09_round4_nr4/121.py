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

struct point { double x,y; };

point operator + (point a, point b) { return (point){a.x+b.x , a.y+b.y}; }
point operator - (point a, point b) { return (point){a.x-b.x , a.y-b.y}; }
point operator * (double a, point b) { return (point){a*b.x , a*b.y}; }
double operator * (point a, point b) { return a.x*b.x + a.y*b.y; }

void solve () {

  int N;
  cin>>N;
  vector<point> x(N);
  vector<double> r(N);

  REP(i,N) {
    int X,Y;
    cin>>X>>Y>>r[i];
    x[i] = (point){X,Y};
  }

  vector<point> pos;

  REP(i,N) pos.PB(x[i]);

  REP(i,N) REP(j,i) {
    double d = sqrt((x[j]-x[i])*(x[j]-x[i]));
    pos.PB(x[i] + (d+r[j]-r[i])/2/d * (x[j]-x[i]));
  }

  double res = 1e100;
  
  REP(i,pos.SZ) REP(j,i+1) {
    double lo=0,hi=1e10;
    REP(times,100) {
      double R = (lo+hi)/2;
      bool ok=1;
      REP(k,N) {
	bool ok1 = sqrt((x[k]-pos[i])*(x[k]-pos[i])) < R-r[k];
	bool ok2 = sqrt((x[k]-pos[j])*(x[k]-pos[j])) < R-r[k];
	if (!ok1 && !ok2) ok=0;
      }
      if (ok) hi=R; else lo=R;
    }

    res <?= lo;
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
