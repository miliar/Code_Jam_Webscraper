#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <ext/functional>
#include <ext/rope>
#include <ext/rb_tree>
#include <ext/iterator>
#include <ext/slist>

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define REP(i, n) for(int i=0; i<n; ++i)
#define REPD(i, n) for(int i=(n)-1; i>=0; --i)
#define FOR(i, b, e) for(typeof(e) i=b; i!=e; ++i)

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

const int INF=10000000;

int R,C;
VVI height, cmap;

int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};

int dfs(int r, int c, int col) {
  if(cmap[r][c]!=-1) return cmap[r][c];
  int mini=INF;
  REP(i, 4) {
    int nr=r+dr[i], nc=c+dc[i];
    if(nr<0 || nr>=R || nc<0 || nc>=C) continue;
    if(height[nr][nc]>=height[r][c]) continue;
    mini=min(mini, height[nr][nc]);
  }
  REP(i, 4) {
    int nr=r+dr[i], nc=c+dc[i];
    if(nr<0 || nr>=R || nc<0 || nc>=C) continue;
    if(height[nr][nc]>=height[r][c]) continue;
    if(height[nr][nc]>mini) continue;
    return (cmap[r][c]=dfs(nr, nc, col));
  }
  cmap[r][c]=col;
  return col;
}

void go() {
  cin >> R >> C;
  height=VVI(R, VI(C));
  cmap=VVI(R, VI(C,-1));
  REP(i, R) REP(j, C) cin >> height[i][j];
  int col=0;
  REP(i, R) REP(j, C) if (cmap[i][j]==-1) {
    int used=dfs(i,j,col);
    if(used==col) col++;
  }
  REP(i, R) {REP(j, C) {if (j) cout << " "; cout << (char)('a'+cmap[i][j]);} cout<<"\n";}
}

int main() {
  int nruns;
  cin >> nruns;
  REP(i, nruns) {
    cout << "Case #" << (i+1) <<":\n";
    go();
  }
  return 0;
}
