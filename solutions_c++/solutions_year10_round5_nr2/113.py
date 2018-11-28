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

#define TEST_NAME "B-small-attempt2"

const int iterate=2000001;
ll cnt[iterate];

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          ll L;
          int n;
          int b[100];
          cin>>L>>n;
          REP(i,n)cin>>b[i];
          sort(b,b+n);
          ll res=-1;
          REP(i,iterate) {
               if(i==0)cnt[i]=0;
               else cnt[i]=INF;
               REP(k,n-1)
                    if(i>=b[k]&&cnt[i]>cnt[i-b[k]]+1)cnt[i]=cnt[i-b[k]]+1;
               if((L-i)%b[n-1]==0&&cnt[i]!=INF) {
                    if(res<0||res>(L-i)/b[n-1]+cnt[i])res=(L-i)/b[n-1]+cnt[i];
               }
          }
          cout<<"Case #"<<test<<": ";
          if(res==-1)cout<<"IMPOSSIBLE"<<endl;
          else cout<<res<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
