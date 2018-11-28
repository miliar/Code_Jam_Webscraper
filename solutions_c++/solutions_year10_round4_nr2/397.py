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
#define INFLL 1000000000000000000LL
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "B-large"

const int maxP=10;

int M[1<<maxP];
int price[maxP][1<<maxP-1];

ll cost[maxP][maxP][1<<maxP-1];

ll calc(int p,int skipped,int beg) {
     if(p<0) {
          if(M[beg]>=skipped)return 0;
          else return INFLL;
     }
     ll &res=cost[p][skipped][beg];
     if(res>=0)return res;
     
     res=INFLL;
     res=min(res,price[p][beg]+calc(p-1,skipped,2*beg)+calc(p-1,skipped,2*beg+1));
     res=min(res,calc(p-1,skipped+1,2*beg)+calc(p-1,skipped+1,2*beg+1));
//      cerr<<"calc("<<p+1<<", "<<skipped<<", "<<beg<<")="<<res<<endl;
     return res;
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int p;
          cin>>p;
          REP(i,1<<p)cin>>M[i];
          
          REP(k,p)REP(i,(1<<(p-k-1)))cin>>price[k][i];
         
          memset(cost,-1,sizeof cost);
          cout<<"Case #"<<test<<": "<<calc(p-1,0,0)<<endl;
          
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
