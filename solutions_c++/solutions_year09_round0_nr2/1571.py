// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int H, W;
int A[128][128];
int basins;
int B[128][128];

int dr[]={-1,0,0,1}, dc[]={0,-1,1,0};

void solve(int r, int c) {
  if (B[r][c] >= 0) return;
  int best = A[r][c];
  int where = -1;
  REP(d,4) {
    int nr=r+dr[d], nc=c+dc[d];
    if (A[nr][nc] >= best) continue;
    best = A[nr][nc];
    where = d;
  }
  if (where==-1) {
    ++basins;
    B[r][c] = basins;
  } else {
    int nr=r+dr[where], nc=c+dc[where];
    solve(nr,nc);
    B[r][c] = B[nr][nc];
  }
}

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    cin >> H >> W;
    FOR(h,0,H+1) FOR(w,0,W+1) A[h][w] = 12345;
    FOR(h,1,H) FOR(w,1,W) cin >> A[h][w];
    memset(B,-1,sizeof(B));
    FOR(h,1,H) FOR(w,1,W) solve(h,w);
    map<int,char> Z;
    FOR(i,1,basins) Z[i]=' ';
    cout << "Case #" << t << ":" << endl;
    char letter = 'a';
    FOR(h,1,H) {
      FOR(w,1,W) {
        if (Z[ B[h][w] ]==' ') {
          Z[ B[h][w] ] = letter;
          ++letter;
        }
        cout << (w==1 ? "" : " ") << Z[ B[h][w] ];
      }
      cout << endl;
    }
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
