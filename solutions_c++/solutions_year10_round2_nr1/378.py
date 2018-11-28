#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;

const int DBG = 0, INF = int(1e9);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

int main() {
  ios_base::sync_with_stdio(0);

  int T;

  scanf("%d", &T);

  REP(q,T) {

    int N, M;

    scanf("%d %d", &N, &M);

    set<string> S;

    REP(j,N) {
      char buf[150];

      scanf("%s", buf);

      string line = buf;
    
      line += '/';

      FOR(i,1,line.size() - 1)
        if (line[i] == '/')
          S.insert(line.substr(0,i));

    }

    int res = 0;

    REP(j,M) {
  
      char buf[150];

      scanf("%s", buf);

      string line = buf;

      line += '/';

      FOR(i,1,line.size() - 1)
        if (line[i] == '/') {

          if (! S.count(line.substr(0,i))) {
            ++res;
            S.insert(line.substr(0,i));
          }

        }

    } 

    printf("Case #%d: %d\n",q + 1, res);





  }

  return 0;
}
