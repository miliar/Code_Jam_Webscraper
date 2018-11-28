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


char buf[150];
int N;

bool probuj(int pos, LL num) {
  if (!buf[pos]) {
      LL p = sqrt(num);
      if (p*p==num) {
/*        bool byl = false;
        FORD(x, 60, 0) {
          if (p&(1LL<<x))
            byl = 1;
          if (byl)
            printf("%d", (p&(1LL<<x)) ? 1: 0);
        }
        printf("\n");*/
        printf("%s\n", buf);
        return true;
      }
      return false;
  }
  if (buf[pos]=='?') {
    buf[pos] = '0';
    if (probuj(pos+1, num*2)) { buf[pos] = '?'; return true; }
    buf[pos] = '1';
    if (probuj(pos+1, num*2+1)) { buf[pos] = '?'; return true; }
    buf[pos] = '?';
    return false;
  }
  if (buf[pos]=='1')
    return probuj(pos+1, num*2+1);
  return probuj(pos+1, num*2);
    
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%s", buf);
        N = strlen(buf);
        printf("Case #%d: ", (tt+1));
        probuj(0, 0);
    }
}


