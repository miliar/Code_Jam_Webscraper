#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;

int d,n,m,k;
set<string> S,s;
string q,f;

int main() {

scanf("%d%d%d", &d, &n, &m);
while(n--) {
  cin >> q;
  S.insert(q);
}

FOR(zz,1,m) {
  s = S; k=0;

  cin >> q;
  while(SIZE(q)) {
    f.clear();

    if(q[0]=='(') {
      q.erase(0, 1);
      while(q[0]!=')') {
        f+=q[0];
        q.erase(0, 1);
      }
      q.erase(0, 1);
    } else {
      f = q[0];
      q.erase(0, 1);
    }

    FOREACH(it, s) 
    if(f.find((*it)[k]) == string::npos) s.erase(it);

    k++;
  }

  printf("Case #%d: %d\n", zz, SIZE(s));
}

return 0;
}
