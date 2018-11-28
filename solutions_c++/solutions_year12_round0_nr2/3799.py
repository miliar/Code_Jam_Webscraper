#include <string>
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

#define INF 1000000000

#define PB push_back
#define MP make_pair

typedef long long LL;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
 
template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

int N,S,P, cur;

int main() {
  int TT;
  scanf("%d", &TT);
  REP(tt, TT) {
    int ile_ok = 0;
    scanf("%d%d%d", &N, &S, &P);
    REP(a, N) {
      scanf("%d", &cur);
      if ((cur+2)/3>=P)
        ++ile_ok;
//	0 -> N/3
//      1 -> N/3+1
//      2 -> N/3+1
      else {
        if (cur<=1 || !S) continue;
        if ((cur+4)/3>=P)
          ++ile_ok, --S;
//        0 -> -1,0,1 -> N/3+1
//        1 -> -1,1,1 -> N/3+1
//        2 -> 0,0,2 -> N/3+2
      }
    }
    printf("Case #%d: %d\n", tt+1, ile_ok);
  }
}
