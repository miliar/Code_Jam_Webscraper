#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int INF = 1<<30;                
const double EPS = 1e-9;
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

#define ALL(a) a.begin(),a.end()
#define PB push_back
#define MP make_pair
#define SZ(a) (int)a.size()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FOR(i,a,n) for(int i=(a);i<(n);++i)
#define FORD(i,a,n) for(int i=(a);i>=(n);--i)
#define REP(i,n) FOR(i,0,n) 


/// CODE HERE

const int N = 6025;
const int S = 3005;


int X[N][N];
int sx[N];
int Y[N][N];
int sy[N];
int table[N][N];

inline void add(int x, int y, int dx, int dy) {
  if (dx == 1) {
    X[x][sx[x]++] = y;
    //X[x].PB(y);
  } else if (dx == -1) {
    X[x-1][sx[x-1]++] = y;
    //X[x-1].PB(y);
  } else if (dy == 1) {
    Y[y][sy[y]++] = x;
    //Y[y].PB(x);
  } else if (dy == -1) {
    Y[y-1][sy[y-1]++] = x;
    //Y[y-1].PB(x);
  }
}

inline void right(int& dx, int& dy) {
  if (dx == 1) {
    dx = 0, dy = -1;
  } else if (dx == -1) {
    dx = 0, dy = 1;
  } else if (dy == -1) {
    dx = -1, dy = 0;
  } else if (dy == 1) {
    dx = 1, dy = 0;
  }
}
inline void left(int& dx, int& dy) {
   if (dx == 1) {
    dx = 0, dy = 1;
  } else if (dx == -1) {
    dx = 0, dy = -1;
  } else if (dy == -1) {
    dx = 1, dy = 0;
  } else if (dy == 1) {
    dx = -1, dy = 0;
  }
}

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(NT,1,T+1) {
    CLR(sx,0);
    CLR(sy,0);
    int xx = S, yy = S;
    int dx = -1, dy = 0;
    int L;
    scanf("%d", &L);
    getchar();
    REP(i,L) {
      string path;
      int cnt;
      cin >> path >> cnt;
      REP(it,cnt) {
        REP(j,SZ(path)) {
          if (path[j] == 'F') {
            add(xx, yy, dx, dy);
            xx += dx;
            yy += dy;
          } else if (path[j] == 'R') {
            right(dx, dy);
          } else {
            left(dx, dy);
          }
        }
      }
    }
    REP(i,N) {
      sort(X[i],X[i]+sx[i]);
      sort(Y[i],Y[i]+sy[i]);
    }
    CLR(table, 0);

    REP(i,N) {
      int m = sx[i];
      for (int j = 1; j < m; j+= 2) {
        if (j+1 >= m) continue;
        for (int k = X[i][j]; k < X[i][j+1]; ++k)
          table[i][k] = 1;
      }
    }
    REP(i,N) {
      int m = sy[i];
      for (int j = 1; j < m; j+=2) {
        if (j+1 >= m) continue;
        for (int k = Y[i][j]; k < Y[i][j+1]; ++k)
          table[k][i] = 1;
      }
    }
    int ans = 0;
    REP(i,N) REP(j,N)
      if (table[i][j]) ++ans;



    
    printf("Case #%d: %d\n", NT, ans);
  }


  return 0;
}