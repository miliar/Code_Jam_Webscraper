#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
using namespace std;

#define X first
#define Y second
#define PB push_back

typedef long long ll;
typedef long long ent;
typedef pair<int, int> P;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;

typedef queue<int> Q;
typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

const int INF = 1000000000;

int F, C;
ll D;

char mapa[1000][1000];

ll mass[1000][1000];

ll dx[1000][1000];
ll dy[1000][1000];
ll dm[1000][1000];

ll getdx(int i, int j) {
  if (i < 0 or j < 0) return 0;
  return dx[i][j];
}

ll getdy(int i, int j) {
  if (i < 0 or j < 0) return 0;
  return dy[i][j];
}


ll getdm(int i, int j) {
  if (i < 0 or j < 0) return 0;
  return dm[i][j];
}

void suma(int i, int j, int k, ll& sx, ll& sy, ll& sm) {
  sx = getdx(i + k - 1, j + k - 1);
  sx -= getdx(i - 1, j + k - 1);
  sx -= getdx(i + k - 1, j - 1);
  sx += getdx(i - 1, j - 1);
  sx -= 2*i*mass[i][j];
  sx -= 2*i*mass[i][j + k - 1];
  sx -= 2*(i + k - 1)*mass[i + k - 1][j];
  sx -= 2*(i + k - 1)*mass[i + k - 1][j + k - 1];
  
  sy = getdy(i + k - 1, j + k - 1);
  sy -= getdy(i - 1, j + k - 1);
  sy -= getdy(i + k - 1, j - 1);
  sy += getdy(i - 1, j - 1);
  sy -= 2*j*mass[i][j];
  sy -= 2*(j + k - 1)*mass[i][j + k - 1];
  sy -= 2*j*mass[i + k - 1][j];
  sy -= 2*(j + k - 1)*mass[i + k - 1][j + k - 1];
  
  sm = getdm(i + k - 1, j + k - 1);
  sm -= getdm(i - 1, j + k - 1);
  sm -= getdm(i + k - 1, j - 1);
  sm += getdm(i - 1, j - 1);
  sm -= mass[i][j];
  sm -= mass[i][j + k - 1];
  sm -= mass[i + k - 1][j];
  sm -= mass[i + k - 1][j + k - 1];
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> F >> C >> D;
    for (int i = 0; i < F; ++i) {
      for (int j = 0; j < C; ++j) {
        cin >> mapa[i][j];
      }
    }
    
    for (int i = 0; i < F; ++i)
      for (int j = 0; j < C; ++j)
        mass[i][j] = D + mapa[i][j] - '0';
    
    dm[0][0] = mass[0][0];
    for (int j = 1; j < C; ++j)
      dm[0][j] = dm[0][j - 1] + mass[0][j];
    for (int i = 1; i < F; ++i) {
      dm[i][0] = dm[i - 1][0] + mass[i][0];
      for (int j = 1; j < C; ++j) {
        dm[i][j] = dm[i][j - 1] + dm[i - 1][j] - dm[i - 1][j - 1] + mass[i][j];
      }
    }
    
    dx[0][0] = 0;
    for (int j = 1; j < C; ++j)
      dx[0][j] = 0;
    for (int i = 1; i < F; ++i) {
      dx[i][0] = dx[i - 1][0] + 2*i*mass[i][0];
      for (int j = 1; j < C; ++j) {
        dx[i][j] = dx[i][j - 1] + dx[i - 1][j] - dx[i - 1][j - 1] + 2*i*mass[i][j];
      }
    }
    
    dy[0][0] = 0;
    for (int j = 1; j < C; ++j)
      dy[0][j] = dy[0][j - 1] + 2*j*mass[0][j];
    for (int i = 1; i < F; ++i) {
      dy[i][0] = 0;
      for (int j = 1; j < C; ++j) {
        dy[i][j] = dy[i][j - 1] + dy[i - 1][j] - dy[i - 1][j - 1] + 2*j*mass[i][j];
      }
    }
    
    
    int res = 0;
    
    for (int k = 3; k <= min(F, C); ++k) {
      for (int i = 0; i + k <= F; ++i) {
        for (int j = 0; j + k <= C; ++j) {
          /*ll sx = 0;
          ll sy = 0;
          ll mas = 0;
          for (int x = i; x < i + k; ++x) {
            for (int y = j; y < j + k; ++y) {
              if (x == i and y == j) continue;
              if (x == i + k - 1 and y == j) continue;
              if (x == i and y == j + k - 1) continue;
              if (x == i + k - 1 and y == j + k - 1) continue;
              ll m = D + mapa[x][y] - '0';
              sx += 2*x*m;
              sy += 2*y*m;
              mas += m;
            }
          }*/
          ll sx, sy, mas;
//           ll a, b;
          suma(i, j, k, sx, sy, mas);
          
          
          if (sx%mas != 0 or sy%mas != 0) continue;
//           cerr << "OK" << endl;
//           cerr << "(" << i << ", " << j << ", " << k << ")" << endl;
//           cerr << sum.X << " " << sum.Y << endl;
          ll mx = i + i + k - 1;
          ll my = j + j + k - 1;
          if (sx/mas == mx and sy/mas == my) {
            res = k;
          }
          if (res == k) break;
        }
        if (res == k) break;
      }
    }
    
    cout << "Case #" << cas << ": ";
    if (res == 0) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
    
  }
}
