#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>

const int maxn = 1010;


int a[maxn];
bool b[maxn];
double p[maxn][maxn], pn[maxn][maxn], u[maxn];
int t, n;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  for (int i = 0; i < maxn; ++i) {
    for (int j = 0; j < maxn; ++j) {
      p[i][j] = 0;
      pn[i][j] = 0;
    }
  }
  p[0][0] = 1;
  p[1][0] = 0;
  p[1][1] = 1;
  pn[1][0] = 1;
  pn[1][1] = 1;
  pn[0][0] = 1;
  for (int i = 2; i < maxn; ++i) {
    for (int j = 0; j <= i; ++j) {
      if (j > 0) {
        p[i][j] = 1.0/i * (p[i-1][j-1] + pn[i-2][j]);
      } else {
        p[i][j] = 1.0/i * (pn[i-2][j]);
      }
      pn[i][j] = pn[i-1][j] + p[i][j];
    }
  }
  u[1] = 0;
  u[0] = 0;
  for (int i = 2; i < maxn; ++i) {
    double sm = 0;
    for (int j = 1; j <= i; ++j) {
      sm += p[i][j]*(u[i-j]+1);
    }
    u[i] = (sm + p[i][0])/(1-p[i][0]);
  }
  
  std::cin >> t;

  for (int tnum = 1; tnum <= t; ++tnum) { 
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
      std::cin >> a[i];
    }
    std::memset(b, false, sizeof(b));
    double ans = 0;
    for (int i = 1; i <= n; ++i) {
      if (!b[i]) {
        int v = a[a[i]];
        b[a[i]] = true;
        int cc = 1;
        while (v != a[i]) {
          ++cc;
          b[v] = true;
          v = a[v];
        }
        ans += u[cc];
      }
    }
    std::printf("Case #%d: %.10lf\n", tnum, ans);
  } 

  return 0;
}