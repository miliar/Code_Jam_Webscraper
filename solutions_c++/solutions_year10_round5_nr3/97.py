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

#define TEST_NAME "C-small-attempt0"

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int n;
          map<int,int> cnt;
          priority_queue<PII> pq;
          int v,p;
          cin>>n;
          REP(i,n) {
               cin>>p>>v;
               cnt[p]=v;
               if(v>1)pq.push(PII(v,p));
          }
          int res=0,c;
          while(!pq.empty()) {
               v=pq.top().X;
               p=pq.top().Y;
               pq.pop();
               if(v<=1)break;
               if(cnt[p]!=v)continue;
               c=v/2;
               cnt[p]=v%2;
               res+=c;
               cnt[p-1]+=c;if(cnt[p-1]>1)pq.push(PII(cnt[p-1],p-1));
               cnt[p+1]+=c;if(cnt[p+1]>1)pq.push(PII(cnt[p+1],p+1));
          }
          cout<<"Case #"<<test<<": "<<res<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
