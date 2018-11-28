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

bool match(const string &w,const string &d) {
     int i=0;
     REP(k,SZ(d)) {
          if(w[i]=='(') {
               for(i++;w[i]!=')'&&w[i]!=d[k];i++);
               if(w[i]==')')return false;
               while(w[i]!=')')++i;
          }
          else if(w[i]!=d[k])return false;
          i++;
     } 
     return true;
}

int main() {
     int n,test;
     int L,d;
     vector<string> dict;
     string word;
     int res;
     cin>>L>>d>>n;
     dict.resize(d);
     REP(i,d)cin>>dict[i];
     for(test=1;test<=n;++test) {
          cin>>word;
          res=0;
          REP(i,d)if(match(word,dict[i]))++res;
          printf("Case #%d: %d\n",test,res);
     }
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
