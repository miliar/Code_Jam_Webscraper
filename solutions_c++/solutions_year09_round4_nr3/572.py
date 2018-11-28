#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
const decimal EPS = 1e-8;

int nCases;
int nStocks, nPoints;

int a[100][100];
bool b[100][100];

bool touches(int x, int y){
  int *X = a[x];
  int *Y = a[y];
  REP(i, nPoints-1){
    if(X[i] >= Y[i] && X[i+1] <= Y[i+1] || X[i] <= Y[i] && X[i+1] >= Y[i+1]) return true;
  }
  return false;
}

int color[16];
int best;

int solve(int cur, int used){
  if(used >= best) return 100000;
  if(cur == nStocks){
    best = used;
    return used;
  }
  bool forbidden[16] = {0};
  REP(i, nStocks) if(b[cur][i] && color[i] >= 0){
    forbidden[color[i]] = true;
  }
  int ret = 10000000;
  REP(i, used+1){
    if(forbidden[i]) continue;
    color[cur] = i;
    ret = min(ret, solve(cur+1, i < used ? used : used+1));
  }
  color[cur] = -1;
  return ret;
}

int main(){
  scanf("%d ", &nCases);
  REP(ic, nCases){
    cin >> nStocks >> nPoints;
    REP(i, nStocks) REP(j, nPoints){
      int x;
      cin >> x;
      a[i][j] = x;
    }
    REP(i, nStocks) REP(j, nStocks){
      b[i][j] = b[j][i] = touches(i, j);
    }
    best = 100000;
    memset(color, -1, sizeof(color));
    int ret = solve(0, 0);

    cout << "Case #" << ic+1 << ": " << ret << endl;
  }

  return 0;
}

