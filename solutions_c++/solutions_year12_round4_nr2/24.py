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

int N, xs, ys;
pii roz[1000];
int px[1000], py[1000];
int dolx[1002], doly[1002];
int dolx2[1002], doly2[1002];
int iled;


inline bool czy_sie_miesci(int x, int y, int r) {
  return (x==0 || x+r<=xs) && (y==0 || y+r<=ys);
}


int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d", &N, &xs, &ys);
        REP(x, N) {
            scanf("%d", &roz[x].first);
            roz[x].second = x;
        }
        iled = 1;
        dolx[0] = doly[0] = 0;
        
        REP(z, N) {
        
          REP(d, iled)
            if (czy_sie_miesci(dolx[d], doly[d], roz[z].first)) {
              int r = roz[z].first;
              px[roz[z].second] = dolx[d] ? dolx[d]+r : 0;
              py[roz[z].second] = doly[d] ? doly[d]+r : 0;
              int mx = px[roz[z].second]+r;
              int my = py[roz[z].second]+r;
              int nd = 0;
              FORD(d2, iled-1, d) {
                if (doly[d2]>my) {
                  dolx2[nd] = dolx[d2];
                  doly2[nd] = doly[d2];
                  ++nd;
                }
                else {
                  dolx2[nd] = dolx[d2];
                  doly2[nd] = my;
                  ++nd;
                  break;
                }
              }
              FOR(d2, 0, d)
                if (dolx[d2]<=mx) {
                  dolx[d2] = mx;
                  iled = d2+1;
                  break;
                }
              while (nd) {
                --nd;
                dolx[iled] = dolx2[nd];
                doly[iled] = doly2[nd];
                ++iled;
              }
              goto dalej;
            }
          fprintf(stderr, "ZLE!!!!!\n");
          dalej:;
        }

        printf("Case #%d:", (tt+1));
        REP(a, N)
            printf(" %d %d", px[a], py[a]);
        printf("\n");
    }
}


