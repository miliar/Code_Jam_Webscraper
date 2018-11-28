#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int N;
int wid[2000];
int poz[2000];

void rek(int pocz, int kon, int lev) { // kon ma juz przydzielony, pocz-1 poka
  if (pocz==kon) return;
  int px=pocz;
  FOR(x, pocz, kon-1) {
    if (wid[x]>kon) throw 0;
    if (wid[x]==kon) {
      poz[x] = poz[kon]-1-lev*(kon-x);
      rek(px, x, lev+1);
      px = x+1;
    }
  }
}


int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d", &N);
        REP(x, N-1) {
            scanf("%d", &wid[x]);
            --wid[x];
        }
        printf("Case #%d:", (tt+1));
        try {
          poz[N-1] = 0;
          rek(0, N-1, 0);
          int m = 0;
          REP(a, N)
            m = min(m, poz[a]);
          m = -m;
          REP(a, N)
            printf(" %d", m+poz[a]);
        }
        catch (...) {
          printf(" Impossible");
        }
        printf("\n");
    }
}


