#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef unsigned long long ull;

int mp[105][105];
int mpg[105][105];

#define INF 20000

int iter(int h, int w, int k) {
  if (mpg[h][w] >= 0) return mpg[h][w];
  int buf  = mp[h][w];
  int fh = -1; int fw = -1;
  if (buf > mp[h-1][w  ]) { buf = mp[h-1][w  ]; fh = h-1; fw = w  ; }
  if (buf > mp[h  ][w-1]) { buf = mp[h  ][w-1]; fh = h  ; fw = w-1; }
  if (buf > mp[h  ][w+1]) { buf = mp[h  ][w+1]; fh = h  ; fw = w+1; }
  if (buf > mp[h+1][w  ]) { buf = mp[h+1][w  ]; fh = h+1; fw = w  ; }
  mpg[h][w] = (fh < 0) ? k : iter(fh, fw, k);
  return mpg[h][w];
}

void solve() {
  int H, W;
  cin >> H >> W;
  REP(h,H) REP(w,W) cin >> mp[h+1][w+1];
  REP(h,H+2) mp[h][0]   = INF;
  REP(h,H+2) mp[h][W+1] = INF;
  REP(w,W+2) mp[0][w]   = INF;
  REP(w,W+2) mp[H+1][w] = INF;
  REP(h,H+2) REP(w,W+2) mpg[h][w] = -1;

  int k = 0;
  REP(h,H) REP(w,W) {
    iter(h+1,w+1,k);
    k++;
  }

  map<int,char> m;
  char c = 'a';
  REP(h,H) {
    REP(w,W) {
      int g = mpg[h+1][w+1];
      if (m.find(g) == m.end()) m[g] = c++;
      printf("%c%s", m[g], w == W-1 ? "" : " " );
    }
    printf("\n");
  }
}

int main () {
  int T;
  cin >> T;
  REP(i,T) {
    printf("Case #%d:\n", i+1);
    solve();
  }
}

