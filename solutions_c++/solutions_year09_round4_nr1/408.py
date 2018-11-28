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

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int N;
int last[100];

int main() {
    int T;
    scanf("%d", &T);
    REP(t, T) {
        int ile = 0;
        scanf("%d", &N);
        REP(y, N) {
          char buf[100];
          scanf("%s", buf);
          last[y] = 0;
          REP(x, N)
            if (buf[x]=='1')
              last[y] = x;
        }
        REP(y, N) {
          int best;
          FOR(z, y, N-1)
            if (last[z]<=y) {
              best = z;
              break;
            }
          FORD(z, best-1, y) {
            ++ile;
            swap(last[z], last[z+1]);
          }
        }
        printf("Case #%d: %d\n", t+1, ile);
    }
    
}


