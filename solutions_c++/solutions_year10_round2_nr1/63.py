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

struct PathTree {
     map<string,PathTree> subdirs;
     int insert(string path) {
          if(path=="")return 0;
          int e=path.find('/',1);
          if(e==string::npos)e=SZ(path);
          string name=path.substr(1,e-1);
          int res=0;
          if(subdirs.find(name)==subdirs.end()) {
               subdirs.insert(make_pair(name,PathTree()));
               ++res;
          }
          res+=subdirs[name].insert(path.substr(e));

          return res;
     }
};

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int tc,test;
	
     for(cin>>tc,test=1;test<=tc;++test) {
          int n,m;
          string path;
          cin>>n>>m;
          PathTree tr;
          REP(i,n) {
               cin>>path;
               tr.insert(path);
          }
          int res=0;
          REP(i,m) {
               cin>>path;
               res+=tr.insert(path);
          }
          cout<<"Case #"<<test<<": "<<res<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
