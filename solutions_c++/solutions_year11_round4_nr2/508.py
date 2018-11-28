#include <iostream>
#include <cstring>
#include <string>

using namespace std;

const int N = 500;

int w[N][N];
int a[N][N];

inline int calc(int a, int b, int c, int d) {
  if (c < a || d < b) return 0;
  return w[c][d] - (a > 0 ? w[a-1][d] : 0) - (b > 0 ? w[c][b-1] : 0) + (a > 0 && b > 0 ? w[a-1][b-1] : 0);
}

int go(int r, int c) {
    for (int k = min(r, c); k >= 3; k--) {
      int half = k >> 1;
      for (int i = 0; i+k <= r; i++) for (int j = 0; j+k <= c; j++) {
        unsigned long long m = 1;
        int add;
        if (k & 1) add = 1; else add = 2;
        unsigned long long pp = 0;
        unsigned long long qq = 0;
        for (int kk = 1, p = j+half-1, q = j+k-half; kk <= half; kk++, p--, q++, m += add) {
          pp += calc(i + (kk == half ? 1 : 0), p, i+k-1-(kk == half ? 1 : 0), p) * m;
          qq += calc(i + (kk == half ? 1 : 0), q, i+k-1-(kk == half ? 1 : 0), q) * m;
        }
        if (pp != qq) continue;

        pp = 0;
        qq = 0;
        m = 1;
        for (int kk = 1, p = i+half-1, q = i+k-half; kk <= half; kk++, p--, q++, m += add) {
          pp += calc(p, j + (kk == half ? 1 : 0), p, j+k-1-(kk == half ? 1 : 0)) * m;
          qq += calc(q, j + (kk == half ? 1 : 0), q, j+k-1-(kk == half ? 1 : 0)) * m;
        }

        if (pp == qq) return k;
      }
    }
    return 0;
}

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int r, c, d; cin >> r >> c >> d;
    for (int i = 0; i < r; i++) {
      string s; cin >> s;
      for (int j = 0; j < c; j++) w[i][j] = s[j]-'0';
    }
    memcpy(a, w, sizeof(a));

    for (int i = 0; i < r; i++) for (int j = 1; j < c; j++) w[i][j] += w[i][j-1];
    for (int j = 0; j < c; j++) for (int i = 1; i < r; i++) w[i][j] += w[i-1][j];
    int k = go(r, c);

    cout << "Case #" << tt << ": ";
    if (k == 0) cout << "IMPOSSIBLE" << endl; else cout << k << endl;
  }
  return 0;
}

