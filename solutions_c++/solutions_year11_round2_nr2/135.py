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
typedef long double cfloat;

#define TEST_NAME "B-large"

int d;
VPII shop;

bool good(cfloat t) {
     cfloat nxt=-1e100;
     REP(i,SZ(shop)) {
          cfloat b = shop[i].X - t, e= shop[i].X + t;
          REP(k,shop[i].Y)  {
               if(nxt < b)nxt = b;
               if(nxt > e)return false;
               nxt += d;
          }
     }
     return true;
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int c;
        cerr<<"Test #"<<test<<"..."<<endl;
          cin>>c>>d;
          shop.resize(c);
          REP(i,c)cin>>shop[i].X>>shop[i].Y;
          cfloat mint=0.0, maxt=1e15, t;
          while(fabsl(maxt-mint)>=1e-7) {
               t=(maxt+mint)/2.0;
               if(good(t))maxt=t;
               else mint=t;
          }
          cout<<"Case #"<<test<<": ";
          cout.setf(ios::fixed);
          cout.precision(10);
          cout<<(mint+maxt)/2.0<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
