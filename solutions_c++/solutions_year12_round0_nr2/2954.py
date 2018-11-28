#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdlib>

using namespace std;

int _N, _S, _P;
int _ans;
const int _MAXN = 110;
const int _MAXS = 110;
int _T[_MAXN][4];
int _t[_MAXN];
int _dp[_MAXN][_MAXS];

bool suprise(int a, int b, int c) {
  return a == b + 2 || b == c + 2 || a == c + 2;
}

void gen(int ti) {
  for (int i = _t[ti] / 3; i <= _t[ti]; ++i)
    for (int j = max(i - 2, 0); j <= i; ++j) {
      int k = _t[ti] - i - j;
      if (k >= 0 && k >= i - 2 && k >= j - 2 && k <= j) {
        int flg = 0;
        if (i >= _P) flg |= 1;
        if (suprise(i, j, k)) flg |= 2; 
        _T[ti][flg] = 1;
      }
    }
}

void solve() {
  cin >> _N >> _S >> _P;
  for (int i = 1; i <= _N; ++i) {
    cin >> _t[i];
    for (int j = 0; j < 4; ++j)
      _T[i][j] = 0;
    gen(i);
  }
  memset(_dp, 0, sizeof(_dp));
  for (int i = 1; i <= _N; ++i)
    for (int j = 0; j <= _S; ++j) {
      _dp[i][j] = 0;
      if (_T[i][0]) {
        _dp[i][j] = max(_dp[i][j], _dp[i-1][j]);
      }
      if (_T[i][1]) {
        _dp[i][j] = max(_dp[i][j], _dp[i-1][j] + 1);
      }
      if (_T[i][2]) {
        if (j > 0)
          _dp[i][j] = max(_dp[i][j], _dp[i-1][j-1]);
      }
      if (_T[i][3]) {
        if (j > 0)
        _dp[i][j] = max(_dp[i][j], _dp[i-1][j-1] + 1);
      }
    }
  cout << _dp[_N][_S] << endl;
}

int main() {
  int ncs;
  cin >> ncs;
  for (int i = 1; i <= ncs; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
