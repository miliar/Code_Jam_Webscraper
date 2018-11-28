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
#define V second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "B-large"

#define TIME(i) ((b-chick[i].X+chick[i].V-1)/chick[i].V)

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int n,k,b,t;
          cin>>n>>k>>b>>t;
          VPII chick(n);
          VI arrive(n+1);
          REP(i,n)cin>>chick[i].X;
          REP(i,n)cin>>chick[i].V;
          int res=0;
          arrive[n]=-INF;

          REP(it,k) {
               int next;
               for(next=n-1-it;next>=0&&TIME(next)>t;--next);
               if(next<0) {
                    res=-1;
                    break;
               }
               while(next<n-1-it) {
                    swap(chick[next],chick[next+1]);
                    ++next;++res;
               }
               arrive[next]=max(arrive[next+1],TIME(next));
               while(arrive[next]>t) {
                    swap(chick[next],chick[next+1]);
                    arrive[next+1]=max(arrive[next+2],TIME(next+1));
                    arrive[next]=max(arrive[next+1],TIME(next));
                    ++next;++res;
               }
          }

          cout<<"Case #"<<test<<": ";
          if(res>=0)cout<<res<<endl;
          else cout<<"IMPOSSIBLE"<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
