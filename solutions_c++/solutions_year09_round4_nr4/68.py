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

#define TEST_NAME "D-small-attempt1"

#define SQR(x) ((x)*(x))

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int n,test;
	
     for(cin>>n,test=1;test<=n;++test) {
          int n;
          cin>>n;
          vector<double> x(n),y(n),r(n);
          REP(i,n)cin>>x[i]>>y[i]>>r[i];
          double ans=1e100;
          
          if(n<=2) {
               ans=0;
               REP(i,n)ans=max(ans,r[i]);
          }
          else {
               REP(i,3)REP(j,i) {
                    ans=min(ans,max((sqrt(SQR(x[i]-x[j])+SQR(y[i]-y[j]))+r[i]+r[j])/2.0,r[0+1+2-i-j]));                   
               }
          }
          printf("Case #%d: %.6lf\n",test,ans);         
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
