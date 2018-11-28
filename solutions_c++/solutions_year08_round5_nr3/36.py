#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cassert>
using namespace std;


#define VV vector
#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND = 0;

#define DB(x) { if (COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

#define SZ (85*85 + 10)
VV <int> Q[SZ];

int A[SZ];
int skoj[SZ];
int VIS[SZ];

int ST, ED;


void add(int p1, int p2, int x, int y) {
  Q[p1].PB(p2);
}

bool go(int i) {
   if (VIS[i]) return false;
   VIS[i] = true;
   FORE (it, Q[i]) if (skoj[*it] == -1 || go(skoj[*it])) {
        skoj[*it] = i;
        skoj[i] = *it;
        return true;
   }  
   return false;
}

int flow() {
  int ret = 0;
  while (true) {
    CLR(VIS, 0);
    bool ok = false;
    REP (i, SZ) if (!VIS[i] && skoj[i] == -1) {
      if (go(i)) { ok = true; ret++; }
    }
    if (!ok) break;
  }
  return ret;

}
    

int main(int argc, char **argv) {
  COND = argc >= 2 && argv[1][0] == 'q';
  int T; cin >> T;
  FOR (my, 1, T) {
    REP (i, SZ) Q[i].clear();
    int N, M; cin >> N >> M;
  CLR(skoj, -1);
    int work = 0;
    int c1 = 0, c2 = 0; 
    REP (i, N) REP (j, M) { char x;
      cin >> x;
      A[i*81 + j] = x;
      if (x == '.') work++;
   
      if (x == 'x') {
        if (j % 2 == 0) c1++;
        else c2++;
      }
    }
    DB(c1<<" "<<c2);
    ST = 81 * 80;
    ED = ST + 1;

    REP (i, N) REP (j, M) if (j % 2 == 0) {
      FOR (dx, -1, 1)  FOR (dy, -1, 1) if (dy) {
        int ni = i + dx, nj = j + dy;
        if (ni >= 0 && ni < N && nj >= 0 && nj < M && A[81*i + j] == '.'
           && A[81*ni+nj] == '.') {
          int p1 = i * 81 + j;
          int p2 = ni * 81 + nj;
          add(p1, p2, 1, 0);
     //     DB(p1<<" "<<p2);

        }
      }
    }
   int ret = flow();
    REP (i, N) REP(j, M) if (j % 2 == 0) {
      DB(i<<" "<<j<<" "<<skoj[i*81+j]);
   } 
    DB(work<<" "<<ret);
    printf("Case #%d: %d\n", my, work - ret);
  }

  return 0;
}
