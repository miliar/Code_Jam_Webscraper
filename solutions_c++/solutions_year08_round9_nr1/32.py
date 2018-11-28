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

const int MAX = 10000;

void solve () {
  int N;
  cin>>N;

  VI a(N),b(N),c(N);
  REP(i,N) cin>>a[i]>>b[i]>>c[i];

  int res=0;
  
  FOR(A,0,MAX+1) {
    vector<int> add(MAX-A+2,0);
    
    REP(i,N) if (a[i]<=A) {
      int fr=b[i];
      int to=MAX-A-c[i];
      //      printf ("%i - %i\n",fr,to);
      
      if (to>=fr) {
	add[fr]++;
	add[to+1]--;
      }
    }
    
    int cnt=0;
    REP(i,add.SZ) res = max(res, cnt += add[i]);
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
