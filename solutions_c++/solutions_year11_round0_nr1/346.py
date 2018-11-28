#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "A-large"

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int n;
          char chr;
          cin>>n;
          VPII seq(n);
          VI rpos[2];
          REP(i,n) {
               cin>>chr>>seq[i].Y;
               seq[i].X=(chr=='B'?0:1);
               rpos[seq[i].X].pb(seq[i].Y);
          }
          int ready[2]={0};
          int t=0;
          REP(k,2) {
               REVERSE(rpos[k]);
               if(!rpos[k].empty())ready[k]=abs(rpos[k].back() - 1);
          }
          REP(i,n) {
               int k = seq[i].X;
               t = max(t, ready[k]);
               ++t;
               ready[k] = t;
               rpos[k].pop_back();
               if(!rpos[k].empty())ready[k] += abs(rpos[k].back() - seq[i].Y);
          }
          printf("Case #%d: %d\n",test,max(ready[0],ready[1]));
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
