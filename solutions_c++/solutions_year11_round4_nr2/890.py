#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>
#include <iomanip>
#include <assert.h>
#include <list>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef long long ll;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-9)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}

#define MAX 510

int n,m,d;
char matr[MAX][MAX];

struct point {
  double x,y;
  point(double x = 0, double y = 0): x(x), y(y) {}

  point operator +(point q){ return point(x + q.x, y + q.y); }
  point operator -(point q){ return point(x - q.x, y - q.y); }
  point operator *(double t){ return point(x * t, y * t); }
  point operator /(double t){ return point(x / t, y / t); }
  double operator *(point q){ return x * q.x + y * q.y; }
  double operator %(point q){ return x * q.y - y * q.x; }

  int cmp(point q) const {
    if (int t = ::cmp(x, q.x)) return t;
    return ::cmp(y, q.y);
  }
  bool operator ==(point q) const { return cmp(q) == 0; }
  bool operator !=(point q) const { return cmp(q) != 0; }
  bool operator < (point q) const { return cmp(q) < 0; }
};

point mat[MAX][MAX];
point mato[MAX][MAX];

point calc(int y0, int x0, int sz) {
  int y1 = y0 + sz-1;
  int x1 = x0 + sz-1;
  if (y1 >= n || x1 >= m) return point(-INF,-INF);
  //point res;
  // for (int i = y0; i <= y1; i++)
  //    for (int j = x0; j <= x1; j++)
  //      res = res + mato[i][j];
  point res = mat[y1][x1];
  if (x0 > 0) res = res - mat[y1][x0-1];
  if (y0 > 0) res = res - mat[y0-1][x1];
  if (y0 > 0 && x0 > 0) res =  res + mat[y0-1][x0-1];
  res = res - mato[y0][x0] - mato[y0][x1]-mato[y1][x1]-mato[y1][x0];
  return res;
}

int main() {
  int ncases;
  scanf("%d",&ncases);
  FOR(ccases,ncases) {
    printf("Case #%d: ",ccases+1);
    cin >> n >> m >> d;
    FOR(i,n) cin >> matr[i];
    int res = 0;
    point pzero(0,0);
    FOR(y,n) FOR(x,m) {
      //int y = 1, x = 1;
      int sz = 3;
      while (true) {
        point pc(x+(sz-1)/2.,y+(sz-1)/2.);
        FOR(i,n) {
          FOR(j,m) {
            mato[i][j] = (point(j,i)-pc)*(d+(int)(matr[i][j]-'0'));
            mat[i][j] = mato[i][j];
            if (i > 0) mat[i][j] = mat[i][j] + mat[i-1][j];
            if (j > 0) mat[i][j] = mat[i][j] +  mat[i][j-1];
            if (i > 0 && j > 0) mat[i][j] = mat[i][j] - mat[i-1][j-1];
          }
        }
        point r = calc(y,x,sz);
        if (r == point(-INF,-INF)) break;
        if (r == pzero && sz > res) res = sz;
        sz++;
      }
    }
    if (res == 0) cout << "IMPOSSIBLE" << endl;
    else  cout << res << endl;
  }
  return 0;
}
