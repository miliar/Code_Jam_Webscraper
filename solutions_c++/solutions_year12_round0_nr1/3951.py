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
#define INIT(a,v) __typeof(v) a = (v)
#define FOREACH(a,v) for(INIT(a, (v).begin()); a!=(v).end(); ++a)

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

char i[] = "abcdefghijklmnopqrtsuvwxyz";
char o[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    char buf[200];
    fgets(buf, 200, stdin);
    for (char *x = buf; *x; ++x) {
      if (*x>='a' && *x<='z')
        *x = o[*x-'a'];
    }
    printf("Case #%d: %s", tt+1, buf);
  }
}
