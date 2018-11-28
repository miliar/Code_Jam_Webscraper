#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;
#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FCC(i,a,b) for(int i=a,_b=b;i<=_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ROF(i,n) for(int i=n-1;i>=0;--i)
#define SZ(v) (signed(v.size()))
#define FOZ(i,v) FOR(i,SZ(v))
#define ALL(s) s.begin(),s.end()
#define LET(a,b) typeof(b) a=b
#define FOREACH(it,s) for(LET(it,s.begin());it!=s.end();++it)

typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define D(A) A

const int INF = 2000000000;
typedef long long ll;
typedef long double ld;
const ld FINF = 1e8;
const ld eps = 1e-9;

char m[500][500], r[500][500], c[500][500];

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum, ncases) {
    int R, C, D;
    scanf("%d %d %d\n",&R, &C, &D);
    
    FOR(i,R) {
      FOR(j,C) {
        scanf("%c", &m[i][j]);
        m[i][j] -= '0';
      }
      scanf("\n");
    }
    //FOR(i,R) { FOR(j,C) printf("%d ", m[i][j]); printf("\n"); }
    FOR(i,R) {
      int s = 0;
      FOR(j,C) {
        s += m[i][j];
        r[i][j] = s;
      }
    }
    FOR(j,C) {
      int s = 0;
      FOR(i,R) {
        s += m[i][j];
        c[i][j] = s;
      }
    }

    int ans = 0;
    //i+K-1 < R => i < R+1-K
    FCC(K, 3, min(R,C)) FOR(i,R+1-K) FOR(j,C+1-K) {
      //The KxK blade starting at (i,j)
      int us = 0;
      FCO(y, i, i+K/2) us += r[y][j+K-1] - (j ? r[y][j-1] : 0);
      us -= m[i][j]; us -= m[i][j+K-1];
      int ds = 0;
      FCC(y, i+K-1-K/2+1, i+K-1) ds += r[y][j+K-1] - (j ? r[y][j-1] : 0);
      ds -= m[i+K-1][j]; ds -= m[i+K-1][j+K-1];

      int ls = 0;
      FCO(x, j, j+K/2) ls += c[i+K-1][x] - (i ? c[i-1][x] : 0);
      ls -= m[i][j]; ls -= m[i+K-1][j];
      int rs = 0;
      FCC(x, j+K-1-K/2+1, j+K-1) rs += c[i+K-1][x] - (i ? c[i-1][x] : 0);
      rs -= m[i][j+K-1]; rs -= m[i+K-1][j+K-1];

      if(us==ds and ls==rs) ans=K;
    }
    if(ans >= 3) {
      printf("Case #%d: %d\n", casenum+1, ans);
    }
    else {
      printf("Case #%d: IMPOSSIBLE\n", casenum+1);
    }
  }
  return 0;
}
