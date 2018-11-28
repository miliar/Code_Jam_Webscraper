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
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define REP(v, hi) for (int v=0; v<(hi); v++)
#define REPD(v, hi) for (int v=((hi)-1); v>=0; v--)
#define FOR(v, lo, hi) for (int v=(lo); v<(hi); v++)
#define FORD(v, lo, hi) for (int v=((hi)-1); v>=(lo); v--)
 
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector <string> VS;
 
int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {

    int K,N;
    cin>>K;
    string s;
    cin>>s;
    N=s.SZ;
        
    VI p(K);
    REP(i,K) p[i]=i;

    int res = INT_MAX;
    
    do {
      int tmp=0;
      char last = '?';
      
      REP(i,N/K) {
	string t = s.substr(i*K,K);
	REP(j,K) {
	  if (t[p[j]] != last) tmp++;
	  last = t[p[j]];
	}
      }

      res <?= tmp;
    }
    while (next_permutation(p.begin(),p.end()));
	   
    printf ("Case #%i: %i\n",run, res);
  }

  return 0;
}
