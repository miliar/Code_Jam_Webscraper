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

const int MAXA=1000001;
VI fr,to;

void solve () {
  int a1,a2,b1,b2;
  cin>>a1>>a2>>b1>>b2;
  
  LL res=0;

  REP(times,2) {
    FOR(a,a1,a2+1) {
      if (b2>to[a]) res += b2 - max(b1,to[a]+1) + 1;
    }
    
    swap(a1,b1);
    swap(a2,b2);
  }

  printf ("%lli",res);
}

int main () {

  fr=to=VI(MAXA,0);
  fr[1]=to[1]=1;
  fr[2]=2; to[2]=3;

  int i=2;
  FOR(j,3,MAXA) {
    while (to[i]<j) i++;
    fr[j]=i;
    to[j]=i+j-1;
  }
  
  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i: ",run);
    solve();
    printf ("\n");
  }

  return 0;
}
