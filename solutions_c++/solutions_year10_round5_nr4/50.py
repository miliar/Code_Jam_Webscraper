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
#define INIT(a, b) __typeof(b) a = (b)
#define FOREACH(a, b) for(INIT(a, (b).begin()); a!=(b).end(); ++a)
 
#define PB push_back
#define MP make_pair
 
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;
 
#define INF 1000000000
 
template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

#define MOD 1000000007

int B;
LL N;
int cyfry[60];
int ilec;

int rozb0[71][71*71];
int rozz0[71][71*71];
int wyn[61][71][71];

int silnia(int k) {
  int w  = 1;
  FOR(x, 1, k)
    w = (w*(LL)x)%MOD;
  return w;
}

int noverk[71][71];

int main() {
    noverk[0][0] = 1;
    FOR(n, 1, 70)
      REP(k, n+1)
        noverk[n][k] = ((k>0 ? noverk[n-1][k-1] : 0)+(k<n ? noverk[n-1][k] : 0))%MOD;
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%Ld%d", &N, &B);
        ilec = 0;
        while (N) {
          cyfry[ilec++] = N%B;
          N /= B;
        }
        int m_roz = B*(B-1)/2;
        REP(a, 71) REP(b, 71*71)
          rozb0[a][b] = rozz0[a][b] = 0;
        rozb0[0][0] = 1;
        rozz0[1][0] = 1;
        FOR(a, 1, B-1)
          FORD(i, B-1, 0)
            FOR(s, 0, m_roz-a) {
              rozb0[i+1][s+a] = (rozb0[i+1][s+a]+rozb0[i][s])%MOD;
              rozz0[i+1][s+a] = (rozz0[i+1][s+a]+rozz0[i][s])%MOD;
            }
        REP(poz, ilec+1) REP(ile, B+1) REP(p,B)
          wyn[poz][ile][p] = 0;
        wyn[ilec][0][0] = 1;
        FORD(poz, ilec-1, 0)
          REP(pl, B) {
            int ma_byc_ = pl*B+cyfry[poz];
            REP(pp, min(B, ma_byc_+1)) {
              int ma_byc = ma_byc_-pp;
              REP(ile, B+1) REP(ilel, ile+1) {
                wyn[poz][ile][pp] = (wyn[poz][ile][pp]+wyn[poz+1][ilel][pl]*(LL)silnia(ilel)%MOD*noverk[ile][ilel]%MOD*rozb0[ile][ma_byc])%MOD;
                if (ilel>0)
                wyn[poz][ile][pp] = (wyn[poz][ile][pp]+wyn[poz+1][ilel][pl]*(LL)silnia(ilel)%MOD*noverk[ile-1][ilel-1]%MOD*rozz0[ile][ma_byc])%MOD;
              }
            }
          }
        int res = 0;
        REP(ile, B+1)
          res = (res+wyn[0][ile][0])%MOD;
        printf("Case #%d: %d\n", tt+1, res);
    }
}


