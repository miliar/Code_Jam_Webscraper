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

int karty[1005];
int N;

int otw[1005], ile_otw;
int best;

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d", &N);
        REP(a, N)
            scanf("%d", &karty[a]);
        sort(karty, karty+N);
        best = N ? INF : 0;
        ile_otw = 0;
        int pop = -1000;
        int nr = 0;
        for (;;) {
            if (nr==N || pop<karty[nr]-1) {
                REP(a, ile_otw)
                  best = min(best, pop-otw[a]+1);
                ile_otw = 0;
                pop = karty[nr]-1;
            }
            if (nr==N)
              break;
            int ile = 0;
            while (nr<N && karty[nr]==pop+1)
              ++ile, ++nr;
            if (ile<ile_otw) {
              REP(a, ile_otw-ile)
                best = min(best, pop-otw[a]+1);
              REP(a, ile)
                otw[a] = otw[a+ile_otw-ile];
              ile_otw = ile;
            }
            ++pop;
            while (ile_otw<ile)
              otw[ile_otw++] = pop;
        }
        printf("Case #%d: %d\n", (tt+1), best);
    }
}


