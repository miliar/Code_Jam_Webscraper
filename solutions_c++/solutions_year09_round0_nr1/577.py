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

int main () {

  int L,D,N;
  cin>>L>>D>>N;

  VS d(D);
  
  REP(i,D) cin>>d[i];

  REP(i,N) {

    string s;
    cin>>s;

    VVI pos(L,VI(26,0));
    int idx=0;
    
    REP(j,s.SZ) {
      if (isalpha(s[j]))
	pos[idx][s[j]-'a']=1;
      else {
	j++;
	while (s[j]!=')') pos[idx][s[j++]-'a']=1;
      }

      idx++;
    }
    
    int res=0;
    
    REP(j,D) {
      int ok=1;
      REP(k,L) ok &= pos[k][d[j][k]-'a'];
      res+=ok;
    }

    printf ("Case #%i: %i\n",i+1,res);
  }
  
  return 0;
}
