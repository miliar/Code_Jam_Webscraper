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
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;


#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

vector<vector<int> > tab;
int cmp[17][17]; // a>b

int wyn[17][1<<16];

int N, K;

int main() {
    int TT;
    scanf("%d", &TT);
    REP(t, TT) {
        scanf("%d%d", &N, &K);
        tab.clear();
        REP(a, N) {
          vi fff;
          REP(b, K) {
            int z;
            scanf("%d", &z);
            fff.PB(z);
          }
          tab.PB(fff);
        }
        sort(tab.begin(), tab.end());
        REP(a, N)
          REP(b, N) {
            cmp[a][b] = 1;
            REP(x, K)
                if (!(tab[a][x]>tab[b][x]))
                    cmp[a][b] = 0;
          }
        REP(z, N+1)
          REP(x, 1<<16)
            wyn[z][x] = INF;
        wyn[0][0] = 0;
        REP(nr, N) {
          REP(gdzie, nr) // nr nad gdzie
            if (cmp[nr][gdzie])
              REP(x, 1<<N)
                if (x&(1<<gdzie)) {
                    int nx = (x & (~(1<<gdzie))) | (1<<nr);
                    wyn[nr+1][nx] = min(wyn[nr+1][nx], wyn[nr][x]);
                }
          // dodajemy nowy wykres
          REP(x, 1<<N) {
            int nx = x | (1<<nr);
            wyn[nr+1][nx] = min(wyn[nr+1][nx], wyn[nr][x]+1);
          }
        }
        int best = INF;
        REP(x, 1<<N)
          best = min(best, wyn[N][x]);
        printf("Case #%d: %d\n", t+1, best);
        fprintf(stderr, "Case #%d: %d\n", t+1, best);
    }
    
}


