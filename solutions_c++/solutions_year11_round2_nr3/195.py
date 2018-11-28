#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <utility>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>




int n, m, k;
std::vector<int> a[100];

int r[10];
int ans[10], col, bc;
bool was[10];

void Rec(int cur) {
  if (cur > n) {
    for (int i = 1; i <= n; ++i) {
      was[r[i]] = true;
    }
    for (int i = 1; i <= col; ++i) {
      if (!was[i]) {
        return;
      }
    }
    for (int i = 0; i < k; ++i) {
      std::memset(was, false, sizeof(was));
      for (int j = 0; j < a[i].size(); ++j) {
        was[r[a[i][j]]] = true;
      }
      for (int j = 1; j <= col; ++j) {
        if (!was[j]) {
          return;
        }
      }
    }
    for (int i = 1; i <= n; ++i) {
      ans[i] = r[i];
    }
    bc = col;
  } else {
    for (int i = 1; i <= col; ++i) {
      r[cur] = i;
      Rec(cur+1);
    }
  }
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;
  std::cin >> t;
  for (int q = 1; q <= t; ++q) {
    std::cin >> n >> m;
    int u[10], v[10];
    for (int i = 0; i < m; ++i) {
      std::cin >> u[i];
    }
    for (int i = 0; i < m; ++i) {
      std::cin >> v[i];
    }
    
    k = 1;
    a[0].clear();
    for (int i = 1; i <= n; ++i) {
      a[0].push_back(i);
    }
    for (int i = 0; i < m; ++i) {
      int f = 0;
      while (true) {
        int how = 0;
        int k1 = -1, k2 = -1;
        for (int j = 0; j < a[f].size(); ++j) {
          if (a[f][j] == u[i] || a[f][j] == v[i]) {
            ++how;
            if (k1 < 0) {
              k1 = j;
            } else {
              k2 = j;
            }
          }
        }
        if (how == 2 && k2-k1 != 1 && (k1 != 0 || k2+1 != a[f].size())) {
          break;
        }
        ++f;
      }
      int k1 = -1, k2 = -1;
      for (int j = 0; j < a[f].size(); ++j) {
        if (a[f][j] == u[i] || a[f][j] == v[i]) {
          if (k1 < 0) {
            k1 = j;
          } else {
            k2 = j;
          }
        }
      }
      a[k].clear();
      a[k].insert(a[k].begin(), a[f].begin(), a[f].begin()+k1+1);
      a[k].insert(a[k].end(), a[f].begin()+k2, a[f].end());
      a[f].erase(a[f].begin()+k2+1, a[f].end());
      a[f].erase(a[f].begin(), a[f].begin()+k1);
      ++k;
    }
    a[0] = a[0];
    
    for (int i = 1; i <= 8; ++i) {
      col = i;
      Rec(1);
    }
    
    std::printf("Case #%d: %d\n", q, bc);
    for (int i = 1; i <= n; ++i) {
      std::cout << ans[i] << " ";
    }
    std::cout << std::endl;
  }

  return 0;
}