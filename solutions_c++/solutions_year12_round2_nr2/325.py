#include <cstdio>
#include <iostream>

using namespace std;

typedef long double ld;
typedef long long ll;

const int _x[4] = {1, 0, -1, 0};
const int _y[4] = {0, 1, 0, -1};
const int maxn = 100 + 5;
const int inf = 1 << 30;

struct item
{
  int x, y;
  item(): x(0), y(0) {}
  item(int x, int y): x(x), y(y) {}
};

int B[maxn][maxn], T[maxn][maxn];
ll D[maxn][maxn];
bool used[maxn][maxn];

const int maxq = 100 * maxn * maxn;
item Q[maxq];

void solve(int test_id)
{
  cout << "Case #" << test_id << ": ";
  
  int h, n, m;
  cin >> h >> n >> m;
  
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> T[i][j];
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> B[i][j];
    }
  }
  
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      //for (int l = 0; l <= h + n + m + 10; ++l) {
        D[i][j] = inf;
        used[i][j] = 0;
    
    }
  }
  
  D[0][0] = 0;
  used[0][0] = 1;
  int l = 0, r = 0;
  Q[l] = item(0, 0);
  
  while (l != r + 1) {
    //cerr << l << endl;
    int x = Q[l].x, y = Q[l].y;

    ++l;
    
    if (l == maxq) {
      l = 0;
    }
    
    used[x][y] = 0;
    for (int i = 0; i < 4; ++i) {
      int sx = x + _x[i];
      int sy = y + _y[i];
     
      if (sx < 0 || sx >= n || sy < 0 || sy >= m) {
        continue;
      }
      int ch = max(h - D[x][y], 0LL);
      int sb = max(B[sx][sy], ch);
      if (T[sx][sy] - B[x][y] >= 50 && T[x][y] - B[sx][sy] >= 50 && T[sx][sy] - B[sx][sy] >= 50) {
        int cost;
        bool good = D[x][y] == 0;
        int t = min(T[x][y], T[sx][sy]);
        if (t - sb >= 50) {
          cost = (ch - B[x][y] >= 20) ? 10 : 100;
        }
        else {
          good = 0;
          cost = 50 - (t - sb);
          int ch = max(h - (50 - (t - sb)), 0);

          cost += (ch - B[x][y] >= 20) ? 10 : 100;
        }
        
        /*if (cost <= 0) {
          cerr << "%) " << x << " " << y << " | " << sx << " " << sy << endl;
        }*/
        if (good) {
          cost = 0;
        }
        
        if (D[sx][sy] > D[x][y] + cost) {
          D[sx][sy] = D[x][y] + cost;
          if (!used[sx][sy]) {
            ++r;
            if (r == maxq) {
              r = 0;
            }
            Q[r] = item(sx, sy);
            used[sx][sy] = 1;
          }
        }
      }
    }
  }
  
  ld res = (ld)D[n - 1][m - 1] / 10;
 
  cout << res << '\n';
}

int main()
{
  freopen("B.in", "r", stdin);
  
  ios::sync_with_stdio(0);
  cout.setf(ios::fixed);
  cout.precision(7);
  
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    solve(i);
  }
  
  return 0;
}