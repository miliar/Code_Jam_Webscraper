#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <sstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define VAR(a) cout << #a << " : " << a << endl;

typedef long long int lli;

using namespace std;

const int N = 1000 + 1;
bool g[N][N];

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int node;
    cin >> node;

    fill(&g[0][0], &g[N - 1][N], false);

    for (int i = 0; i < (int)node; ++i) {
      int m;
      cin >> m;
      for (int j = 0; j < (int)m; ++j) {
        int x;
        cin >> x;
        g[i][x - 1] = true;
      }
      // g[i][i] = true;
    }

    // for (int k = 0; k < (int)node; ++k) {
    //   for (int i = 0; i < (int)node; ++i) {
    //     for (int j = 0; j < (int)node; ++j) {
    //       g[i][j] = g[i][j] || (g[i][k] && g[k][j]);
    //     }
    //   }      
    // }

    // bool flg = false;
    // for (int src = 0; src < (int)node; ++src) {
    //   for (int dst = 0; dst < (int)node; ++dst) {
    //     if (!g[src][dst] || src == dst) continue;
    //     for (int i = 0; i < (int)node; ++i) {

    //       if (i == src || i == dst) continue;    
    //       if (g[src][i] && g[i][dst]) ; else continue;

    //       for (int j = 0; j < (int)node; ++j) {
            
    //         if (i == j) continue;
    //         if (j == dst) continue;
    //         if (g[src][j] && g[j][dst]) ; else continue;

    //         flg = true;
            
    //       }
    //     }
    //   }
    // }
    // static int tc = 0;
    // cout << "Case #" << ++tc << ": " << (flg ? "Yes" : "No") << endl;


    bool flg = false;

    int t[node][node];
    for (int src = 0; src < (int)node; ++src) {
      fill(&t[0][0], &t[node - 1][node], 0);
      t[0][src] = 1;
      for (int len = 0; len + 1 < (int)node; ++len) {        
        // for (int i = 0; i < (int)node; ++i) {
        //   t[len + 1][i] += t[len][i];
        // }
        for (int n = 0; n < (int)node; ++n) {
          if (t[len][n] == 0) continue;
          for (int m = 0; m < (int)node; ++m) {
            if (g[n][m]) {
              t[len + 1][m] += t[len][n];
            }
          }
        }
      }
      if (src == 0 && false) {
        for (int i = 0; i < (int)node; ++i) {
          for (int j = 0; j < (int)node; ++j) {
            cout << t[i][j] << ", ";
          }
          cout << endl;
        }
        cout << endl;
      }
      map<int, int> cnt;
      int mx = 0;
      for (int i = 0; i < (int)node; ++i) {
        for (int j = 0; j < (int)node; ++j) {
          cnt[j] += t[i][j];
          mx = max(cnt[j], mx);
        }
      }
      if (2 <= mx) {
        flg = true;
        break;
      }
      if (src == 0 && false) 
      for (int i = 0; i < (int)node; ++i) {
        cout << i << " : " << cnt[i] << endl;
      }
    }

    static int tc = 0;
    cout << "Case #" << ++tc << ": " << (flg ? "Yes" : "No") << endl;
  }
  return 0;
}
