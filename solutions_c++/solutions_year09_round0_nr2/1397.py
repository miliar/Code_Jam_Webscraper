#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<fstream>
#include<complex>
#include<cassert>
#include<climits>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

int H,W;
int altitude[100][100];
int flow[100][100];
int mapping[100][100];
//S,E,W,N
char dir[] = "NWES.";
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};

bool ok(int i, int j){
  return 0 <= i && i < H && 0 <= j && j < W;
}

int where_to_flow(int i, int j){
  int alt = altitude[i][j];
  int ret = 4;
  REP(k,4){
    int ni = i + di[k];
    int nj = j + dj[k];
    if(ok(ni, nj) && alt > altitude[ni][nj]){
      alt = altitude[ni][nj];
      ret = k;
    }
  }
  return ret;
}

char getCell(int i, int j){
  return 'a' + mapping[i][j] - 1;
}

struct UnionFind {
  vector<int> data;
  UnionFind(int size) : data(size, -1) { }
  bool unionSet(int x, int y) {
    x = root(x); y = root(y);
    if (x != y) {
      if (data[y] < data[x]) swap(x, y);
      data[x] += data[y]; data[y] = x;
    }
    return x != y;
  }
  bool findSet(int x, int y) {
    return root(x) == root(y);
  }
  int root(int x) {
    return data[x] < 0 ? x : data[x] = root(data[x]);
  }
  int size(int x) {
    return -data[root(x)];
  }
};


int main()
{
  int T;
  cin >> T;
  REP(turn,T){
    cin >> H >> W;
    REP(i,H)
      REP(j,W) cin >> altitude[i][j];
    
    UnionFind uf(H*W);
    REP(i,H){
      REP(j, W){
        int f = where_to_flow(i,j);
        if(f != 4){
          int ni = i + di[f];
          int nj = j + dj[f];
          uf.unionSet(i*W + j, ni*W + nj);
        }
      }
    }

    memset(mapping, 0, sizeof(mapping));
    int alph = 0, colored = 0;
    REP(i, H) REP(j, W){
      if(mapping[i][j]) continue;
      ++alph;
      REP(k,H) REP(l,W)
        if(uf.findSet(i*W + j, k*W + l))
          mapping[k][l] = alph;       
    }
    
    printf("Case #%d:\n", turn+1);
    REP(i,H) REP(j, W)
      cout << getCell(i,j) << ((j != W-1) ? ' ' : '\n');
  }
  return 0;
}

